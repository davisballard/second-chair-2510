"""Generate S5 Diana MVA Primary VO — Bill voice, Sarah-tuned settings.

Script Option A (recorded-statement frame, data-validated 2026-04-25):
the "first offer" hook is mistimed for non-soft-tissue audiences (per IRC,
Martindale-Nolo data — first offer in serious cases doesn't land for 30-90
days, gated by MMI 6-12mo). Diana's audience is in the EARLY weeks: insurance
calling within 24-72hrs for recorded statement, medical authorization
requests weeks 1-3. The script reflects that real moment.

Slate consistency: same Bill voice + same tuned settings as Sarah S1 Primary
(stability 0.50, similarity 0.70, style 0.45, speed 1.12 — Davis confirmed
"much, much better" on Sarah). UGC discipline lives in the visual register;
the VO carries firm authority across the slate.
"""
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

# Option A — recorded-statement frame (data-validated)
# [serious] audio tag at top anchors declarative tone — eleven-v3 supports
# inline emotion tags. Without this, Bill reads "Broken bones. Bills don't
# stop." with rising-question intonation because 2-word fragments lack the
# carrier text the model expects for declarative interpretation.
SCRIPT_OPTION_A = (
    "[serious] "
    "Broken bones. "
    "Bills don't stop. "
    "Insurance is already calling. "
    "They want a recorded statement before you have a lawyer. "
    "You don't have to give one. "
    "Arizona trial attorneys fight insurance every day. "
    "Get your free case review in sixty seconds. "
    "No fee unless they win."
)

# Diana-tuned: maximum dampening on expressive variation to kill the
# questioning swing on short fragments. Style at 0.15 is near-floor;
# stability at 0.65 forces consistent declarative reads.
SETTINGS = {
    "voice": "Bill",
    "stability": 0.65,
    "similarity_boost": 0.75,
    "style": 0.15,
    "speed": 1.08,
}


async def main() -> None:
    print(f"Script ({len(SCRIPT_OPTION_A.split())} words):\n{SCRIPT_OPTION_A}\n")
    url = await generate_voiceover(text=SCRIPT_OPTION_A, **SETTINGS)
    raw_path = OUT_DIR / "vo_s5_primary_bill.mp3"
    padded_path = OUT_DIR / "vo_s5_primary_bill_padded.mp3"
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
