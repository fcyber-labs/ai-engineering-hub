# 🌟 AI Engineering Hub
![Agentic RAG Assistant Demo](01-agentic-rag-assistant/media/gif_3.gif)

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](your-linkedin-link)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Profile-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/fcyber)

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-1C3C3C?logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-0.0.20-7C3AED)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-CC5A4A?logo=anthropic&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B?logo=streamlit&logoColor=white)
![许可证](https://img.shields.io/badge/许可证-MIT-yellow)
![贡献](https://img.shields.io/badge/贡献-欢迎-brightgreen)

<h3>精选的生产就绪型LLM应用集合，基于RAG、AI智能体、代理系统、MCP等构建</h3>

<p>
本代码库包含使用<strong>OpenAI</strong>、<strong>Anthropic</strong>、<strong>Google</strong>、<strong>xAI</strong>模型以及<strong>Qwen</strong>或<strong>Llama</strong>等开源模型的LLM应用，您可以在本地计算机上运行这些应用。
</p>

<div align="center">
  
[![EN](https://img.shields.io/badge/EN-English-blue)](README.md)
[![DE](https://img.shields.io/badge/DE-Deutsch-black)](README.de.md)
[![RU](https://img.shields.io/badge/RU-Русский-orange)](README.ru.md)
[![ZH](https://img.shields.io/badge/ZH-中文-yellow)](README.zh.md)

</div>

[📂 精选AI项目](#-精选ai项目) •
[🚀 快速开始](#-快速开始) •
[🤔 为什么选择AI Engineering Hub？](#-为什么选择ai-engineering-hub) •
[🤝 参与贡献](#-参与贡献) •
[🙏 感谢](#-感谢社区支持)

</div>

---

## 🤔 为什么选择AI Engineering Hub？

| 💡 发现 | 🔥 探索 | 🎓 学习 |
| :--- | :--- | :--- |
| 发现LLM在不同领域（从文档分析到智能代理）的实用和创造性应用方式。 | 探索将LLM与AI智能体、智能体团队、MCP和代理型RAG相结合的应用。 | 从文档完善的项目中学习，并为不断增长的开源生态系统做出贡献。 |

---

## 📂 精选AI项目

### 👨‍💼 [1. 代理型RAG助手](./01-agentic-rag-assistant)   
[![Demo Video](https://img.shields.io/badge/📺-Watch%20Demo-red)](01-agentic-rag-assistant/media/project_1.gif) [![Live App](https://img.shields.io/badge/🤗-Try%20Now-yellow)](https://huggingface.co/spaces/fcyber/agentic_rag)

#### 智能问答助手，具备智能路由、查询优化、幻觉检测和自我修正循环功能。

<div align="center">

![状态](https://img.shields.io/badge/状态-活跃中-success)
![难度](https://img.shields.io/badge/难度-高级-red)
![LangGraph](https://img.shields.io/badge/LangGraph-%E2%9C%93-purple)
![混合搜索](https://img.shields.io/badge/混合搜索-%E2%9C%93-blue)
![自我修正](https://img.shields.io/badge/自我修正-%E2%9C%93-orange)

</div>

| 功能 | 描述 |
| :--- | :--- |
| **🔀 智能路由** | 基于意图分析，动态地将查询路由到专门的智能体。 |
| **🔍 查询优化** | 通过反思和重写来自我改进查询。 |
| **✅ 幻觉检测** | 通过忠实度评分，根据源文档验证响应。 |
| **🔄 自我修正** | 自动检测并修复不充分的响应。 |
| **📊 混合检索** | 结合语义搜索、关键词搜索和知识图谱搜索。 |

---

### 🚧 更多项目即将推出

<details><summary><b>🔮 计划中的项目（点击展开）</b></summary>

| 项目 | 描述 | 状态 |
| :--- | :--- | :--- |
| 🗣️ **语音RAG智能体** | 支持语音的问答，实时转录 | `计划中` |
| 🌐 **MCP浏览器智能体** | 基于模型上下文协议的浏览器自动化 | `计划中` |
| 🤝 **多智能体研究** | 具有任务交接的协作研究智能体 | `计划中` |
| 📄 **PDF聊天** | 支持混合搜索的文档问答 | `计划中` |
| 💬 **状态记忆** | 具有持久性记忆的对话式AI | `计划中` |

</details>

---

## 🚀 快速开始

### 🎯 快速启动比较（更新版）

| 方法 | 命令 | 时间 | 需要 |
|--------|---------|------|---------|
| **Python** | `pip install -r requirements.txt && python app.py` | 2-5分钟 | Python 3.9+ |
| **Docker** | `docker-compose up -d` | 30秒 | Docker + Compose |
| **Hugging Face** | [![Hugging Face](https://img.shields.io/badge/🤗%20Live%20Demo-FFD21E?style=flat-square)](https://huggingface.co/spaces/fcyber/agentic_rag) | 1秒 | 网页浏览器 |

### 📦 选项1：Python（本地设置）

1. **克隆代码库**
   ```bash
   git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)
   ```

2. **导航到所需项目目录**
   ```bash
   cd ai-engineering-hub/01-agentic-rag-assistant
   ```

3. **安装所需的依赖项**
   ```bash
   pip install -r requirements.txt
   ```

#### 请遵循每个项目`README.md`文件中的特定项目说明来设置和运行应用。

• • •

### 🐳 选项2：Docker Compose（推荐）
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/fcyber/agentic-rag-assistant)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)

1. **克隆代码库**
   ```bash
   git clone https://github.com/fcyber/ai-engineering-hub.git
   ```

2. **导航到所需项目目录**
   ```bash
   cd ai-engineering-hub/01-agentic-rag-assistant
   ```

3. **设置环境变量**
   ```bash
   cp .env.example .env
   # 使用您的API密钥编辑.env文件 GROQ_API_KEY
   ```

4. **使用Docker Compose运行**
   ```bash
   docker-compose up -d
   ```

5. **查看日志（可选）**
   ```bash
   docker-compose logs -f
   ```
6. **在浏览器中打开**
   ```bash
   http://localhost:7860
   ```
7. **停止容器**
   ```bash
   docker-compose down
   ```

**就这样！** 项目包含预配置的`Dockerfile`和`docker-compose.yml` — 无需额外设置。

• • •

### 🤗 选项3：Hugging Face Spaces

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/fcyber/)

```bash
# 无需安装！点击上面的徽章尝试在线演示。
# 或者克隆并在本地运行：
pip install huggingface-hub
huggingface-cli download fcyber/agentic-rag-assistant
python app.py  # Gradio应用通过python运行

```



## 🛠️ 技术栈

| 类别 | 技术 |
| --- | --- |
| LLM框架 | LangChain, LangGraph, LlamaIndex |
| 模型 | GPT-4, Claude 3.5, Sonnet, Gemini 1.5 Pro, Llama 3.1, Qwen 2.5 |
| 向量数据库 | Pinecone, Chroma, Weaviate, Qdrant |
| 嵌入技术 | OpenAI, Cohere, HuggingFace, Voyage |
| 前端 | Streamlit, Gradio, Chainlit |
| 监控 | LangSmith, Arize Phoenix, Weights & Biases |
| 部署 | Streamlit Cloud, Hugging Face Spaces, Docker, AWS |

---

## 🤝 参与贡献

我们欢迎贡献！请遵循以下步骤：

- 复刻（Fork）代码库
- 创建功能分支 
   ```bash
   git checkout -b feature/精彩项目
   ```
- 提交您的更改 
  ```bash
  git commit -am '添加精彩项目'
  ```
- 推送到分支
  ```bash
  git push origin feature/精彩项目
  ```
- 开启拉取请求（Pull Request）

### ✅ 贡献检查清单

- 独立的项目目录
- 包含设置说明的完整README文件
- 具有清晰设置步骤的有效演示
- 包含所有必需变量的`.env.example`文件
- 包含固定版本依赖的`requirements.txt`文件
- 展示功能的屏幕截图

---

## 🙏 感谢社区支持！

<br> <br>

<center>
⭐ 如果您觉得这个代码库有用，请给它加星！ ⭐

<br> <br>

---
 
## 📊 代码库统计

<div align="center">

| ⭐ **星标数** | 🍴 **复刻数** | 👀 **关注者** |
|:-----------:|:-----------:|:--------------:|
| [![GitHub Stars](https://img.shields.io/github/stars/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=ffd700)](https://github.com/fcyber101/ai-engineering-hub/stargazers) | [![GitHub Forks](https://img.shields.io/github/forks/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=58a6ff)](https://github.com/fcyber101/ai-engineering-hub/network/members) | [![GitHub Watchers](https://img.shields.io/github/watchers/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=2ea44f)](https://github.com/fcyber101/ai-engineering-hub/watchers) |

| 🐛 **问题** | 🔀 **拉取请求** | 📦 **版本发布** |
|:------------:|:----------:|:---------------:|
| [![GitHub Issues](https://img.shields.io/github/issues/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=f85149)](https://github.com/fcyber101/ai-engineering-hub/issues) | [![GitHub PRs](https://img.shields.io/github/issues-pr/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=f0883e)](https://github.com/fcyber101/ai-engineering-hub/pulls) | [![GitHub Release](https://img.shields.io/github/v/release/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=a371f7)](https://github.com/fcyber101/ai-engineering-hub/releases) |

| 👥 **贡献者** | 📅 **最后提交** | 📝 **许可证** |
|:------------------:|:------------------:|:--------------:|
| [![GitHub Contributors](https://img.shields.io/github/contributors/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/graphs/contributors) | [![GitHub Last Commit](https://img.shields.io/github/last-commit/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/commits/main) | [![GitHub License](https://img.shields.io/github/license/fcyber101/ai-engineering-hub?style=flat-square&logo=github&logoColor=white&labelColor=2d3339&color=6e7681)](https://github.com/fcyber101/ai-engineering-hub/blob/main/LICENSE) |

</div>

---
[![Star History Chart](https://api.star-history.com/svg?repos=fcyber101/ai-engineering-hub&type=Date)](https://star-history.com/#fcyber101/ai-engineering-hub&Date)
---

<sub>由AI工程师为AI工程师用❤️构建</sub>

</center>