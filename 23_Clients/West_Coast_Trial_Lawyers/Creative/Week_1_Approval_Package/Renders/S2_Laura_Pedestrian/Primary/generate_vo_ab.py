"""Roll two parallel Laura VO samples at the same settings.

Davis feedback (2026-04-27): "Its so close but the first 4 seconds are weird,
the last part is great." Settings are right; we just need a fresh roll where
the model lands the first fragment cleanly. Generate two parallel samples
and pick the one with the cleaner opening.
"""
import asyncio
import os
import subprocess
import time
import urllib.request
from pathlib import Path


def download_with_retry(url: str, dest: Path, max_attempts: int = 6) -> None:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    }
    delay = 2
    for attempt in range(1, max_attempts + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as resp:
                dest.write_bytes(resp.read())
            return
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            if attempt == max_attempts:
                raise
            print(f"             [retry {attempt}/{max_attempts}] {e} — sleeping {delay}s")
            time.sleep(delay)
            delay *= 2


REPO_ROOT = Path("/Users/davisballard/Documents/claude-creative-work")
env_file = REPO_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

import importlib.util
ELEVENLABS_PATH = REPO_ROOT / "Abracadabra" / "04_Production" / "_Ad_Factory" / "audio_models" / "elevenlabs.py"
spec = importlib.util.spec_from_file_location("_el", ELEVENLABS_PATH)
_el = importlib.util.module_from_spec(spec)  # type: ignore
spec.loader.exec_module(_el)  # type: ignore
generate_voiceover = _el.generate_voiceover

OUT_DIR = Path(__file__).parent

SCRIPT = (
    "[calm] "
    "Hit while crossing the street? "
    "Find out what the law says about your case. "
    "You weren't the one driving. "
    "They blamed her for crossing. "
    "The law says otherwise. "
    "Free 60-second case review. "
    "No fee unless we win."
)

SETTINGS = {
    "voice": "Bill",
    "stability": 0.65,
    "similarity_boost": 0.75,
    "style": 0.20,
    "speed": 1.05,
}


async def generate_one(name: str) -> Path:
    print(f"\n[{name}] Generating...")
    url = await generate_voiceover(text=SCRIPT, **SETTINGS)
    raw_path = OUT_DIR / f"vo_s2_primary_bill_{name}.mp3"
    padded_path = OUT_DIR / f"vo_s2_primary_bill_{name}_padded.mp3"
    download_with_retry(url, raw_path)
    print(f"[{name}] Raw saved: {raw_path.name}")
    print(f"[{name}] URL: {url}")

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path), "-af", "apad=pad_dur=1.2",
         "-c:a", "libmp3lame", "-q:a", "2", str(padded_path)],
        check=True, capture_output=True,
    )
    print(f"[{name}] Padded saved: {padded_path.name}")
    return padded_path


async def main() -> None:
    print(f"Script ({len(SCRIPT.split())} words):\n{SCRIPT}\n")
    a_task = asyncio.create_task(generate_one("roll1"))
    b_task = asyncio.create_task(generate_one("roll2"))
    await asyncio.gather(a_task, b_task)
    print("\nBoth rolls generated. Compare roll1 vs roll2 — pick the one with the cleaner opening.")


if __name__ == "__main__":
    asyncio.run(main())
