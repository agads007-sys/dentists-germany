# France outreach run prompt

Run the Google-review outreach workflow using the GitHub repository `agads007-sys/dentists-germany`.

**DRAFTS ONLY. NEVER SEND EMAILS.**

Create exactly **25 new, high-quality Gmail drafts** for **dentists / dental clinics located in France only**.

Eligible prospects must meet ALL of these conditions:

- Dentist / dental clinic only.
- Physically located in France.
- Located in an actual French city/town (`ville`). Small towns are allowed. Villages, hamlets, isolated rural locations, and genuinely rural communes without city/town character are not eligible. If the location cannot be verified confidently as a city/town rather than a rural settlement, skip it.
- Verified current Google/Google Maps review count of **2 through 25 inclusive**. Clinics with 0–1 or 26+ reviews are ineligible.
- An appropriate officially published contact email must be available.
- Never guess the review count, city/town eligibility, contact details, or marketing activity.

Within the eligible **2–25 review** range, prioritize prospects with the **lowest verified current Google/Google Maps review counts first**.

As a secondary priority, favor eligible clinics that have **verified signs they are actively marketing themselves or trying to attract patients**. Examples include active promotional campaigns, advertising, active social-media marketing, SEO or landing-page activity, or other clearly observable current marketing. Treat this only as a prioritization signal, not an eligibility requirement, and never guess or invent marketing activity.

Work in **batches of 5 successful drafts** until you reach **25 total successful drafts**. Do not research 25 prospects upfront and do not build a large candidate backlog.

For each batch:

1. Research only enough candidates to find 5 valid French prospects, then deduplicate them against the campaign exclusions and the in-memory list for this run.
2. Create the 5 Gmail drafts.
3. Update `data/exclusions-log.txt` for those successful drafts only.
4. Continue with the next batch using the same in-memory deduplication list plus all clinics and email addresses selected during the run.

If you cannot realistically verify 5 suitable prospects in a batch without excessive searching, create the valid drafts you can verify, update the exclusion log for those successful drafts, and stop the entire run. Do not search indefinitely.

At the beginning of the run, read once:

- `MESSAGE.md`
- `data/excluded_emails.txt`
- `data/excluded_facilities.txt`
- `data/exclusions-log.txt`
- `data/gmail_accounts.txt`

Load the three exclusion files once and combine them into the working deduplication list for the whole run. These exclusions belong only to the France campaign. Do NOT use exclusion lists from `agads007-sys/dentists`, `agads007-sys/outreach-barebones`, or any other repository.

As soon as a new prospect is selected, add both its clinic name and email address to the in-memory working deduplication list so it cannot be selected again in a later batch.

Follow all messaging, verification, eligibility, Gmail-account distribution, and logging rules in `MESSAGE.md`.

For every draft, preserve the exact campaign skeleton in this order. Observation of the clinic on Google. Verified low review count. Comparison with other nearby clinics. Explanation of why reviews matter to patients. Explanation that reviews can also affect local Google visibility. Natural transition into why Michael is writing. Very simple SMS product explanation. Minimal effort for the clinic. Strong conviction that consistent use can make a large difference over time. Michael handles setup. Exact price of **39,99 € per month**. No long-term commitment. Short natural CTA. Signature from Michael Berg.

Write the actual emails in natural conversational French, not translated German. They should sound like something a French person would genuinely send. Use ordinary paragraphs and simple punctuation. Do not use dashes or colons as stylistic devices in the email copy. Avoid semicolons, headings, list-like phrasing, agency language, and artificial sales copy.

After each successful batch, append the newly drafted clinic email addresses and facility names to `data/exclusions-log.txt`. Record only drafts that were actually created successfully.

Stop once exactly 25 successful new drafts have been created and recorded. Never send any email automatically.
