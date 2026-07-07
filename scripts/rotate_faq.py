#!/usr/bin/env python3
"""Append one rotating FAQ entry to FAQ.md from faq_pool.json."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAQ_PATH = ROOT / "FAQ.md"
POOL_PATH = ROOT / "scripts" / "faq_pool.json"
STATE_PATH = ROOT / "scripts" / ".faq_rotate_index"

MARKER_START = "<!-- ROTATING_FAQ_START -->"
MARKER_END = "<!-- ROTATING_FAQ_END -->"


def main() -> None:
    pool = json.loads(POOL_PATH.read_text(encoding="utf-8"))
    index = 0
    if STATE_PATH.exists():
        index = int(STATE_PATH.read_text(encoding="utf-8").strip())
    index = index % len(pool)
    entry = pool[index]
    STATE_PATH.write_text(str((index + 1) % len(pool)), encoding="utf-8")

    month_year = datetime.now(timezone.utc).strftime("%B %Y")
    block = (
        f"{MARKER_START}\n\n"
        f"## Rotating FAQ — {month_year}\n\n"
        f"### {entry['question']}\n\n"
        f"{entry['answer']}\n\n"
        f"{MARKER_END}"
    )

    text = FAQ_PATH.read_text(encoding="utf-8")
    if MARKER_START in text:
        start = text.index(MARKER_START)
        end = text.index(MARKER_END) + len(MARKER_END)
        text = text[:start] + block + text[end:]
    else:
        insert_at = text.rfind("## Keywords")
        if insert_at == -1:
            insert_at = len(text)
        text = text[:insert_at] + block + "\n\n" + text[insert_at:]

    FAQ_PATH.write_text(text, encoding="utf-8")
    print(f"Rotated FAQ #{index}: {entry['question']}")


if __name__ == "__main__":
    main()
