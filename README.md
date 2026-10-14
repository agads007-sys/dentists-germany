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

Use current verified Google/Google Maps review counts for personalized drafts when available. If a Google profile or review count cannot be verified, use the equally natural no-count message variant in `MESSAGE.md` without pretending to have checked the profile or local competitors. A missing review count, or a count outside the former 2–25 range, does not automatically disqualify an otherwise suitable private clinic. Use an appropriate officially published contact email. Never guess review counts, location eligibility, or contact details.

When counts are verified, lower review counts may be a prioritization signal but are not a mandatory filter. Favor private dental clinic owners/partners; deduplicate clinics and contact emails, and exclude institution-only addresses and known non-owner roles when a clinic decision-maker is available. As a secondary signal, favor clinics with verified evidence that they are actively marketing themselves or trying to acquire patients. Marketing activity is a prioritization signal only, never an eligibility requirement, and must never be guessed.

Email subjects must not mention « avis Google », « Google reviews » or equivalent phrases. In the body, write the price as **39.99 par mois**, never with any currency word or symbol. Keep the same sales skeleton for the verified-count and no-count versions.

When multiple connected Gmail accounts are available, spread genuinely new drafts across the accounts in `data/gmail_accounts.txt`. Never duplicate prospects merely to fill accounts.

Actual Gmail app-password values must remain in GitHub **Settings > Secrets and variables > Actions** and must never be committed.

**DRAFTS ONLY. NEVER SEND AUTOMATICALLY.**
