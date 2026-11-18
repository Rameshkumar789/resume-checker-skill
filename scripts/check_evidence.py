"""Validate references between explicitly supplied career evidence and a bullet map."""
import argparse
import json
from pathlib import Path


def check_evidence(bank, mapping):
    errors, warnings = [], []
    records = bank.get("records", []) if isinstance(bank, dict) else bank
    if not isinstance(records, list):
        return ["Career records must be a list."], []
    indexed = {}
    for index, record in enumerate(records):
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            errors.append(f"Record {index + 1} needs a string id.")
            continue
        evidence_id = record["id"]
        if evidence_id in indexed:
            errors.append(f"Duplicate evidence id: {evidence_id}")
        indexed[evidence_id] = record

    if isinstance(mapping, list):
        variants = {"draft": {"bullets": mapping}}
    elif isinstance(mapping, dict) and isinstance(mapping.get("bullets"), list):
        variants = {"draft": mapping}
    elif isinstance(mapping, dict):
        variants = mapping
    else:
        return errors + ["Bullet map must be an object or list."], warnings

    count = 0
    for variant, entry in variants.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("bullets"), list):
            errors.append(f"Variant {variant} needs a bullets list.")
            continue
        for number, bullet in enumerate(entry["bullets"], 1):
            count += 1
            prefix = f"{variant} bullet {number}"
            if not isinstance(bullet, dict):
                errors.append(f"{prefix} must be an object.")
                continue
            ids = bullet.get("evidence_ids")
            if not isinstance(ids, list) or not ids or not all(isinstance(x, str) for x in ids):
                errors.append(f"{prefix} needs a nonempty evidence_ids list.")
                continue
            if not isinstance(bullet.get("bullet"), str) or not bullet["bullet"].strip():
                errors.append(f"{prefix} needs nonempty bullet text.")
            for evidence_id in ids:
                if evidence_id not in indexed:
                    errors.append(f"{prefix} references unknown evidence: {evidence_id}")
                    continue
                status = str(indexed[evidence_id].get("verification", "")).lower()
                if status in {"conflicting", "resume_only", "unknown"}:
                    warnings.append(f"{prefix} references unresolved evidence: {evidence_id}")
    if count == 0:
        errors.append("No mapped bullets found.")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("career_bank", type=Path)
    parser.add_argument("bullet_map", type=Path)
    args = parser.parse_args()
    try:
        bank = json.loads(args.career_bank.read_text())
        mapping = json.loads(args.bullet_map.read_text())
        errors, warnings = check_evidence(bank, mapping)
    except (OSError, ValueError) as exc:
        print(f"Input could not be read: {type(exc).__name__}")
        return 1
    print(json.dumps({"errors": errors, "warnings": warnings}, indent=2))
    print("Reference checks only; claim meaning and metric attribution still require review.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
