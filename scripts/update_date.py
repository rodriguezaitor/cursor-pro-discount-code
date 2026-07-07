#!/usr/bin/env python3
"""Update date/month markers across repo files for daily SEO freshness."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MARKDOWN_FILES = [
    "README.md",
    "FAQ.md",
    "INDEX.md",
    "CURSOR-COUPON-CODE.md",
    "CURSOR-REFERRAL-CODE.md",
    "CURSOR-PRO-PRICING.md",
    "CURSOR-PRO-VS-COPILOT.md",
]

HTML_FILES = [
    "docs/index.html",
    "docs/coupon.html",
    "docs/referral.html",
    "docs/pricing.html",
]


def replace_marker(content: str, marker: str, value: str) -> str:
    pattern = rf"<!-- {marker} -->.*?<!-- /{marker} -->"
    replacement = f"<!-- {marker} -->{value}<!-- /{marker} -->"
    return re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)


def update_file(path: Path, verified: str, month_year: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_marker(text, "DATE_VERIFIED", verified)
    text = replace_marker(text, "MONTH_YEAR", month_year)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    now = datetime.now(timezone.utc)
    verified = now.strftime("%A, %B %d, %Y")
    month_year = now.strftime("%B %Y")
    iso_date = now.strftime("%Y-%m-%d")

    for name in MARKDOWN_FILES:
        update_file(ROOT / name, verified, month_year)

    for name in HTML_FILES:
        update_file(ROOT / name, verified, month_year)

    (ROOT / "UPDATED.txt").write_text(
        "\n".join(
            [
                f"last_verified={iso_date}",
                f"verified_display={verified}",
                f"month_year={month_year}",
                "updated_by=rodriguezaitor",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Updated dates to {verified} ({month_year})")


if __name__ == "__main__":
    main()
