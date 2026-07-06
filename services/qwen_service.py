import ollama


class QwenService:

    def __init__(self, model_name="qwen2.5:1.5b"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
