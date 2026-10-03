# Germany outreach run prompt

Run the Google-review outreach workflow using the GitHub repository `agads007-sys/dentists-germany`.

**DRAFTS ONLY. NEVER SEND EMAILS.**

Create exactly **25 new, high-quality Gmail drafts** for **dentists / dental clinics located in Germany only**.

Work in **batches of 5 successful drafts** until you reach **25 total successful drafts**. Do not research 25 prospects upfront and do not build a large candidate backlog.

For each batch:
1. Research only enough candidates to find 5 valid German prospects, then deduplicate them against the campaign exclusions and the in-memory list for this run.
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

Load the three exclusion files once and combine them into the working deduplication list for the whole run. These exclusions belong only to the Germany campaign. Do NOT use exclusion lists from `agads007-sys/dentists`, `agads007-sys/outreach-barebones`, or any other repository.

As soon as a new prospect is selected, add both its clinic name and email address to the in-memory working deduplication list so it cannot be selected again in a later batch.

Follow all messaging, verification, eligibility, Gmail-account distribution, and logging rules in `MESSAGE.md`. Only create drafts for dental clinics physically located in Germany with a verified current Google/Google Maps review count below 30 and an appropriate officially published contact email. Never guess review counts. Preserve the full campaign message while genuinely varying the wording across drafts.

After each successful batch, append the newly drafted clinic email addresses and facility names to `data/exclusions-log.txt`. Record only drafts that were actually created successfully.

Stop once exactly 25 successful new drafts have been created and recorded. Never send any email automatically.
