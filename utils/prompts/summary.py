SUMMARY_PROMPT = """
You are an expert AI assistant.

Your task is to summarize the following transcript chunk.

Rules:

1. Keep only important information.
2. Remove repetition.
3. Preserve technical terms.
4. Keep the original meaning.
5. Use simple English.
6. Use bullet points.
7. Do NOT add information that is not present.

Transcript:

{transcript}
"""


FINAL_SUMMARY_PROMPT = """
You are an expert AI assistant.

Below are summaries from different parts of a long video.

Combine them into ONE coherent summary.

Rules:

1. Remove duplicate points.
2. Preserve important information.
3. Arrange logically.
4. Use headings and bullet points.
5. Keep it concise.
6. Do NOT invent information.

Partial Summaries:

{summaries}
"""