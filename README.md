# DAB — Flexible Business Outreach Workspace

This repository controls **research and Gmail draft creation** for the Google review invitation service. **DAB is the signature label only in outbound emails. Never write "I run DAB", "DAB offers", or use "DAB" anywhere in the subject or body.**

## A command like "5 drafts for England" must work
- **No industry specified:** Discover suitable prospects across different industries, such as independent car service businesses, detailing, physiotherapy, podiatry, veterinary practices, or other appropriate local businesses. Do not default to garages. Aim for at least three industries in a five-draft batch when verifiable prospects permit.
- **One or more industries specified:** Follow the user's selection. Industry discovery remains flexible within those bounds.
- **Any requested count:** 5, 20, 30, 70, etc. means an aim for that many **verified Gmail drafts**, not permission to send or invent leads.
- Switch industries when the available contacts are generic, inaccessible, irrelevant, or unverifiable. If the quota is impossible with reliable contacts, report a shortfall.

## Mandatory research and contact standard
1. Find a real, active business in the requested market with a plausible reason to collect genuine Google reviews.
2. Identify a **named** owner, director, partner or relevant manager. Verify their role.
3. Find that person's **direct, publicly available business email** and verify its attribution. Never infer an email from a name or guess a format.
4. **Reject shared/role inboxes** such as `info@`, `contact@`, `hello@`, `service@`, `admin@`, `office@`, `reception@`, `praxis@`, `support@`, etc., including variations.
5. Verify one factual, specific, relevant observation for the email. Review counts, ratings and competitor comparisons require verification before mention.
6. Deduplicate prospects within the run and check accessible past-contact and opt-out records; honor known opt-outs. Removing historical exclusion-list files does not erase earlier contact or permission obligations.
7. Don't substitute a generic email, an invented identity or an invented claim just to meet the requested number.

## Mandatory outbound copy standard — do not deviate
- The actual service: after an appropriate completed service/appointment, staff enter a customer phone number with permission; the customer gets an SMS link inviting a **voluntary, honest Google review**. The service provider handles setup.
- **The company label "DAB" can appear only as the last line of the email signature, immediately after "Michael". It cannot appear in the subject or body, even as "I run DAB".** The signature must end exactly:
  ```text
  Michael
  DAB
  ```
- Refer to the offer naturally in the body as **"I run a simple service..."**, **"I've built a simple service..."**, or an equivalent personal, plain explanation. Do not put the company acronym into the body.
- Approx. 75–115 words (excluding signature), short truthful subject, one verified neutral/positive observation, one simple explanation, one non-pushy question. No criticism of the company's review count, long SEO explanation, fictional proof, guaranteed outcomes, or unapproved pricing/trials.
- **Meaningful variation:** tailored subject, opening, business-specific use-case, natural phrasing and CTA; no five virtually identical emails with replaced names.
- Read `MESSAGE.md` for current copy rules and examples. Validate every drafted message with `validate_draft.py` where code execution is available **before** saving it to Gmail; all other requirements still need human/agent source verification.
- **Drafts only. Never send or schedule emails** unless the user explicitly requests a separate sending action and it is appropriate.

## Ten Gmail accounts for drafts
The canonical mapping is [`data/gmail_accounts.txt`](data/gmail_accounts.txt). These ten accounts were verified through their connected Gmail profiles on 2026-11-23. **Read the map at the beginning of every run and confirm live access.** For 10 or more drafts, distribute drafts as evenly as practical across available accounts on that list; for smaller requests, use a subset. Never use a connected account outside the list without explicit authorization. No passwords or app passwords belong in this repository.

## Required operating sequence
1. Read `README.md`, `MESSAGE.md`, `RUN_PROMPT.md` and `data/gmail_accounts.txt` on every fresh run.
2. Research leads and verify named direct contacts and observation sources.
3. Write each email using the business-specific facts.
4. Check all copy gates: no DAB in subject/body; signature only; named/direct email; no generic inbox; accurate service; 75–115 words where practicable; meaningful variation; no made-up data.
5. Run `validate_draft.py` when possible, then save Gmail draft and verify that Gmail returned a draft ID. Code validation cannot verify factual truth, recipient permission, nor whether Gmail was actually accessed.
6. Report verified contacts by sector, source evidence, actual draft counts, rejected generic contacts and shortfalls. Do not claim that drafts have been sent, delivered, or opened.

**No historical lead logs/exclusion files are included in the new current branch.** The repository is intentionally general-purpose. Git history is not deleted by file replacement.
