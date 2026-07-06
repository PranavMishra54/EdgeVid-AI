from config import TRANSCRIPT_DIR
from utils.prompts.cleaning import TRANSCRIPT_CLEANING_PROMPT
from services.qwen_service import QwenService


class TranscriptService:

    def __init__(self, qwen_service: QwenService):
        self.qwen = qwen_service

    def clean(self, raw_transcript, language):
        prompt = TRANSCRIPT_CLEANING_PROMPT.format(
            transcript=raw_transcript,
            language=language
        )

        cleaned_transcript = self.qwen.generate(prompt)
        return cleaned_transcript

    def save(self, cleaned_text, audio_path):
        cleaned_path = TRANSCRIPT_DIR / f"{audio_path.stem}_cleaned.txt"

        with open(cleaned_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)

        return cleaned_path