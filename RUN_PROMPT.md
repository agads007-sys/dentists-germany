# France outreach run prompt

Run the Google-review outreach workflow using the GitHub repository `agads007-sys/dentists-germany`.

**DRAFTS ONLY. NEVER SEND EMAILS.**

Create exactly **25 new, high-quality Gmail drafts** for **dentists / dental clinics located in France only**.

Eligible prospects must meet ALL of these conditions:

- Dentist / dental clinic only.
- Physically located in France.
- Located in an actual French city/town (`ville`). Small towns are allowed. Villages, hamlets, isolated rural locations, and genuinely rural communes without city/town character are not eligible. If the location cannot be verified confidently as a city/town rather than a rural settlement, skip it.
- Prefer verified Google/Google Maps review counts for genuine personalization, but a missing verified count does not disqualify an otherwise suitable clinic. Never invent a count or claim a comparison that was not made.
- An appropriate officially published contact email must be available.
- Never guess the review count, local comparisons, city/town eligibility, contact details, or marketing activity. If the Google profile/count cannot be verified, use the no-count version in MESSAGE.md.

Work in **batches of 5 successful drafts** until you reach **25 total successful drafts**. Do not research 25 prospects upfront and do not build a large candidate backlog.

For each batch:

1. Research only enough candidates to find 5 valid French prospects, then deduplicate them against the campaign exclusions and the in-memory list for this run.
2. Create the 5 Gmail drafts.
3. Update `data/exclusions-log.txt` for those successful drafts only.
4. Continue with the next batch using the same in-memory deduplication list plus all clinics and email addresses selected during the run.

If you cannot create the valid drafts you can verify, update the exclusion log for those successful drafts, and stop the entire run. Do not search indefinitely.

At the beginning of the run, read once:

- `MESSAGE.md`
- `data/excluded_emails.txt`
- `data/excluded_facilities.txt`
- `data/exclusions-log.txt`
- `data/gmail_accounts.txt`

Load the three exclusion files once and combine them into the working deduplication list for the whole run. These exclusions belong only to the France campaign. Do NOT use exclusion lists from `agads007-sys/dentists`, `agads007-sys/outreach-barebones`, or any other repository.

As soon as a new prospect is selected, add both its clinic name and email address to the in-memory working deduplication list so it cannot be selected again in a later batch.

Follow all messaging, verification, eligibility, Gmail-account distribution, and logging rules in `MESSAGE.md`.

For every draft, preserve the exact campaign skeleton in this order. Genuine discovery of the clinic in the area. Verified review count if available, otherwise a confident but general opportunity to develop reviews. Real nearby comparison only if actually checked, otherwise an explanation of why patients compare clinics. Explanation of why reviews matter to patients. Explanation that reviews can also affect local Google visibility. Natural transition into why Michael is writing. Very simple SMS product explanation. Minimal effort for the clinic. Strong conviction that consistent use can make a difference over time. Michael handles setup. Exact price of **39.99 per month**, without any currency word or symbol in draft copy. No long-term commitment. Short natural CTA. Signature from Michael Berg.

Write the actual emails in natural conversational French, not translated German. They should sound like something a French person would genuinely send. Use ordinary paragraphs and simple punctuation. Do not use dashes or colons as stylistic devices in the email copy. Avoid semicolons, headings, list-like phrasing, agency language, and artificial sales copy.

**SUBJECT RULE: Never write « avis Google », « Google reviews », « Google-Bewertungen » or equivalents about Google reviews in the email subject.** Use short neutral subjects such as « Une petite idée pour votre cabinet » or « Concernant votre cabinet ».

**PRICE RULE: Never put any currency word or symbol into the subject or body.** Write « 39.99 par mois » in French.

Use the same warm, confident sales tone whether review data is verified or not. If the Google listing or count is not verified, use the secondary message in MESSAGE.md, without pretending to have inspected the listing, counted its reviews, or compared competitors.

After each successful batch, append the newly drafted clinic email addresses and facility names to `data/exclusions-log.txt`. Record only drafts that were actually created successfully.

Stop once exactly 25 successful new drafts have been created and recorded. Never send any email automatically.
