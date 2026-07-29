"""
Mirror gov.gitcoin.co (Discourse) into ./gov/<category>/<slug>__<id>.md.

Each topic is one markdown file: YAML-ish frontmatter + the raw markdown
body served by Discourse's public /raw/<id> endpoint (post bodies prefixed
with `username | timestamp | #N` headers, in post order).

Incremental: a topic is refetched only when its remote last_posted_at is
newer than the value stored in the local file's frontmatter.

Tunables via env:
  GOV_MAX_PAGES   stop after this many /latest.json pages (default 200)
  GOV_MAX_TOPICS  stop after writing this many topics; 0 = no limit (default 0)
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

import requests

BASE = "https://gov.gitcoin.co"
GOV_DIR = Path("gov")
USER_AGENT = "owocki-mirror/1.0"
REQUEST_DELAY = 0.5
MAX_PAGES = int(os.environ.get("GOV_MAX_PAGES", "200"))
MAX_TOPICS = int(os.environ.get("GOV_MAX_TOPICS", "0"))


def sanitize(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip().strip(".")
    return (name or "untitled")[:100]


def http_get(url: str):
    headers = {"User-Agent": USER_AGENT}
    for _ in range(3):
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After", "5"))
            time.sleep(wait + 1)
            continue
        r.raise_for_status()
        time.sleep(REQUEST_DELAY)
        return r
    raise RuntimeError(f"giving up on {url} after retries")


def get_json(url: str) -> dict:
    return http_get(url).json()


def get_text(url: str) -> str:
    return http_get(url).text


def load_categories() -> list[tuple[int, str]]:
    """Return [(id, slug), ...] including subcategories."""
    data = get_json(f"{BASE}/categories.json?include_subcategories=true")
    out: list[tuple[int, str]] = []
    for c in data["category_list"]["categories"]:
        out.append((c["id"], c["slug"]))
        for sub in c.get("subcategory_list") or []:
            out.append((sub["id"], sub["slug"]))
    return out


def parse_local_last_posted(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        with path.open() as f:
            if f.readline().strip() != "---":
                return None
            for line in f:
                if line.strip() == "---":
                    return None
                m = re.match(r"last_posted_at:\s*(\S+)", line)
                if m:
                    return m.group(1)
    except OSError:
        return None
    return None


def render(topic: dict, category_slug: str, body: str) -> str:
    tid = topic["id"]
    title = topic["title"]
    slug = topic["slug"]
    created = topic.get("created_at", "")
    last = topic.get("last_posted_at") or topic.get("bumped_at") or created
    url = f"{BASE}/t/{slug}/{tid}"

    frontmatter = [
        "---",
        f"id: {tid}",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"slug: {slug}",
        f"category: {category_slug}",
        f"url: {url}",
        f"created_at: {created}",
        f"last_posted_at: {last}",
        f"posts_count: {topic.get('posts_count', '')}",
        f"views: {topic.get('views', '')}",
        f"like_count: {topic.get('like_count', '')}",
        "---",
        "",
        f"# {title}",
        "",
        f"<{url}>",
        "",
    ]
    return "\n".join(frontmatter) + body.rstrip() + "\n"


def main():
    GOV_DIR.mkdir(parents=True, exist_ok=True)
    print(f"loading categories from {BASE} ...")
    cats = load_categories()
    print(f"  {len(cats)} categories")

    seen = written = skipped = failed = 0

    for cat_id, cat_slug in cats:
        print(f"\n=== category: {cat_slug} (id={cat_id}) ===")
        for page in range(MAX_PAGES):
            try:
                data = get_json(
                    f"{BASE}/c/{cat_id}/l/latest.json?page={page}&order=default"
                )
            except requests.HTTPError as e:
                print(f"  page={page} failed: {e}", file=sys.stderr)
                break

            topics = data.get("topic_list", {}).get("topics") or []
            if not topics:
                break

            page_writes = 0
            for t in topics:
                seen += 1
                if MAX_TOPICS and written >= MAX_TOPICS:
                    print(f"hit GOV_MAX_TOPICS={MAX_TOPICS}, stopping")
                    _summary(seen, written, skipped, failed)
                    return

                slug = t["slug"]
                tid = t["id"]
                target = GOV_DIR / sanitize(cat_slug) / f"{sanitize(slug)}__{tid}.md"

                local_last = parse_local_last_posted(target)
                remote_last = t.get("last_posted_at") or t.get("bumped_at")
                if local_last and remote_last and local_last >= remote_last:
                    skipped += 1
                    continue

                try:
                    body = get_text(f"{BASE}/raw/{tid}")
                except requests.HTTPError as e:
                    print(f"  topic {tid} ({slug}) failed: {e}", file=sys.stderr)
                    failed += 1
                    continue

                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(render(t, cat_slug, body))
                written += 1
                page_writes += 1
                print(f"  wrote {target}")

            if not data.get("topic_list", {}).get("more_topics_url"):
                break

    _summary(seen, written, skipped, failed)


def _summary(seen, written, skipped, failed):
    print(f"\ndone. seen={seen} written={written} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()
