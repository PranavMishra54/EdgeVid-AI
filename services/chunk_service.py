from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:

    def __init__(
        self,
        chunk_size=2000,
        chunk_overlap=200
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(self, transcript: str):

        if len(transcript) <= self.splitter._chunk_size:
            return [transcript]

        return self.splitter.split_text(transcript)