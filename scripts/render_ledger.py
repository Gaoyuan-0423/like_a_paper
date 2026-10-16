#!/usr/bin/env python3
"""Render a like-a-paper JSONL sentence ledger as a human-readable Markdown file."""

from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a JSONL sentence ledger to Markdown.")
    parser.add_argument("ledger", help="Path to sentence_ledger.jsonl")
    parser.add_argument("--output", help="Output Markdown path; stdout when omitted")
    return parser.parse_args()


def text(value: Any, fallback: str = "—") -> str:
    if value is None:
        return fallback
    rendered = str(value).strip()
    return rendered or fallback


def load_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_no, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                continue
            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"line {line_no}: invalid JSON: {exc.msg}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"line {line_no}: record must be an object")
            records.append(record)
    return records


def render_evidence(evidence: Any) -> list[str]:
    if not isinstance(evidence, list) or not evidence:
        return ["- No evidence record (valid only for a justified rhetorical or objective sentence)."]

    lines: list[str] = []
    for item in evidence:
        if not isinstance(item, dict):
            lines.append("- Invalid evidence item.")
            continue
        evidence_id = text(item.get("evidence_id"))
        evidence_type = text(item.get("evidence_type"))
        relation = text(item.get("support_relation"))
        citation = text(item.get("citation"), "")
        locator = text(item.get("locator"))
        source_text_type = text(item.get("source_text_type"))
        source_note = text(item.get("source_text"))
        label = f"- **{evidence_id}** — `{evidence_type}` / `{relation}`"
        if citation:
            label += f" — {citation}"
        lines.append(label)
        lines.append(f"  - Locator: {locator}")
        lines.append(f"  - {source_text_type}: {source_note}")
    return lines


def render(records: list[dict[str, Any]]) -> str:
    grouped: OrderedDict[str, OrderedDict[str, list[dict[str, Any]]]] = OrderedDict()
    for record in records:
        section = text(record.get("section"), "Unspecified section")
        paragraph = text(record.get("paragraph_id"), "Unspecified paragraph")
        grouped.setdefault(section, OrderedDict()).setdefault(paragraph, []).append(record)

    lines = [
        "# Bilingual sentence ledger",
        "",
        f"Total candidate sentences: {len(records)}",
        "",
        "> This document is an audit and approval surface, not the clean submission manuscript.",
        "",
    ]

    for section, paragraphs in grouped.items():
        lines.extend([f"## {section}", ""])
        for paragraph, paragraph_records in paragraphs.items():
            lines.extend([f"### {paragraph}", ""])
            for record in paragraph_records:
                sentence_id = text(record.get("sentence_id"))
                function = text(record.get("function"))
                status = text(record.get("status"))
                lines.extend(
                    [
                        f"#### {sentence_id} — {function} — `{status}`",
                        "",
                        "**English**",
                        "",
                        text(record.get("english")),
                        "",
                        "**中文**",
                        "",
                        text(record.get("chinese")),
                        "",
                        "**Claim type and ceiling**",
                        "",
                        f"- Type: `{text(record.get('claim_type'))}`",
                        f"- Ceiling: {text(record.get('claim_ceiling'))}",
                        "",
                        "**Evidence**",
                        "",
                    ]
                )
                lines.extend(render_evidence(record.get("evidence")))
                lines.extend(
                    [
                        "",
                        "**Logic**",
                        "",
                        f"- Previous: {text(record.get('previous_link'))}",
                        f"- Next: {text(record.get('next_link'))}",
                        "",
                        "**Risks and review**",
                        "",
                    ]
                )
                flags = record.get("risk_flags")
                if isinstance(flags, list) and flags:
                    lines.extend(f"- `{text(flag)}`" for flag in flags)
                else:
                    lines.append("- No active risk flag recorded.")

                approved_by = text(record.get("approved_by"), "")
                approved_at = text(record.get("approved_at"), "")
                if approved_by or approved_at:
                    lines.append(f"- Approval: {approved_by or 'unspecified'} at {approved_at or 'unspecified'}")
                notes = text(record.get("notes"), "")
                if notes:
                    lines.append(f"- Notes: {notes}")
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    input_path = Path(args.ledger).expanduser().resolve()
    if not input_path.is_file():
        print(f"Ledger not found: {input_path}", file=sys.stderr)
        return 2

    try:
        records = load_records(input_path)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output = render(records)
    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8", newline="\n")
        print(f"Rendered {len(records)} sentences to {output_path}")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
