<div align="center">
  
[![EN](https://img.shields.io/badge/EN-English-blue)](README.md)
[![DE](https://img.shields.io/badge/DE-Deutsch-black)](README.de.md)
[![RU](https://img.shields.io/badge/RU-Русский-orange)](README.ru.md)
[![ZH](https://img.shields.io/badge/ZH-中文-yellow)](README.zh.md)

</div>


### 👨‍💼 1. Agentic RAG Assistant
[![Demo Video](https://img.shields.io/badge/📺-Watch%20Demo-red)](assets/project_1.gif) [![Live App](https://img.shields.io/badge/🤗-Try%20Now-yellow)](https://huggingface.co/spaces/fcyber/agentic_rag)

#### Smart Q&A Assistant with intelligent routing, query refinement, hallucination checking, and self-correction loops.



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
| **Hugging Face** | [![Hugging Face](https://img.shields.io/badge/🤗%20Live%20Demo-FFD21E?style=flat-square)](https://huggingface.co/spaces/fcyber/agentic_rag) | 1 sec | Web browser |


### 📦 Option 1: Python (Local Setup)

1. **Clone the repository**
   ```bash
   git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)
   ```

2. **Navigate to the desired project directory**
   ```bash
   cd ai-engineering-hub/01-agentic-rag-assistant
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
cd ai-engineering-hub/01-agentic-rag-assistant
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
http://localhost:7860
```


7. **Stop the container**
```bash
docker-compose down
```

**That's it!** The project includes a pre-configured `Dockerfile` and `docker-compose.yml` — no additional setup needed.

• • •

### 🤗 Option 3: Hugging Face Spaces

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/fcyber/)

```bash
# No installation needed! Click the badge above to try the live demo.
# Or clone and run locally:
pip install huggingface-hub
huggingface-cli download fcyber/agentic-rag-assistant
python app.py  # Gradio apps run with python
```
