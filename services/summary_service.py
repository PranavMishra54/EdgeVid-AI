from services.chunk_service import ChunkService
from services.qwen_service import QwenService
from config import SUMMARY_DIR

from utils.prompts.summary import (
    SUMMARY_PROMPT,
    FINAL_SUMMARY_PROMPT,
)


class SummaryService:
    """
    Responsible for generating the final summary.

    Workflow:
    1. Split cleaned transcript into chunks.
    2. Generate a summary for each chunk.
    3. Merge all partial summaries.
    4. Generate one final summary from the merged summaries.
    """

    def __init__(
        self,
        chunk_service: ChunkService,
        qwen_service: QwenService,
    ):
        self.chunk_service = chunk_service
        self.qwen = qwen_service

    def summarize(self, cleaned_transcript: str) -> str:

        # Step 1: Split transcript into chunks
        chunks = self.chunk_service.split(cleaned_transcript)

        partial_summaries = []

        # Step 2: Summarize each chunk
        for index, chunk in enumerate(chunks, start=1):

            prompt = SUMMARY_PROMPT.format(
                transcript=chunk
            )

            summary = self.qwen.generate(prompt)

            partial_summaries.append(summary)

        # If there is only one chunk,
        # there is no need to summarize again.
        if len(partial_summaries) == 1:
            return partial_summaries[0]

        # Step 3: Merge partial summaries
        merged_summary = "\n\n".join(partial_summaries)

        # Step 4: Generate one final summary
        final_prompt = FINAL_SUMMARY_PROMPT.format(
            summaries=merged_summary
        )

        final_summary = self.qwen.generate(final_prompt)

        return final_summary
    
    def save(self, summary, audio_path):
        summary_path = SUMMARY_DIR / f"{audio_path.stem}_summary.txt"

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary)

        return summary_path