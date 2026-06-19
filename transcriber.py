import os
import whisper
import subprocess
from pathlib import Path


class PlaylistTranscriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)
    def extract_audio(self, video_path, audio_path):
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                video_path,
                "-vn",
                "-ar",
                "16000",
                "-ac",
                "1",
                audio_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def transcribe_video(self, video_path, transcript_dir):
        name = Path(video_path).stem
        audio_path = os.path.join(
            transcript_dir,
            f"{name}.wav"
        )
        self.extract_audio(
            video_path,
            audio_path
        )
        result = self.model.transcribe(
            audio_path
        )
        txt_path = os.path.join(
            transcript_dir,
            f"{name}.txt"
        )
        with open(
            txt_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(result["text"])

        if os.path.exists(audio_path):
            os.remove(audio_path)
        return result["text"]

    def transcribe_playlist(
        self,
        download_dir,
        transcript_dir
    ):

        os.makedirs(
            transcript_dir,
            exist_ok=True
        )

        combined = []
        videos = sorted([
            f for f in os.listdir(download_dir)
            if f.endswith(
                (
                    ".mp4",
                    ".mkv",
                    ".webm"
                )
            )
        ])

        for video in videos:
            video_path = os.path.join(
                download_dir,
                video
            )
            text = self.transcribe_video(
                video_path,
                transcript_dir
            )
            combined.append(
                f"\n\n===== {video} =====\n\n"
            )
            combined.append(text)
        combined_path = os.path.join(
            transcript_dir,
            "combined_transcript.txt"
        )
        with open(
            combined_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write("".join(combined))
        return combined_path