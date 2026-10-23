"""Wraps each page fragment in src/ into a full HTML document in docs/.

docs/ is served by GitHub Pages and by server.js on Railway.
Run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
# Share links resolve against the Railway domain (GitHub Pages copies point there too).
BASE = "https://makom-tunel-production.up.railway.app"
# source fragment -> (published file, share title, meta description, share card in docs/og/)
PAGES = {
    "index.html":     ("index.html",  "MAKOM Kontrol Merkezi",
                       "3 bunker, 4 tünel ve 20 üretim odası tek ekranda: canlı saha planı, üretim takvimi, enerji ve alarmlar. Created by GOTONOM.", "index"),
    "bunker.html":    ("bunker.html", "MAKOM · Faz 1 Bunker Otomasyonu",
                       "Fan 5 dk çalışır, 25 dk durur; gerekirse 6–7 dk'ya uzar, 7 dk PLC sınırıdır. 8 prob, °C/saat değişim hızı. Created by GOTONOM.", "bunker"),
    "dashboard.html": ("tunel.html",  "MAKOM · Faz 2 Tünel Otomasyonu",
                       "Pastörizasyon ve kondisyonlama: 7 etaplı tarif, otomatik geçiş, manuel müdahale ve alarm senaryoları. Created by GOTONOM.", "tunel"),
    "oda.html":       ("oda.html",    "MAKOM · Üretim Odaları",
                       "20 odanın iklim kontrolü: sıcaklık, nem, CO₂ ve taze hava, 52 günlük döngü boyunca. Created by GOTONOM.", "oda"),
}
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%230a2463'/%3E%3Cpath d='M7 23V9l9 8 9-8v14' "
           "fill='none' stroke='%23fff' stroke-width='3' stroke-linejoin='round'/%3E%3C/svg%3E")

def wrap(src: str, out: str, title: str, description: str, card: str) -> str:
    split = src.index('<div class="wrap">')
    head, body = src[:split].strip(), src[split:].strip()
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MAKOM">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{BASE}/{'' if out == 'index.html' else out}">
<meta property="og:image" content="{BASE}/og/{card}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{BASE}/og/{card}.png">
<meta name="theme-color" content="#0a2463">
<link rel="icon" href="{FAVICON}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;-webkit-text-size-adjust:100%}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""

for name, (out, title, desc, card) in PAGES.items():
    src = ROOT / "src" / name
    if not src.exists():
        print(f"skip {name} (not found)")
        continue
    page = wrap(src.read_text(encoding="utf-8"), out, title, desc, card)
    (ROOT / "docs" / out).write_text(page, encoding="utf-8")
    print(f"docs/{out} written ({len(page):,} bytes)")
