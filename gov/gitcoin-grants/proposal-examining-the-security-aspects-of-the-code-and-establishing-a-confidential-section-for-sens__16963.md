---
id: 16963
title: "[PROPOSAL] Examining the Security Aspects of the Code and Establishing a Confidential Section for Sensitive Information"
slug: proposal-examining-the-security-aspects-of-the-code-and-establishing-a-confidential-section-for-sensitive-information
category: gitcoin-grants
url: https://gov.gitcoin.co/t/proposal-examining-the-security-aspects-of-the-code-and-establishing-a-confidential-section-for-sensitive-information/16963
created_at: 2023-11-05T04:57:19.965Z
last_posted_at: 2023-11-05T04:57:20.036Z
posts_count: 1
views: 3376
like_count: 4
---

# [PROPOSAL] Examining the Security Aspects of the Code and Establishing a Confidential Section for Sensitive Information

<https://gov.gitcoin.co/t/proposal-examining-the-security-aspects-of-the-code-and-establishing-a-confidential-section-for-sensitive-information/16963>
philipjonsen | 2023-11-05 04:57:20 UTC | #1

(put it in grant, can't post in propsals yet:)

Background:

My journey in the realm of hacking began at an early age; when I was approximately 10 years old, I already aspired to become a hacker. During my most active years as a hacker, in my teenage years, I dedicated countless hours, often sacrificing sleep, to infiltrating diverse targets, from banks to government entities, and even military systems, among many others.

I vividly remember the day I realized that intruding into people's, businesses', and institutions' data was ethically wrong. Individuals, especially, deserved their privacy. Fast forward approximately two decades or more, I've harnessed my dream and passion to assist others using my extensive knowledge. I typically engage in this endeavor during my free time, driven by a genuine passion rather than profit. My team has collaborated with organizations such as GitLab, OpenZeppelin, NASA, and more. We primarily focus our efforts on crypto projects. It deeply concerns me when investors lose their hard-earned money, and trust and reputation hang in the balance.

I've witnessed numerous promising projects left unfinished or insecure, leading to their demise due to malicious actors. It truly saddens me to witness such outcomes.

Recently, we scrutinized some of your code and found it reasonably acceptable. However, it still harbors around 10 or more critical security vulnerabilities and over 20 major bugs that could potentially lead to catastrophic consequences. Our previous experience working directly with GitLab led to the discovery and resolution of vulnerabilities, conducted within a confidential space accessible only to developers and involved parties. This approach safeguards against publicizing potentially devastating zero-day exploits that could impact not only GitLab but also all projects following their lead. Once in the "wild," such vulnerabilities can wreak havoc.

Hence, I propose the establishment of a "confidential area" within the forum dedicated to sensitive information.

The second facet of our proposal involves a more thorough examination of your code, with a primary focus on identifying and rectifying the 15 critical flaws and the 20 major flaws, which represent the most pressing priorities. Subsequently, we will address other issues, including approximately 270 different bugs, security vulnerabilities, performance concerns, style issues, and documentation matters. We offer our services to assist in resolving the 15 critical and 20 major flaws within a 15-day timeframe from our side. We do not seek substantial compensation but perhaps a modest allocation of Gitcoins, ranging from 5,000 to 10,000 in usd preferably in BTC, GTC or USD, as this work is time-consuming and performed during our spare time.

Moreover, there are three critical flaws that can be easily rectified. The first issue pertains to an undefined variable and undefined name, which could potentially lead to various issues, including overflows and injections. For instance, ".base64." is undeclared here:passport-scorer/blob/main/api/aws_lambdas/scorer_api_passport/utils.py#L31-L31
. You can promptly address this by importing "base64."


The second security issue involves the potential for a cross-site scripting (XXS) vulnerability, which necessitates a more in-depth audit. The use of "mark_safe()" may expose an XXS vulnerability, which is particularly concerning within an admin part of the code. You can find it on line 56-57 here: /passport-scorer/blob/main/api/account/admin.py#L56-L56

This issue arises because "mark_safe" explicitly marks a string as safe for HTML output, bypassing Django's automatic string escaping. While it is an acceptable practice for internally generated strings, using it on unchecked user input poses a security risk. We recommend utilizing "format_html" where possible, as it ensures that all arguments are passed through conditionalescape(). For example, consider using "format_html("<b>%s</b>", user_input)".

We trust that this information is valuable and, hopefully, harmless. Prioritizing security is paramount, and it's better to err on the side of caution.

For further references, please consider reviewing Notable Common Weakness Enumerations (CWEs) such as CWE-79: Cross-site Scripting, CWE-89: SQL Injection, and CWE-73: External Control of File Name or Path, along with OWASP's Top Ten Project (A03: Injection) and the CWE-79 definition: "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')".

https://owasp.org/Top10/A03_2021-Injection/

https://cwe.mitre.org/data/definitions/79.html

mark_safe() : https://docs.djangoproject.com/en/3.0/ref/utils/#django.utils.safestring.mark_safe


Thank you for taking the time to read and understand my perspective. I remain at your service to support my fellow crypto enthusiasts.

Be blessed, 
Philip

-------------------------
