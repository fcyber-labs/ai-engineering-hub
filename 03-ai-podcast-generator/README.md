### 🎧 3.  AI News Podcast Generator - AI DAILY DIGEST
[![Demo Video](https://img.shields.io/badge/📺-Watch%20Demo-red)](assets/project3_demo.gif) [![Live App](https://img.shields.io/badge/🤗-Try%20Now-yellow)](https://huggingface.co/spaces/fcyber/ai-podcast)

#### AI Podcast Generator transforms top AI news headlines into fully-produced podcast episodes automatically. Simply enter URLs of AI news sources, and the app scrapes, summarizes, and converts the content into a professional podcast script with downloadable MP3 audio.



<div align="center">

![Status](https://img.shields.io/badge/Status-Active-success)
![Groq](https://img.shields.io/badge/Groq-%E2%9C%93-purple)
![LangGraph](https://img.shields.io/badge/LangGraph-%E2%9C%93-blue)
![gTTS](https://img.shields.io/badge/gTTS-%E2%9C%93-green)
![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%93-red)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-%E2%9C%93-orange)

</div>

| Feature | Description |
| :--- | :--- |
| **🕸️ AI News Scraping** | Automatically scrapes and extracts headlines from top AI news sources using advanced web scraping techniques with Cloudscraper. |
| **🏆 Smart Headline Rating** | Uses **Groq API** to intelligently rate and rank AI news headlines on a 0-100 scale based on relevance and importance. |
| **📝 AI-Powered Summarization** | Generates concise, high-quality 150-200 word summaries of articles using LLM technology for podcast-ready content. |
| **🎙️ Podcast Script Generation** | Creates professional podcast scripts with engaging intros, natural transitions between stories, and compelling outros. |
| **🔊 Text-to-Speech Conversion** | Converts podcast scripts to natural-sounding audio using **gTTS** with downloadable MP3 files for offline listening. |
| **🔄 LangGraph Workflow** | Orchestrates the entire multi-step process through a structured LangGraph pipeline for reliability and modularity. |
| **📊 Top-10 Article Selection** | Automatically selects and prioritizes the most relevant AI news articles based on intelligent scoring algorithms. |
| **💾 File Export Options** | Download both the podcast script (.txt) and generated audio (.mp3) for sharing and archiving. |
| **⚡ Groq Acceleration** | Ultra-fast LLM inference powered by Groq's LPU technology for real-time processing and summarization. |
| **📝 BART Large CNN** | Facebook's BART Large CNN model generates high-quality, abstractive summaries by understanding context and rephrasing content naturally, perfect for condensing long-form content into digestible podcast scripts. |

---

<div align="center">

![Agentischer RAG-Workflow](assets/workflow.gif)

</div>

---


## 🚀 Getting Started
### 🎯 Quick Start Comparison

| Method | Command | Time | Requires |
|--------|---------|------|----------|
| **Python** | `pip install -r requirements.txt && streamlit run streamlit_app.py` | 2-5 min | Python 3.9+ |
| **Docker** | `docker-compose up -d` | 30 sec | Docker + Compose |
| **Hugging Face** | [![Hugging Face](https://img.shields.io/badge/🤗%20Live%20Demo-FFD21E?style=flat-square)](https://huggingface.co/spaces/fcyber/ai-podcast) | 1 sec | Web browser |


### 📦 Option 1: Python (Local Setup)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)
   ```

2. **Navigate to the desired project directory**
   ```bash
   cd ai-engineering-hub/03-ai-podcast-generator
   ```

3. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run streamlit apps**
   ```bash
   streamlit run streamlit_app.py
   ```

#### Follow the project-specific instructions in each project's `README.md` file to set up and run the app.
• • •

### 🐳 Option 2: Docker Compose (Recommended)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/fcyber/)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)

1. **Clone the repository**
```bash
git clone https://github.com/fcyber/ai-engineering-hub.git
```

2. **Navigate to the desired project directory**
```bash
cd ai-engineering-hub/03-ai-podcast-generator
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

### 🤗 Option 3: Hugging Face Spaces

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/fcyber/ai-podcast)

```bash
# No installation needed! Click the badge above to try the live demo.
# Or clone and run locally:
pip install huggingface-hub
huggingface-cli download fcyber/ai-podcast
python streamlit run streamlit_app.py  # Gradio apps run with python
```
