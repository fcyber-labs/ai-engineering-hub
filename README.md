# 🌟 AI Engineering Hub

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](your-linkedin-link)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Profile-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/fcyber)

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-1C3C3C?logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20-7C3AED)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-CC5A4A?logo=anthropic&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

<h3>A curated collection of production-ready LLM applications built with RAG, AI Agents, Agentic Systems, MCP, and more</h3>

<p>
This repository features LLM apps that use models from <strong>OpenAI</strong>, <strong>Anthropic</strong>, <strong>Google</strong>, <strong>xAI</strong> and open-source models like <strong>Qwen</strong> or <strong>Llama</strong> that you can run locally on your computer.
</p>

<div align="right">
  
[![EN](https://img.shields.io/badge/EN-English-blue)](README.md)
[![ES](https://img.shields.io/badge/ES-Español-red)](README.es.md)
[![FR](https://img.shields.io/badge/FR-Français-blue)](README.fr.md)
[![DE](https://img.shields.io/badge/DE-Deutsch-black)](README.de.md)
[![JA](https://img.shields.io/badge/JA-日本語-red)](README.ja.md)
[![KO](https://img.shields.io/badge/KO-한국어-blue)](README.ko.md)
[![PT](https://img.shields.io/badge/PT-Português-green)](README.pt.md)
[![RU](https://img.shields.io/badge/RU-Русский-orange)](README.ru.md)
[![ZH](https://img.shields.io/badge/ZH-中文-yellow)](README.zh.md)

</div>

[📂 Featured AI Projects](#-featured-ai-projects) •
[🚀 Getting Started](#-getting-started) •
[🤔 Why AI Engineering Hub?](#-why-ai-engineering-hub) •
[🤝 Contributing](#-contributing) •
[🙏 Thank You](#-thank-you)


</div>

---

## 🤔 Why AI Engineering Hub?

| 💡 Discover | 🔥 Explore | 🎓 Learn |
| :--- | :--- | :--- |
| Discover practical and creative ways LLMs can be applied across different domains, from document analysis to intelligent agents. | Explore apps that combine LLMs with AI Agents, Agent Teams, MCP, and Agentic RAG. | Learn from well-documented projects and contribute to the growing open-source ecosystem. |

---

## 📂 Featured AI Projects



### [1. 👨‍💼 Agentic RAG Assistant: **Smart Q&A Assistant with intelligent routing, query refinement, hallucination checking, and self-correction loops.**](./01-agentic-rag-assistant)

### 👉 [**🤗 Test it**](https://huggingface.co/spaces/fcyber/agentic_rag)
<div align="center">

![Status](https://img.shields.io/badge/Status-Active-success)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red)
![LangGraph](https://img.shields.io/badge/LangGraph-%E2%9C%93-purple)
![Hybrid Search](https://img.shields.io/badge/Hybrid_Search-%E2%9C%93-blue)
![Self Correction](https://img.shields.io/badge/Self_Correction-%E2%9C%93-orange)

</div>

| Feature | Description |
| :--- | :--- |
| **🔀 Intelligent Routing** | Dynamically routes queries to specialized agents based on intent analysis. |
| **🔍 Query Refinement** | Self-improves queries through reflection and rewriting. |
| **✅ Hallucination Checking** | Validates responses against source documents with faithfulness scoring. |
| **🔄 Self-Correction** | Automatically detects and fixes inadequate responses. |
| **📊 Hybrid Retrieval** | Combines semantic, keyword, and knowledge graph search. |



---

### 🚧 More Projects Coming Soon

<details><summary><b>🔮 Planned Projects (Click to Expand)</b></summary>

| Project | Description | Status |
| :--- | :--- | :--- |
| 🗣️ **Voice RAG Agent** | Voice-enabled Q&A with real-time transcription | `Planned` |
| 🌐 **MCP Browser Agent** | Browser automation with Model Context Protocol | `Planned` |
| 🤝 **Multi-Agent Research** | Collaborative research agents with handoffs | `Planned` |
| 📄 **Chat with PDF** | Document Q&A with hybrid search | `Planned` |
| 💬 **Stateful Memory** | Conversational AI with persistent memory | `Planned` |

</details>

---

## 🚀 Getting Started
### 📦 Option 1: Python (Local Setup)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)


2. **Navigate to the desired project directory**
   ```bash
   cd ai-engineering-hub/01-agentic-rag-assistant
   ```

3. **Install the required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

#### Follow the project-specific instructions in each project's `README.md` file to set up and run the app.
---

### 🐳 Option 2: Docker Compose (Recommended)


1. **Clone the repository**
   ```bash
   git clone https://github.com/fcyber/ai-engineering-hub.git
   ```
2. **Navigate to the desired project directory**
   ```bash
   cd ai-engineering-hub/01-agentic-rag-assistant
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```
4. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```
6. **View logs (optional)**
   ```bash
   docker-compose logs -f
   ```
7. **Stop the container**
   ```bash
   docker-compose down
   ```

**That's it!** The project includes a pre-configured `Dockerfile` and `docker-compose.yml` — no additional setup needed.

---

### 🤗 Option 3: Hugging Face Spaces

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/spaces/fcyber/agentic_rag)

```bash
# No installation needed! Click the badge above to try the live demo.
# Or clone and run locally:
pip install huggingface-hub
huggingface-cli download fcyber/agentic-rag-assistant
python app.py  # Gradio apps run with python
```
---

## 🎯 Quick Start Comparison (Updated)

| Method | Command | Time | Requires |
|--------|---------|------|----------|
| **Python** | `pip install -r requirements.txt && python app.py` | 2-5 min | Python 3.9+ |
| **Docker** | `docker-compose up -d` | 30 sec | Docker + Compose |
| **Hugging Face** | Click link | 1 sec | Web browser |

---

## 🛠️ Technology Stack
| Category | Technologies |
| --- | --- |
| LLM Frameworks | LangChain, LangGraph, LlamaIndex |
| Models | GPT-4, Claude 3.5, Sonnet, Gemini 1.5 Pro, Llama 3.1, Qwen 2.5 |
| Vector Databases | Pinecone, Chroma, Weaviate, Qdrant |
| Embeddings | OpenAI, Cohere, HuggingFace, Voyage |
| Frontend | Streamlit, Gradio, Chainlit |
| Monitoring | LangSmith, Arize Phoenix, Weights & Biases |
| Deployment | Streamlit Cloud, Hugging Face Spaces, Docker, AWS |

---

## 🤝 Contributing
We welcome contributions! Please follow these steps:
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-project`)
- Commit your changes (`git commit -m 'Add amazing project'`)
- Push to the branch (`git push origin feature/amazing-project`)
- Open a Pull Request

### ✅ Contribution Checklist
- Self-contained project directory
- Comprehensive README with setup instructions
-Working demo with clear setup steps
-.env.example with all required variables
-requirements.txt with pinned versions
-Screenshots demonstrating functionality 

## 🙏 Thank You, Community, for the Support!

<center>
⭐ Star this repository if you find it useful! ⭐

<br> <br>

 
---
 
## 📊 Repository Stats

<div align="center">

| ⭐ **Stars** | 🍴 **Forks** | 👀 **Watchers** |
|:-----------:|:-----------:|:--------------:|
| [![GitHub Stars](https://img.shields.io/github/stars/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=ffd700)](https://github.com/fcyber101/ai-engineering-hub/stargazers) | [![GitHub Forks](https://img.shields.io/github/forks/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=58a6ff)](https://github.com/fcyber101/ai-engineering-hub/network/members) | [![GitHub Watchers](https://img.shields.io/github/watchers/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=2ea44f)](https://github.com/fcyber101/ai-engineering-hub/watchers) |

| 🐛 **Issues** | 🔀 **PRs** | 📦 **Releases** |
|:------------:|:----------:|:---------------:|
| [![GitHub Issues](https://img.shields.io/github/issues/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=f85149)](https://github.com/fcyber101/ai-engineering-hub/issues) | [![GitHub PRs](https://img.shields.io/github/issues-pr/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=f0883e)](https://github.com/fcyber101/ai-engineering-hub/pulls) | [![GitHub Release](https://img.shields.io/github/v/release/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=a371f7)](https://github.com/fcyber101/ai-engineering-hub/releases) |

| 👥 **Contributors** | 📅 **Last Commit** | 📝 **License** |
|:------------------:|:------------------:|:--------------:|
| [![GitHub Contributors](https://img.shields.io/github/contributors/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/graphs/contributors) | [![GitHub Last Commit](https://img.shields.io/github/last-commit/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/commits/main) | [![GitHub License](https://img.shields.io/github/license/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/blob/main/LICENSE) |

</div>

---

<sub>Built with ❤️ by AI Engineers for AI Engineers</sub>

</center>
