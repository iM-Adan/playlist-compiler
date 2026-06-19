import yt_dlp
import os


def download_playlist(url, download_dir):

    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        "outtmpl": os.path.join(
            download_dir,
            "%(playlist_index)s_%(title)s.%(ext)s"
        ),
        "ignoreerrors": True,
        "format": "bestvideo+bestaudio/best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])