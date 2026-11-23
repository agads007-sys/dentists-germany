#!/usr/bin/env python3
"""DAB draft preflight. Run: python validate_draft.py draft.json
JSON fields: {"to": "person@company.example", "subject": "...", "body": "..."}.
This checks mechanical rules only. The research facts, public attribution of a
direct email, recipient eligibility, permission, opt-outs, and meaningful copy
variation MUST be checked separately.
"""
import json
import re
import sys
from pathlib import Path

SHARED_PREFIXES = (
    "info", "contact", "hello", "office", "admin", "reception",
    "service", "support", "sales", "team", "mail", "enquiries",
    "inquiries", "appointments", "appointment", "booking",
    "bookings", "praxis", "general", "enquiry", "inquiry",
)

def validate(record):
    errors = []
    recipient = str(record.get("to", "")).strip().lower()
    subject = str(record.get("subject", ""))
    body = str(record.get("body", "")).replace("\r\n", "\n").rstrip()
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", recipient):
        errors.append("Recipient must be a syntactically valid email address.")
    else:
        local = recipient.split("@", 1)[0]
        if any(re.match(r"^" + re.escape(p) + r"(?:$|[._+\-\d])", local) for p in SHARED_PREFIXES):
            errors.append("Recipient appears to be a generic/shared inbox.")
    if not subject.strip():
        errors.append("Subject is required.")
    if re.search(r"\bdab\b", subject, flags=re.I):
        errors.append("DAB is prohibited in the subject.")
    lines = body.split("\n")
    if len(lines) < 3 or lines[-2:] != ["Michael", "DAB"]:
        errors.append("Body must end exactly with the two signature lines: Michael / DAB.")
    unsigned = "\n".join(lines[:-2]) if len(lines) >= 2 else body
    if re.search(r"\bdab\b", unsigned, flags=re.I):
        errors.append("DAB is prohibited anywhere above the signature.")
    if len(re.findall(r"\bdab\b", body, flags=re.I)) != 1:
        errors.append("DAB must occur exactly once in the complete body.")
    words = len(unsigned.split())
    if words < 60 or words > 130:
        errors.append(f"Body has {words} words before signature; expected roughly 75–115 (hard band 60–130).")
    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_draft.py draft.json", file=sys.stderr)
        return 2
    try:
        record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        errors = validate(record)
    except (ValueError, OSError) as exc:
        print(f"Invalid input: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("FAIL")
        for error in errors:
            print("- " + error)
        return 1
    print("PASS — mechanical gates only; research and permission checks still required")
    return 0

if __name__ == "__main__":
    sys.exit(main())
