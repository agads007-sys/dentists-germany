# Google-review outreach — Germany

This repository is the Germany-specific version of `agads007-sys/dentists`.

It contains:

- `MESSAGE.md` — the Google-review outreach message and drafting rules for Germany.
- `data/excluded_emails.txt` — Germany-campaign email exclusions.
- `data/excluded_facilities.txt` — Germany-campaign clinic/facility exclusions.
- `data/exclusions-log.txt` — successful new Germany drafts recorded by campaign runs.
- `data/gmail_accounts.txt` — Gmail accounts and their GitHub Actions secret-name mapping.

## Germany campaign scope

Only research and draft for dentists / dental clinics located in Germany. Verify the clinic's current Google/Google Maps review count and use only clinics with fewer than 30 reviews. Use an appropriate officially published contact email. Never guess review counts or contact details.

The exclusion state in this repository starts clean and belongs only to the Germany campaign. Do not import or consult exclusion lists from `agads007-sys/dentists`, `agads007-sys/outreach-barebones`, or any other campaign.

When multiple connected Gmail accounts are available, spread genuinely new drafts across the accounts in `data/gmail_accounts.txt`. Never duplicate prospects merely to fill accounts.

Actual Gmail app-password values must remain in GitHub **Settings > Secrets and variables > Actions** and must never be committed.

**DRAFTS ONLY. NEVER SEND AUTOMATICALLY.**
