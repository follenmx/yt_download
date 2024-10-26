import streamlit as st
from fat.cock import cum

st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")

st.title("🎥 YouTube Video Downloader and Viewer")
st.markdown(
    "**Disclaimer:** Please ensure that you have the right to download and use the content. Respect the [YouTube Terms of Service](https://www.youtube.com/static?template=terms)."
)

with st.sidebar:
    st.header("Instructions")
    st.write(
        """
    1. Enter a valid YouTube video URL.
    2. Choose your preferred video quality.
    3. Click on 'Download and Display Video'.
    """
    )
    st.write("**Note:** Please respect YouTube's Terms of Service.")

data = st.text_input("Please input")
if data:
    src = cum(data)
    st.video(src)
