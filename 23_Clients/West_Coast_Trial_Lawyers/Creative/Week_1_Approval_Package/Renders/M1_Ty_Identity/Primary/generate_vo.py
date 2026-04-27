"""Generate M1 Ty Identity Primary VO — Bill voice, Lead Faucet settings."""
import asyncio
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

# Load FAL_KEY from repo root .env
REPO_ROOT = Path("/Users/davisballard/Documents/claude-creative-work")
env_file = REPO_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

# Load elevenlabs helper module directly (skip the package __init__ which needs imageio_ffmpeg)
import importlib.util
ELEVENLABS_PATH = REPO_ROOT / "Abracadabra" / "04_Production" / "_Ad_Factory" / "audio_models" / "elevenlabs.py"
spec = importlib.util.spec_from_file_location("_el", ELEVENLABS_PATH)
_el = importlib.util.module_from_spec(spec)  # type: ignore
spec.loader.exec_module(_el)  # type: ignore
generate_voiceover = _el.generate_voiceover

OUT_DIR = Path(__file__).parent

# V3_TODAY_BREAK — period-break on "Today" so Bill gives it its own beat instead of swallowing it into "like"
SCRIPT_V2 = (
    "Riders don't ask for sympathy. They ask for what's fair. "
    "A driver didn't see him. The bills don't stop. The presumption doesn't either. "
    "No fee unless we win. Find out what fair looks like. Today."
)

# Lead Faucet production settings
SETTINGS = {
    "voice": "Bill",
    "stability": 0.75,
    "similarity_boost": 0.70,
    "style": 0.15,
    "speed": 1.0,
}


async def main() -> None:
    print(f"Script ({len(SCRIPT_V2.split())} words):\n{SCRIPT_V2}\n")
    url = await generate_voiceover(text=SCRIPT_V2, **SETTINGS)
    raw_path = OUT_DIR / "vo_v3_today_break_bill.mp3"
    padded_path = OUT_DIR / "vo_v3_today_break_bill_padded.mp3"
    urllib.request.urlretrieve(url, raw_path)
    print(f"\nRaw saved: {raw_path}")
    print(f"Source URL: {url}")

    # Auto-pad 1.2s of trailing silence so CapCut / players never clip the last word
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path), "-af", "apad=pad_dur=1.2",
         "-c:a", "libmp3lame", "-q:a", "2", str(padded_path)],
        check=True, capture_output=True,
    )
    print(f"Padded saved (1.2s trailing silence): {padded_path}")


if __name__ == "__main__":
    asyncio.run(main())
