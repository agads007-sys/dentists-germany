# Google-review outreach — Germany

This repository is the Germany-specific version of `agads007-sys/dentists`.

It contains:

- `MESSAGE.md` — the Google-review outreach message and drafting rules for Germany.
- `data/excluded_emails.txt` — Germany-campaign email exclusions.
- `data/excluded_facilities.txt` — Germany-campaign clinic/facility exclusions.
- `data/exclusions-log.txt` — successful new Germany drafts recorded by campaign runs.
- `data/gmail_accounts.txt` — Gmail accounts and their GitHub Actions secret-name mapping.

## Germany campaign scope

Only research and draft for dentists / dental clinics located in Germany, in cities, can be small cities, but never completely rural places with tiny populations. Verify the clinic's current Google/Google Maps review count and use only clinics with between 1-25 reviews. Use an appropriate officially published contact email. Never guess review counts or contact details.

When multiple connected Gmail accounts are available, spread genuinely new drafts across the accounts in `data/gmail_accounts.txt`. Never duplicate prospects merely to fill accounts.

Actual Gmail app-password values must remain in GitHub **Settings > Secrets and variables > Actions** and must never be committed.

**DRAFTS ONLY. NEVER SEND AUTOMATICALLY.**
