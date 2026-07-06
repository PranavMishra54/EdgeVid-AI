# 🎥 EdgeVid AI

> **Offline Multilingual Video Intelligence System**

EdgeVid AI is an offline AI-powered video summarization system that extracts speech from videos, generates transcripts using Whisper, cleans transcription errors using a Small Language Model (Qwen2.5:1.5B), and produces concise summaries. The entire pipeline runs locally without requiring cloud APIs, making it suitable for edge devices such as NVIDIA Jetson Orin.

---

## 🚀 Features

- 🎥 Upload video files
- 🎵 Automatic audio extraction using FFmpeg
- 🎤 Speech-to-text transcription using Whisper
- ✨ AI-powered transcript cleaning using Qwen2.5:1.5B
- 📋 Hierarchical AI summarization
- 🌍 Supports multilingual speech
- 📥 Download cleaned transcript
- 📥 Download AI-generated summary
- 🔒 Fully offline (No external API required)

---

# 🏗️ System Architecture

```
                Video Upload
                      │
                      ▼
              VideoService
                      │
                      ▼
             Audio Extraction
          (FFmpeg / AudioService)
                      │
                      ▼
            Whisper Transcription
                      │
                      ▼
             Raw Transcript
                      │
                      ▼
          TranscriptService
        (Cleaning using Qwen)
                      │
                      ▼
          Clean Transcript
                      │
                      ▼
             ChunkService
                      │
                      ▼
           SummaryService
                      │
                      ▼
      Hierarchical Summarization
                      │
                      ▼
              Final Summary
```

---

# 📂 Project Structure

```
EdgeVid-AI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── video_service.py
│   ├── audio_service.py
│   ├── whisper_service.py
│   ├── transcript_service.py
│   ├── chunk_service.py
│   ├── summary_service.py
│   └── qwen_service.py
│
├── utils/
│   └── prompts/
│       ├── cleaning.py
│       └── summary.py
│
├── uploads/
├── extracted_audio/
├── transcripts/
│
├── output/
│   ├── cleaned_transcripts/
│   └── summaries/
│
├── static/
│   └── style.css
│
└── assets/
```

---

# ⚙️ Tech Stack

### Programming Language

- Python 3.12

### Frontend

- Streamlit

### Speech Recognition

- OpenAI Whisper

### Large Language Model

- Qwen2.5:1.5B
- Ollama

### Audio Processing

- FFmpeg

### AI Framework

- LangChain

### Deployment Target

- NVIDIA Jetson Orin

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/EdgeVid-AI.git

cd EdgeVid-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install FFmpeg

Download FFmpeg and add it to your system PATH.

Verify

```bash
ffmpeg -version
```

---

## Install Ollama

Download Ollama

https://ollama.com/download

Verify

```bash
ollama --version
```

---

## Download Qwen Model

```bash
ollama pull qwen2.5:1.5b
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🖥️ Workflow

1. Upload a video.
2. Extract audio using FFmpeg.
3. Generate transcript using Whisper.
4. Clean transcript using Qwen2.5:1.5B.
5. Split transcript into chunks.
6. Generate summaries for each chunk.
7. Merge chunk summaries.
8. Generate final AI summary.
9. Download transcript and summary.

---

# 🧠 AI Pipeline

```
Video
   │
   ▼
Audio
   │
   ▼
Whisper
   │
   ▼
Raw Transcript
   │
   ▼
Transcript Cleaning
(Qwen2.5:1.5B)
   │
   ▼
Clean Transcript
   │
   ▼
Chunking
   │
   ▼
Chunk Summaries
   │
   ▼
Final Summary
```

---

# 📸 Screenshots

## Home Screen

(Add screenshot)

---

## Transcript

(Add screenshot)

---

## AI Summary

(Add screenshot)

---

# Future Enhancements

- 💬 Chat with Video
- 📌 Timestamp-based Summary
- 📚 RAG-based Question Answering
- 🧠 Mind Map Generation
- 📝 Meeting Notes
- 📄 PDF Summary Export
- 🌐 Multi-language Summary
- ⚡ Optimized deployment on NVIDIA Jetson Orin

---

# 👨‍💻 Author

**Pranav Mishra**

B.Tech Information Technology

MMMUT Gorakhpur

---

# 📜 License

This project is developed for educational and hackathon purposes.

---

# ⭐ If you found this project useful, consider giving it a Star on GitHub!