"""Renders the share cards in og/og.html to docs/og/<page>.png (1200 × 630) with headless Chrome.
Run: python3 og/render.py
"""
import subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = ROOT / "docs" / "og"
OUT.mkdir(parents=True, exist_ok=True)

for page in ["index", "bunker", "tunel", "oda"]:
    with tempfile.TemporaryDirectory() as profile:   # own profile, so a running Chrome is not disturbed
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--user-data-dir={profile}", "--window-size=1200,630", "--virtual-time-budget=8000",
                        f"--screenshot={OUT / (page + '.png')}", f"file://{ROOT / 'og' / 'og.html'}#{page}"],
                       check=True, capture_output=True)
    print(f"docs/og/{page}.png")
