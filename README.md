# Google-review outreach — France

This repository is the France-specific Google-review outreach campaign.

It contains:

- `MESSAGE.md` — the Google-review outreach message and drafting rules for France, written in French.
- `data/excluded_emails.txt` — France-campaign email exclusions.
- `data/excluded_facilities.txt` — France-campaign clinic/facility exclusions.
- `data/exclusions-log.txt` — successful new France drafts recorded by campaign runs.
- `data/gmail_accounts.txt` — Gmail accounts and their GitHub Actions secret-name mapping.

## France campaign scope

Only research and draft for dentists / dental clinics physically located in France. The clinic must be in an actual French **ville / town**; small towns are allowed, but villages, hamlets, isolated rural places, and genuinely rural communes without city/town character are excluded. If the location cannot be verified confidently as a city/town rather than a rural settlement, skip it.

Verify the clinic's current Google/Google Maps review count and use only clinics with **2 through 25 reviews inclusive**. Clinics with 0–1 or 26+ reviews are ineligible. Use an appropriate officially published contact email. Never guess review counts, location eligibility, or contact details.

Within the eligible range, prioritize the **lowest verified review counts first**. As a secondary signal, favor clinics with verified evidence that they are actively marketing themselves or trying to acquire patients. Marketing activity is a prioritization signal only, never an eligibility requirement, and must never be guessed.

When multiple connected Gmail accounts are available, spread genuinely new drafts across the accounts in `data/gmail_accounts.txt`. Never duplicate prospects merely to fill accounts.

Actual Gmail app-password values must remain in GitHub **Settings > Secrets and variables > Actions** and must never be committed.

**DRAFTS ONLY. NEVER SEND AUTOMATICALLY.**
