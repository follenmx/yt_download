import io
import requests
from yt_dlp import YoutubeDL
import streamlit as st


@st.cache_data(show_spinner=False)
def cum(video_url):
    ydl_opts = {
        "format": "best[ext=mp4][acodec!=none][vcodec!=none]/best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        # Extract video information without downloading
        info_dict = ydl.extract_info(video_url, download=False)
        video_direct_url = info_dict["url"]
        # Get HTTP headers needed for the request
        headers = info_dict.get("http_headers", {})

    # Download the video using requests
    response = requests.get(video_direct_url, headers=headers, stream=True)
    response.raise_for_status()

    video_data = io.BytesIO()
    for chunk in response.iter_content(chunk_size=8192):
        video_data.write(chunk)

    video_data.seek(0)
    return video_data
