<div align="center">
  
[![EN](https://img.shields.io/badge/EN-English-blue)](README.md)
[![DE](https://img.shields.io/badge/DE-Deutsch-black)](README.de.md)
[![RU](https://img.shields.io/badge/RU-Русский-orange)](README.ru.md)
[![ZH](https://img.shields.io/badge/ZH-中文-yellow)](README.zh.md)

</div>


### 🤖 2.  Voice AI Assistant
[![Demo Video](https://img.shields.io/badge/📺-Watch%20Demo-red)](assets/project_2.gif) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fcyber101-voice-ai-assistant.streamlit.app/)

#### Voice AI Assistant featuring real-time speech recognition, ultra-fast Groq inference, natural voice synthesis, and downloadable audio responses.



<div align="center">

![Status](https://img.shields.io/badge/Status-Active-success)
![Groq](https://img.shields.io/badge/Groq-%E2%9C%93-purple)
![Whisper](https://img.shields.io/badge/Whisper-%E2%9C%93-blue)
![gTTS](https://img.shields.io/badge/gTTS-%E2%9C%93-green)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%93-red)
![Multi-language](https://img.shields.io/badge/Multi--language-%E2%9C%93-orange)

</div>

| Feature | Description |
| :--- | :--- |
| **🎤 Voice Input Processing** | Leverages **Groq API** for fast LLM inference and **Whisper** for accurate speech-to-text transcription. |
| **🔊 Voice Output Generation** | Converts text responses to natural speech using **gTTS** (Google Text-to-Speech) with download capability. |
| **💬 Conversation History** | Maintains chat history for contextual conversations and easy reference to previous interactions. |
| **⬇️ Audio Download** | Allows users to download AI responses as audio files for offline listening and sharing. |
| **🌐 Language Selection** | Supports multiple languages for both input recognition and output generation. |
| **🤖 Model Selection** | Choose between different AI models to balance speed, quality, and cost. |
| **⚡ Groq Acceleration** | Ultra-fast inference powered by Groq's LPU (Language Processing Unit) technology. |

---

<div align="center">

![Agentischer RAG-Workflow](assets/workflow.gif)

</div>

---


## 🚀 Getting Started
### 🎯 Quick Start Comparison (Updated)

| Method | Command | Time | Requires |
|--------|---------|------|----------|
| **Python** | `pip install -r requirements.txt && python app.py` | 2-5 min | Python 3.9+ |
| **Docker** | `docker-compose up -d` | 30 sec | Docker + Compose |
| **Streamlit** | [![Live App](https://img.shields.io/badge/🚀-Live%20Demo-blue)](https://fcyber101-voice-ai-assistant.streamlit.app/) | 1 sec | Web browser |


### 📦 Option 1: Python (Local Setup)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)
   ```

2. **Navigate to the desired project directory**
   ```bash
   cd ai-engineering-hub/02-voice-ai-assistant
   ```

3. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

#### Follow the project-specific instructions in each project's `README.md` file to set up and run the app.
• • •

### 🐳 Option 2: Docker Compose (Recommended)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/fcyber/agentic-rag-assistant)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)

1. **Clone the repository**
```bash
git clone https://github.com/fcyber/ai-engineering-hub.git
```

2. **Navigate to the desired project directory**
```bash
cd ai-engineering-hub/02-voice-ai-assistant
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your GROQ_API_KEY keys
```

4. **Run with Docker Compose**
```bash
docker-compose up -d
```

5. **View logs (optional)**
```bash
docker-compose logs -f
```

6. **Open in browser**
```bash
http://localhost:8501
```


7. **Stop the container**
```bash
docker-compose down
```

**That's it!** The project includes a pre-configured `Dockerfile` and `docker-compose.yml` — no additional setup needed.

• • •

### 👑 Option 3: Streamlit Community Cloud

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fcyber101-voice-ai-assistant.streamlit.app/)

```bash
# No installation needed! Click the badge above to try the live demo.
# Or run locally:
pip install -r requirements.txt
streamlit run app.py
```
