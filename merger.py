import os
import subprocess
def merge_videos(input_dir,output_file):
    videos = sorted([
        f for f in os.listdir(input_dir)
        if f.endswith((".mp4",".mkv",".webm"))
    ])
    with open("videos.txt","w",encoding="utf-8") as f:
        for video in videos:
            path = os.path.join(input_dir,video).replace("\\", "/")
            f.write(
                f"file '{path}'\n"
            )
    subprocess.run([
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        "videos.txt",
        "-c:v",
        "libx264",
        "-c:a",
        "aac",
        output_file
    ])

    if os.path.exists("videos.txt"):
        os.remove("videos.txt")