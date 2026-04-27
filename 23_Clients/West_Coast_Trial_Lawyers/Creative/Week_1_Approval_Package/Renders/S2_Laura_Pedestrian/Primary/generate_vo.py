"""Generate S2 Laura Pedestrian Primary VO — Bill voice, Laura-tuned settings.

S2 Laura Primary is a 15s video upgrade from the original static-only spec.
The architecture (per ok-so-i-need-memoized-cook.md plan) is:
    Hook (0-3s) → Early CTA (3-5s) → Barrier breakdown (5-11s) → Diegetic quiz (11-15s)

Laura-tuned register vs Sarah and Diana:
- Sarah (S1 V3): stability 0.50, style 0.45, speed 1.12 — punchy commercial-trucking energy
- Diana (S5 Primary): stability 0.65, style 0.15, speed 1.08 — UGC-flat declarative
- Laura (S2 Primary): stability 0.65, style 0.20, speed 1.05 — calmer librarian pace,
  no combat energy, accountability framing

Persona discipline (from Audience/Deep_Personas/Laura/):
- NO combat language ("fight," "aggressive," "make them pay") — kills Laura
- Words that work: "find out what the law says," "accountability," "documented facts"
- PTA-Treasurer cognition — slower pace lands; rushed delivery patronizes

[calm] inline audio tag at the top anchors declarative tone (same pattern as
Diana's [serious] tag) — kills questioning intonation on short fragments.
"""
import asyncio
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path


def download_with_retry(url: str, dest: Path, max_attempts: int = 6) -> None:
    """Download with exponential backoff to handle fal CDN 503s."""
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

# Laura Primary — accountability framing, situation filter + blame-shift inflection
# Total VO read target: ~10s (with [calm] tag and Laura-tuned settings)
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

# Laura-tuned Bill settings — calmer than Sarah, gentler register than Diana
SETTINGS = {
    "voice": "Bill",
    "stability": 0.65,        # higher than Sarah (0.50) → calmer, less swing
    "similarity_boost": 0.75,
    "style": 0.20,            # lower than Sarah (0.45) → less dramatic flair
    "speed": 1.05,            # slower than Sarah (1.12) → librarian pace
}


async def main() -> None:
    print(f"Script ({len(SCRIPT.split())} words):\n{SCRIPT}\n")
    url = await generate_voiceover(text=SCRIPT, **SETTINGS)
    raw_path = OUT_DIR / "vo_s2_primary_bill.mp3"
    padded_path = OUT_DIR / "vo_s2_primary_bill_padded.mp3"
    print(f"\nFull URL: {url}")
    download_with_retry(url, raw_path)
    print(f"Raw saved: {raw_path}")

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(raw_path), "-af", "apad=pad_dur=1.2",
         "-c:a", "libmp3lame", "-q:a", "2", str(padded_path)],
        check=True, capture_output=True,
    )
    print(f"Padded saved (1.2s trailing silence): {padded_path}")


if __name__ == "__main__":
    asyncio.run(main())
