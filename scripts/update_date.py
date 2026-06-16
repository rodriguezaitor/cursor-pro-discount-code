#!/usr/bin/env python3
"""Update date/month markers across repo files for daily SEO freshness."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def replace_marker(content: str, marker: str, value: str) -> str:
    pattern = rf"<!-- {marker} -->.*?<!-- /{marker} -->"
    replacement = f"<!-- {marker} -->{value}<!-- /{marker} -->"
    return re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)


def main() -> None:
    now = datetime.now(timezone.utc)
    verified = now.strftime("%A, %B %d, %Y")
    month_year = now.strftime("%B %Y")
    iso_date = now.strftime("%Y-%m-%d")

    for path in (ROOT / "README.md", ROOT / "FAQ.md"):
        text = path.read_text(encoding="utf-8")
        text = replace_marker(text, "DATE_VERIFIED", verified)
        text = replace_marker(text, "MONTH_YEAR", month_year)
        path.write_text(text, encoding="utf-8")

    index_path = ROOT / "docs" / "index.html"
    html = index_path.read_text(encoding="utf-8")
    html = replace_marker(html, "DATE_VERIFIED", verified)
    html = replace_marker(html, "MONTH_YEAR", month_year)
    index_path.write_text(html, encoding="utf-8")

    updated_path = ROOT / "UPDATED.txt"
    updated_path.write_text(
        "\n".join(
            [
                f"last_verified={iso_date}",
                f"verified_display={verified}",
                f"month_year={month_year}",
                f"updated_by=rodriguezaitor",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Updated dates to {verified} ({month_year})")


if __name__ == "__main__":
    main()
