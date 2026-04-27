"""Generate S1 Sarah V3 First Offer (Elevated) Primary VO — Bill voice.

V3 = the offer-validation door variant. Hook is the numeric shock:
$18K offer vs $74K hospital bill. Severity-qualified to filter out
soft-tissue cases — "after surgery for broken bones" line filters
the audience to serious-injury commercial trucking trauma only.

Slate consistency: same Bill voice + Sarah-tuned settings as S1 Primary
(stability 0.50, similarity 0.70, style 0.45, speed 1.12 — Davis confirmed
"much, much better" on Sarah Primary). The Sarah register holds across
her variants.
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

# V3 First Offer — severity-qualified to filter out soft-tissue
SCRIPT = (
    "Eighteen thousand dollars. "
    "After surgery for broken bones. "
    "The hospital bill was seventy-four thousand. "
    "The first offer is rarely the fair offer. "
    "Insurance companies count on you taking it. "
    "You don't have to. "
    "Arizona trial attorneys fight insurance every day. "
    "Get your free case review. "
    "No fee unless they win."
)

# Sarah-tuned Bill settings (Davis-confirmed "much, much better" on S1 Primary)
SETTINGS = {
    "voice": "Bill",
    "stability": 0.50,
    "similarity_boost": 0.70,
    "style": 0.45,
    "speed": 1.12,
}


async def main() -> None:
    print(f"Script ({len(SCRIPT.split())} words):\n{SCRIPT}\n")
    url = await generate_voiceover(text=SCRIPT, **SETTINGS)
    raw_path = OUT_DIR / "vo_s1_v3_firstoffer_bill.mp3"
    padded_path = OUT_DIR / "vo_s1_v3_firstoffer_bill_padded.mp3"
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
