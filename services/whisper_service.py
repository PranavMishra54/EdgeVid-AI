from pathlib import Path

import whisper

from config import TRANSCRIPT_DIR

class WhisperService:

    def __init__(self):
        self.model = whisper.load_model("tiny")

    def transcribe(self, audio_path: Path):

        result = self.model.transcribe(
            str(audio_path),
            fp16=False,
            task="transcribe"
        )

        return result
    
    def save_transcript(self, result, audio_path):

        transcript_path = TRANSCRIPT_DIR / f"{audio_path.stem}.txt"

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(result["text"])

        return transcript_path

