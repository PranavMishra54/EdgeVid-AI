import subprocess
from pathlib import Path

from config import AUDIO_DIR


class AudioService:

    @staticmethod
    def extract_audio(video_path: Path):

        audio_path = AUDIO_DIR / f"{video_path.stem}.wav"

        command = [
            "ffmpeg",
            "-y",
            "-i", str(video_path),
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            str(audio_path)
        ]

        try:
            subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
        except FileNotFoundError as e:
            raise RuntimeError("ffmpeg is not installed or is not in PATH.") from e
        except subprocess.CalledProcessError as e:
            message = e.stderr.strip() or e.stdout.strip()
            raise RuntimeError(message or "ffmpeg could not extract audio.") from e

        return audio_path
