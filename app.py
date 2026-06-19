import streamlit as st
import os
from downloader import download_playlist
from transcriber import PlaylistTranscriber
from merger import merge_videos

st.set_page_config(page_title="Youtube Plalist Downloader")
st.title("Youtube Playlist Downloader")
playlist_url = st.text_input("Paste Playlist URL")
base_folder = st.text_input("Project Folder",value="Paste Output Folder Location")

merge_video = st.checkbox(
    "Create Combined Video",
    value=False
)
create_transcript = st.checkbox(
    "Create Transcripts",
    value=False
)
if st.button("Start downloading"):
    download_dir = os.path.join(base_folder,"videos")
    transcript_dir = os.path.join(base_folder,"transcripts")
    os.makedirs(download_dir,exist_ok=True)
    os.makedirs(transcript_dir,exist_ok=True)
    st.write("Downloading playlist...")
    download_playlist(playlist_url,download_dir)
    if create_transcript:
        st.write("Generating transcripts...")
        transcriber = PlaylistTranscriber("base")
        transcript_file = (transcriber.transcribe_playlist(download_dir,transcript_dir))

    if merge_video:
        st.write("Merging videos...")
        output_video = os.path.join(base_folder,"combined_course.mp4")
        merge_videos(download_dir,output_video)
    st.success("Process Complete!")

    with open(transcript_file,"r",encoding="utf-8") as f:
        transcript = f.read()
    st.text_area("Transcript Preview",transcript[:5000],height=400)