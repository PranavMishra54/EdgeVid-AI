import json
import subprocess

from config import UPLOAD_DIR


class VideoService:

    @staticmethod
    def save_video(uploaded_file):

        file_path = UPLOAD_DIR / uploaded_file.name

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path

    @staticmethod
    def get_video_metadata(video_path):
        
        command = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            str(video_path)
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
        except FileNotFoundError as e:
            raise RuntimeError("ffprobe is not installed or is not in PATH.") from e
        except subprocess.CalledProcessError as e:
            message = e.stderr.strip() or e.stdout.strip()
            raise RuntimeError(message or "ffprobe could not read the video.") from e

        return json.loads(result.stdout)
    
    @staticmethod
    def parse_metadata(metadata):
        if not metadata:
            return None

        video_stream = next(
            (
                stream
                for stream in metadata["streams"]
                if stream["codec_type"] == "video"
            ),
            None
        )

        if video_stream is None:
            return None

        return {
            "duration": float(metadata["format"]["duration"]),
            "size": int(metadata["format"]["size"]),
            "width": video_stream["width"],
            "height": video_stream["height"],
            "codec": video_stream["codec_name"],
            "fps": video_stream["r_frame_rate"]
        }
