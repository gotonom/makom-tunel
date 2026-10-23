"""Wraps each page fragment in src/ into a full HTML document in docs/.

docs/ is served by GitHub Pages and by server.js on Railway.
Run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
# source fragment -> (published file, meta description)
PAGES = {
    "index.html":     ("index.html",  "MAKOM kompost ve mantar üretim tesisi otomasyon panelleri. Created by GOTONOM."),
    "bunker.html":    ("bunker.html", "MAKOM Faz 1 bunker otomasyon panosu ve simülasyonu. Created by GOTONOM."),
    "dashboard.html": ("tunel.html",  "MAKOM Faz 2 kompost tüneli otomasyon panosu ve simülasyonu. Created by GOTONOM."),
    "oda.html":       ("oda.html",    "MAKOM mantar üretim odası otomasyon panosu ve simülasyonu. Created by GOTONOM."),
}
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%230a2463'/%3E%3Cpath d='M7 23V9l9 8 9-8v14' "
           "fill='none' stroke='%23fff' stroke-width='3' stroke-linejoin='round'/%3E%3C/svg%3E")

def wrap(src: str, description: str) -> str:
    split = src.index('<div class="wrap">')
    head, body = src[:split].strip(), src[split:].strip()
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{description}">
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

for name, (out, desc) in PAGES.items():
    src = ROOT / "src" / name
    if not src.exists():
        print(f"skip {name} (not found)")
        continue
    page = wrap(src.read_text(encoding="utf-8"), desc)
    (ROOT / "docs" / out).write_text(page, encoding="utf-8")
    print(f"docs/{out} written ({len(page):,} bytes)")
