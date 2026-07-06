import streamlit as st

from services.video_service import VideoService
from services.audio_service import AudioService
from services.whisper_service import WhisperService
from services.transcript_service import TranscriptService
from services.qwen_service import QwenService
from services.chunk_service import ChunkService
from services.summary_service import SummaryService


# Page Configuration

st.set_page_config(
    page_title="EdgeVid AI",
    page_icon="🎥",
    layout="wide",
)

# Cached Services

@st.cache_resource
def get_whisper_service():
    return WhisperService()


@st.cache_resource
def get_qwen_service():
    return QwenService()


@st.cache_resource
def get_transcript_service():
    return TranscriptService(get_qwen_service())


@st.cache_resource
def get_summary_service():
    return SummaryService(
        ChunkService(),
        get_qwen_service()
    )


whisper_service = get_whisper_service()
transcript_service = get_transcript_service()
summary_service = get_summary_service()


# Sidebar

with st.sidebar:

    st.title("🎥 EdgeVid AI")

    st.markdown("---")

    st.markdown("### AI Pipeline")

    st.success("1️⃣ Upload Video")
    st.success("2️⃣ Extract Audio")
    st.success("3️⃣ Whisper Transcription")
    st.success("4️⃣ Transcript Cleaning")
    st.success("5️⃣ AI Summarization")

    st.markdown("---")

    st.info(
        """
        **Models**

        • Whisper

        • Qwen2.5:1.5B

        **Mode**

        Offline
        """
    )


# Header

st.title("🎥 EdgeVid AI")
st.caption("Offline Multilingual Video Intelligence System")

st.divider()

uploaded_video = st.file_uploader(
    "Upload a Video",
    type=["mp4", "avi", "mov", "mkv"]
)


# Main Pipeline

if uploaded_video is not None:

    progress = st.progress(0)
    status = st.empty()

    # Save Video
    
    status.info("📥 Saving video...")
    progress.progress(10)

    file_path = VideoService.save_video(uploaded_video)

    
    # Metadata
    
    status.info("📄 Reading video metadata...")
    progress.progress(20)

    try:
        metadata = VideoService.get_video_metadata(file_path)
        info = VideoService.parse_metadata(metadata)

    except Exception as e:
        st.error(e)
        st.stop()

    
    # Video Information
    
    with st.expander("📹 Video Information", expanded=True):

        col1, col2 = st.columns(2)

        with col1:

            st.metric("Resolution",
                      f"{info['width']} × {info['height']}")

            st.metric("Codec",
                      info["codec"])

            st.metric("FPS",
                      info["fps"])

        with col2:

            st.metric("Duration",
                      f"{info['duration']:.2f} sec")

            st.metric(
                "Size",
                f"{uploaded_video.size/(1024*1024):.2f} MB"
            )

            st.metric(
                "Filename",
                uploaded_video.name
            )

    
    # Audio Extraction
    
    status.info("🎵 Extracting audio...")
    progress.progress(35)

    try:

        audio_path = AudioService.extract_audio(file_path)

    except Exception as e:

        st.error(e)
        st.stop()

    
    # Whisper
    
    status.info("🎤 Transcribing audio...")
    progress.progress(55)

    try:

        result = whisper_service.transcribe(audio_path)

    except Exception as e:

        st.error(e)
        st.stop()

    
    # Transcript Cleaning
    
    status.info("🧹 Cleaning transcript...")
    progress.progress(70)

    try:

        cleaned_transcript = transcript_service.clean(
            result["text"],
            result["language"]
        )

        cleaned_path = transcript_service.save(
            cleaned_transcript,
            audio_path
        )

    except Exception as e:

        st.error(e)
        st.stop()


    # AI Summary
    
    status.info("🤖 Generating summary...")
    progress.progress(90)

    try:

        summary = summary_service.summarize(
            cleaned_transcript
        )

        summary_path = summary_service.save(
            summary,
            audio_path
        )

    except Exception as e:

        st.error(e)
        st.stop()

    progress.progress(100)
    status.success("✅ Processing Complete!")

    st.divider()

    
    # Language
    
    st.success(
        f"Detected Language : {result['language'].upper()}"
    )

    
    # Raw Transcript
    
    with st.expander("📝 Raw Transcript"):

        st.text_area(
            "Raw transcript",
            result["text"],
            height=250,
            key="raw",
            label_visibility="collapsed"
        )

    
    # Clean Transcript
    
    with st.expander(
        "✨ Cleaned Transcript",
        expanded=True
    ):

        st.text_area(
            "Cleaned transcript",
            cleaned_transcript,
            height=250,
            key="clean",
            label_visibility="collapsed"
        )

        st.download_button(
            "⬇ Download Clean Transcript",
            cleaned_transcript,
            file_name=f"{audio_path.stem}_cleaned.txt"
        )

   
    # Summary
    
    with st.expander(
        "📋 AI Summary",
        expanded=True
    ):

        st.text_area(
            "AI summary",
            summary,
            height=250,
            key="summary",
            label_visibility="collapsed"
        )

        st.download_button(
            "⬇ Download Summary",
            summary,
            file_name=f"{audio_path.stem}_summary.txt"
        )
