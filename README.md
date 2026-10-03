# Google-review outreach — Germany

This repository is the Germany-specific version of `agads007-sys/dentists`.

It contains:

- `MESSAGE.md` — the Google-review outreach message and drafting rules for Germany.
- `data/excluded_emails.txt` — Germany-campaign email exclusions.
- `data/excluded_facilities.txt` — Germany-campaign clinic/facility exclusions.
- `data/exclusions-log.txt` — successful new Germany drafts recorded by campaign runs.
- `data/gmail_accounts.txt` — Gmail accounts and their GitHub Actions secret-name mapping.

## Germany campaign scope

Only research and draft for dentists / dental clinics located in Germany. The clinic must be located in an actual German **Stadt**; small cities / **Kleinstädte** are allowed, but villages, hamlets, isolated rural places, and rural municipalities without genuine city/town character are excluded. If the location cannot be verified as a city/town rather than a rural settlement, skip it. Verify the clinic's current Google/Google Maps review count and use only clinics with **2 through 25 reviews inclusive**. Clinics with 0–1 or 26+ reviews are ineligible. Use an appropriate officially published contact email. Never guess review counts, location eligibility, or contact details.

When multiple connected Gmail accounts are available, spread genuinely new drafts across the accounts in `data/gmail_accounts.txt`. Never duplicate prospects merely to fill accounts.

Actual Gmail app-password values must remain in GitHub **Settings > Secrets and variables > Actions** and must never be committed.

**DRAFTS ONLY. NEVER SEND AUTOMATICALLY.**
