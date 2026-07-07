#!/usr/bin/env python3
"""Generate GitHub Pages HTML files with shared SEO structure and JSON-LD."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

REFERRAL_URL = "https://cursor.com/referral?code=GZZUNCYJJTMR"
CODE = "GZZUNCYJJTMR"
SITE_BASE = "https://rodriguezaitor.github.io/cursor-pro-discount-code"
REPO_URL = "https://github.com/rodriguezaitor/cursor-pro-discount-code"

STYLES = """
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.6; color: #1a1a1a; background: #fafafa; padding: 2rem 1rem; max-width: 720px; margin: 0 auto; }
    h1 { font-size: 1.75rem; margin-bottom: 1rem; }
    h2 { font-size: 1.25rem; margin: 2rem 0 0.75rem; }
    p { margin-bottom: 1rem; }
    .cta { display: inline-block; background: #000; color: #fff; padding: 0.875rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600; margin: 1rem 0; }
    .cta:hover { background: #333; }
    code { background: #eee; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.95rem; }
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
    th, td { border: 1px solid #ddd; padding: 0.5rem 0.75rem; text-align: left; }
    th { background: #f0f0f0; }
    .note { font-size: 0.875rem; color: #666; }
    ul { margin: 0.5rem 0 1rem 1.5rem; }
    a { color: #0969da; }
    hr { border: none; border-top: 1px solid #ddd; margin: 2rem 0; }
    nav { margin: 1rem 0; font-size: 0.9rem; }
"""

PAGES = [
    {
        "filename": "index.html",
        "title": "Cursor Pro Discount Code 2026 — 50% OFF First Month | GZZUNCYJJTMR",
        "description": "Get 50% OFF your first month of Cursor Pro, Pro+ or Ultra. Verified Cursor referral code GZZUNCYJJTMR — active discount code, promo code and coupon for 2026.",
        "keywords": "cursor promo code, cursor discount code, cursor referral code, cursor coupon code, cursor coupon 2026, cursor pro half price, get cursor pro free, cursor activation code",
        "h1": "Get 50% OFF Your First Month of Cursor Pro",
        "intro": "Looking for a <strong>Cursor Pro discount code</strong>, <strong>Cursor coupon code</strong>, or <strong>Cursor referral code</strong>? Use our verified referral link to get <strong>50% off your first month</strong> of Cursor Pro, Pro+, or Ultra.",
        "faqs": [
            ("Does this Cursor discount code work in 2026?", "Yes. Referral code GZZUNCYJJTMR is active for new signups throughout 2026."),
            ("Which plans get 50% off?", "Pro, Pro+, and Ultra all qualify for the first-month discount."),
            ("Is this an official Cursor link?", "Yes. The URL is hosted on cursor.com."),
        ],
        "extra_body": """
  <h2>Why Cursor Pro?</h2>
  <ul>
    <li>AI tab completion across multiple lines</li>
    <li>Full-codebase indexing and chat</li>
    <li>Access to leading AI models</li>
    <li>AI agents and automations</li>
  </ul>
  <hr>
  <h2>中文 — Cursor Pro 优惠码</h2>
  <p>新用户通过推荐码 <code>GZZUNCYJJTMR</code> 注册，订阅 Cursor Pro、Pro+ 或 Ultra 第一个月享受 <strong>50% 半价优惠</strong>。</p>
  <a class="cta" href="https://cursor.com/referral?code=GZZUNCYJJTMR">点击获取 Cursor Pro 半价优惠</a>
""",
    },
    {
        "filename": "coupon.html",
        "title": "Cursor Coupon Code 2026 — 50% OFF | GZZUNCYJJTMR",
        "description": "Active Cursor coupon code GZZUNCYJJTMR for 50% off your first month of Cursor Pro, Pro+ or Ultra. Official referral coupon for new users in 2026.",
        "keywords": "cursor coupon code, cursor coupon 2026, cursor promo code, cursor discount code, cursor pro coupon",
        "h1": "Cursor Coupon Code 2026 — 50% OFF",
        "intro": "Use <strong>Cursor coupon code</strong> <code>GZZUNCYJJTMR</code> to get <strong>50% off your first month</strong> of Cursor Pro, Pro+, or Ultra. Official referral coupon for new users.",
        "faqs": [
            ("What is the Cursor coupon code for 2026?", "GZZUNCYJJTMR — gives 50% off the first month for new users."),
            ("How do I apply the coupon?", "Sign up via the referral link. The discount applies automatically at checkout."),
            ("Can existing users use this coupon?", "No. This coupon is for new users only."),
        ],
        "extra_body": """
  <h2>How to redeem</h2>
  <ol>
    <li>Click the referral link above</li>
    <li>Create a new Cursor account</li>
    <li>Choose Pro, Pro+, or Ultra</li>
    <li>50% off applies at checkout</li>
  </ol>
""",
    },
    {
        "filename": "referral.html",
        "title": "Cursor Referral Code 2026 — 50% OFF | GZZUNCYJJTMR",
        "description": "Official Cursor referral code GZZUNCYJJTMR for 50% off your first month. Active cursor referral link for Pro, Pro+ and Ultra plans in 2026.",
        "keywords": "cursor referral code, cursor referral link, cursor invite code, cursor discount code, cursor pro referral",
        "h1": "Cursor Referral Code 2026",
        "intro": "The official <strong>Cursor referral code</strong> is <code>GZZUNCYJJTMR</code>. New users get <strong>50% off their first month</strong> on any paid plan.",
        "faqs": [
            ("What is the Cursor referral code?", "GZZUNCYJJTMR — use it via https://cursor.com/referral?code=GZZUNCYJJTMR"),
            ("Referral vs coupon code?", "On Cursor they work the same — both give 50% off the first month."),
            ("Can I share this referral code?", "Yes. Share the link with anyone who wants to try Cursor."),
        ],
        "extra_body": """
  <h2>Referral code details</h2>
  <table>
    <tr><th>Field</th><th>Value</th></tr>
    <tr><td>Code</td><td><code>GZZUNCYJJTMR</code></td></tr>
    <tr><td>Discount</td><td>50% off first month</td></tr>
    <tr><td>Plans</td><td>Pro, Pro+, Ultra</td></tr>
    <tr><td>Eligible users</td><td>New signups only</td></tr>
  </table>
""",
    },
    {
        "filename": "pricing.html",
        "title": "Cursor Pro Pricing 2026 — Plans & 50% Referral Discount",
        "description": "Cursor Pro pricing for 2026: Pro, Pro+ and Ultra plans with 50% off first month using referral code GZZUNCYJJTMR.",
        "keywords": "cursor pro pricing, cursor pro cost, how much is cursor pro, cursor pro price 2026, cursor ultra pricing",
        "h1": "Cursor Pro Pricing 2026",
        "intro": "How much does <strong>Cursor Pro</strong> cost? Full pricing for Pro, Pro+, and Ultra — with <strong>50% off your first month</strong> using referral code <code>GZZUNCYJJTMR</code>.",
        "faqs": [
            ("How much is Cursor Pro?", "Approximately $20/mo regular, ~$10/mo first month with referral code GZZUNCYJJTMR."),
            ("Which plan is best for most developers?", "Pro at ~$20/mo (or ~$10/mo first month with referral) suits most individual developers."),
            ("Does the referral discount renew?", "No. 50% off applies to the first month only."),
        ],
        "extra_body": """
  <h2>Plan comparison</h2>
  <table>
    <tr><th>Plan</th><th>Regular</th><th>First month (referral)</th><th>Best for</th></tr>
    <tr><td>Pro</td><td>~$20/mo</td><td>~$10/mo</td><td>Individual developers</td></tr>
    <tr><td>Pro+</td><td>~$60/mo</td><td>~$30/mo</td><td>Power users</td></tr>
    <tr><td>Ultra</td><td>~$200/mo</td><td>~$100/mo</td><td>Heavy professional use</td></tr>
  </table>
  <p class="note">Prices vary by region. Discount applies to first month only for new users.</p>
""",
    },
]


def faq_schema(faqs: list[tuple[str, str]]) -> str:
    entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faqs
    ]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}, indent=2)


def offer_schema() -> str:
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Offer",
            "name": "Cursor Pro 50% Off First Month",
            "description": "50% off first month of Cursor Pro, Pro+ or Ultra for new users",
            "url": REFERRAL_URL,
            "priceCurrency": "USD",
            "eligibleCustomerType": "New customers",
        },
        indent=2,
    )


def nav_links(current: str) -> str:
    links = [
        ("index.html", "Home"),
        ("coupon.html", "Coupon"),
        ("referral.html", "Referral"),
        ("pricing.html", "Pricing"),
    ]
    parts = []
    for href, label in links:
        if href == current:
            parts.append(f"<strong>{label}</strong>")
        else:
            parts.append(f'<a href="{href}">{label}</a>')
    return " | ".join(parts)


def render_page(page: dict) -> str:
    canonical = f"{SITE_BASE}/{page['filename']}"
    faq_json = faq_schema(page["faqs"])
    offer_json = offer_schema()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="{page['description']}">
  <meta name="keywords" content="{page['keywords']}">
  <link rel="canonical" href="{REFERRAL_URL}">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['description']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
{faq_json}
  </script>
  <script type="application/ld+json">
{offer_json}
  </script>
  <style>{STYLES}</style>
</head>
<body>
  <nav>{nav_links(page['filename'])}</nav>
  <h1>{page['h1']}</h1>
  <p>{page['intro']}</p>
  <a class="cta" href="{REFERRAL_URL}">Claim Your 50% Cursor Pro Discount</a>
  <p>Referral code: <code>{CODE}</code></p>
  <p class="note">Verified active <!-- DATE_VERIFIED -->Tuesday, June 16, 2026<!-- /DATE_VERIFIED --> — Offer for <!-- MONTH_YEAR -->June 2026<!-- /MONTH_YEAR --></p>
{page['extra_body']}
  <hr>
  <p><a href="{REPO_URL}">View full guides on GitHub</a></p>
</body>
</html>
"""


def write_sitemap() -> None:
    urls = [f"{SITE_BASE}/{p['filename']}" for p in PAGES]
    entries = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    (DOCS / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n',
        encoding="utf-8",
    )


def write_robots() -> None:
    (DOCS / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_BASE}/sitemap.xml\n",
        encoding="utf-8",
    )


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    for page in PAGES:
        (DOCS / page["filename"]).write_text(render_page(page), encoding="utf-8")
        print(f"Wrote docs/{page['filename']}")
    write_sitemap()
    write_robots()
    print("Wrote docs/sitemap.xml and docs/robots.txt")


if __name__ == "__main__":
    main()
