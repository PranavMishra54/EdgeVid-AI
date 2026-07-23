from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "uploads"
AUDIO_DIR = BASE_DIR / "extracted_audio"
TRANSCRIPT_DIR = BASE_DIR / "transcripts"
SUMMARY_DIR = BASE_DIR / "summaries"

# Create folders automatically
for folder in [
    UPLOAD_DIR,
    AUDIO_DIR,
    TRANSCRIPT_DIR,
    SUMMARY_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)
