"""Generate M3 Ty Injustice V4 Video Primary VO — Bill voice, M1 settings.

V4 is a NET-ADD video Primary on top of M3's static V1/V2/V3. Architecture
mirrors Laura S2 Pedestrian Primary: Hook (situation filter) → Early CTA →
Barrier breakdown (presumption-of-fault wound) → Diegetic phone CTA → Close.

Persona discipline (from Audience/Deep_Personas/Ty/):
- NO sympathy framing — "Riders don't ask for sympathy"
- NO combat language — accountability + factual record register
- Wound: presumption of fault ("they said the rider was reckless")
- ER-nurse-asked-were-you-speeding-before-how-much-pain shadow

[serious] inline audio tag at the top anchors Ty's factual register (same
pattern as Diana, NOT Laura's [calm]).

Generates 3 parallel rolls at the same Ty M1-proven settings — pick the
cleanest one against the visuals.
"""
import asyncio
import os
import subprocess
import time
import urllib.error
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

# M3-V4 Ty — Laura-formula applied to motorcycle injustice frame
SCRIPT = (
    "[serious] "
    "Hit while riding? "
    "Find out what the law says about your case. "
    "You were doing the speed limit. "
    "They said the rider was reckless. "
    "The law reads the record. "
    "Free 60-second case review. "
    "No fee unless we win."
)

# Ty M1-proven Bill settings (locked from M1 Primary final)
SETTINGS = {
    "voice": "Bill",
    "stability": 0.75,
    "similarity_boost": 0.70,
    "style": 0.15,
    "speed": 1.0,
}


async def generate_one(name: str) -> Path:
    print(f"\n[{name}] Generating...")
    url = await generate_voiceover(text=SCRIPT, **SETTINGS)
    raw_path = OUT_DIR / f"vo_m3v4_bill_{name}.mp3"
    padded_path = OUT_DIR / f"vo_m3v4_bill_{name}_padded.mp3"
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
    tasks = [
        asyncio.create_task(generate_one("roll1")),
        asyncio.create_task(generate_one("roll2")),
        asyncio.create_task(generate_one("roll3")),
    ]
    await asyncio.gather(*tasks)
    print("\nAll 3 rolls generated. Pick the cleanest delivery — same settings, different sample.")


if __name__ == "__main__":
    asyncio.run(main())
