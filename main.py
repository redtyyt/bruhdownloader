import os
import yt_dlp
from tkinter import filedialog

def down_yt(url: str, fmt: str = "mp3"):
    # output folder
    dpath = os.path.join(os.getcwd(), "downloads")
    os.makedirs(dpath, exist_ok=True)

    fmt = fmt.lower()
    # download opts
    if fmt == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(dpath, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    elif fmt == "mp4":
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(dpath, "%(title)s.%(ext)s"),
            # ensure final container is mp4 when merging audio/video
            "merge_output_format": "mp4",
        }
    else:
        raise ValueError("Invalid format. Please use 'mp3' or 'mp4'.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except KeyboardInterrupt:
        confirm = input("[!] Interrupted. Type 'yes' to exit or press ENTER to continue: ").strip().lower()
        if confirm == "yes":
            raise SystemExit(1)
        print("Resuming...")

if __name__ == "__main__":
    lnk = input("Link >> ").strip()
    fmt = input("Choose between mp3 or mp4 format >> ").strip().lower()
    if fmt not in ("mp3", "mp4"):
        print("Invalid format. Defaulting to mp4.")
        fmt = "mp4"
    down_yt(lnk, fmt)