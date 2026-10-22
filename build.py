"""Wraps src/dashboard.html (page body fragment) into a full HTML document at docs/index.html.

docs/ is served by GitHub Pages and by server.js on Railway.
Run: python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "src" / "dashboard.html").read_text(encoding="utf-8")
split = src.index('<div class="wrap">')
head, body = src[:split].strip(), src[split:].strip()

favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%230a2463'/%3E%3Cpath d='M7 23V9l9 8 9-8v14' "
           "fill='none' stroke='%23fff' stroke-width='3' stroke-linejoin='round'/%3E%3C/svg%3E")

page = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="MAKOM Faz 2 kompost tüneli otomasyon panosu ve simülasyonu. Created by GOTONOM.">
<meta name="theme-color" content="#0a2463">
<link rel="icon" href="{favicon}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;-webkit-text-size-adjust:100%}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""
(ROOT / "docs" / "index.html").write_text(page, encoding="utf-8")
print(f"docs/index.html written ({len(page):,} bytes)")
