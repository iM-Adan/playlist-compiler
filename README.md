# YouTube Playlist Compiler

This application downloads an entire YouTube playlist, transcribes each video using Whisper AI, optionally merges all videos into a single video.
Note: This project is still needs a lot(I mean alot) of work. Many planned features are listed in the roadmap below.

---

## Features

### Current Features

* Download complete YouTube playlists
* Save videos locally
* Transcribe every video using OpenAI Whisper
* Generate combined playlist transcript
* Merge all playlist videos into a single video
* Streamlit-based user interface

### Planned Features

* AI-generated study notes
* Chapter summaries
* Quiz generation
* PDF notes
* Chatbot (RAG)
* Searchable transcript database

---

## Project Structure

```text
Playlist_compiler/
│
├── app.py
├── downloader.py
├── merger.py
├── transcriber.py
├── utils.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── videos/
├── transcripts/
└── outputs/
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/playlist_compiler.git

cd playlist_compiler
```

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## FFmpeg Installation

FFmpeg is required for:

* Audio extraction
* Video merging
* Media processing

### Windows

```powershell
winget install Gyan.FFmpeg
```

Verify installation:

```powershell
ffmpeg -version
```

Verify:
```bash
ffmpeg -version
```
---

## Running the Application

Start the Streamlit app:

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

---

## How It Works

### Step 1

Paste a YouTube playlist URL.

### Step 2

The application downloads all videos in the playlist.

### Step 3 (Optional)

Each video is transcribed individually using Whisper.

#### Step 3.1 

All transcripts are combined into a master transcript.

### Step 4 (Optional)

Videos are merged into a single course video.

---

## Output Files

Generated files include:

```text
course_output/
│
├── videos/
│   ├── 001_video.mp4
│   ├── 002_video.mp4
│
├── transcripts/
│   ├── 001_video.txt
│   ├── 002_video.txt
│   └── combined_transcript.txt
│
└── combined_course.mp4
Or instead of course_output/ , you can paste path of the folder where you want to download
```

---

## Technologies Used

* Python
* Streamlit
* yt-dlp
* FFmpeg
* OpenAI Whisper
* PyTorch

---

##  Roadmap

* [x] Playlist Download
* [x] Video Transcription
* [x] Video Merging
* [ ] AI Notes Generation
* [ ] PDF Export
* [ ] Course Chatbot (RAG)
* [ ] Docker Deployment

---

## Contributing

Contributions, ideas, and feature requests are welcome.
Feel free to open an issue or submit a pull request.

---
