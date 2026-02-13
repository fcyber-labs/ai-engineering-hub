

<div align="center">
  
[![EN](https://img.shields.io/badge/EN-English-blue)](README.md)
[![DE](https://img.shields.io/badge/DE-Deutsch-black)](README.de.md)
[![RU](https://img.shields.io/badge/RU-Русский-orange)](README.ru.md)
[![ZH](https://img.shields.io/badge/ZH-中文-yellow)](README.zh.md)

</div>



### 👨‍💼 [1. Agentischer RAG-Assistent](./01-agentic-rag-assistant)    
[![Demo Video](https://img.shields.io/badge/📺-Demo%20ansehen-red)](media/project_1.gif) [![Live App](https://img.shields.io/badge/🤗-Jetzt%20testen-yellow)](https://huggingface.co/spaces/fcyber/agentic_rag)

#### Intelligenter Frage-Antwort-Assistent mit intelligentem Routing, Anfragenverfeinerung, Halluzinationsprüfung und Selbstkorrekturschleifen.

<div align="center">

![Status](https://img.shields.io/badge/Status-Aktiv-success)
![Schwierigkeit](https://img.shields.io/badge/Schwierigkeit-Fortgeschritten-red)
![LangGraph](https://img.shields.io/badge/LangGraph-%E2%9C%93-purple)
![Hybride Suche](https://img.shields.io/badge/Hybride_Suche-%E2%9C%93-blau)
![Selbstkorrektur](https://img.shields.io/badge/Selbstkorrektur-%E2%9C%93-orange)

</div>

| Funktion | Beschreibung |
| :--- | :--- |
| **🔀 Intelligentes Routing** | Leitet Anfragen dynamisch basierend auf der Absichtsanalyse an spezialisierte Agenten weiter. |
| **🔍 Anfragenverfeinerung** | Verbessert Anfragen selbstständig durch Reflexion und Umschreibung. |
| **✅ Halluzinationsprüfung** | Validiert Antworten anhand von Quelldokumenten mit Treuebewertung. |
| **🔄 Selbstkorrektur** | Erkennt und behebt automatisch unzureichende Antworten. |
| **📊 Hybrider Abruf** | Kombiniert semantische Suche, Schlüsselwortsuche und Wissensgraphensuche. |

---



![Agentischer RAG-Workflow](media/workflow.jpeg)

---



## 🚀 Erste Schritte

### 🎯 Schnellstart-Vergleich (Aktualisiert)

| Methode | Befehl | Zeit | Erfordert |
|--------|---------|------|-----------|
| **Python** | `pip install -r requirements.txt && python app.py` | 2-5 Min | Python 3.9+ |
| **Docker** | `docker-compose up -d` | 30 Sek | Docker + Compose |
| **Hugging Face** | [![Hugging Face](https://img.shields.io/badge/🤗%20Live-Demo-FFD21E?style=flat-square)](https://huggingface.co/spaces/fcyber/agentic_rag) | 1 Sek | Webbrowser |

### 📦 Option 1: Python (Lokale Einrichtung)


1. **Repository klonen**
```bash
git clone [https://github.com/fcyber/ai-engineering-hub.git](https://github.com/fcyber/ai-engineering-hub.git)
```

2. **In das gewünschte Projektverzeichnis navigieren**
```bash
cd ai-engineering-hub/01-agentic-rag-assistant
```

3. **Erforderliche Abhängigkeiten installieren**
```bash
pip install -r requirements.txt
```

#### Befolgen Sie die projektspezifischen Anweisungen in der `README.md`-Datei jedes Projekts, um die App einzurichten und auszuführen.

• • •

### 🐳 Option 2: Docker Compose (Empfohlen)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/fcyber/agentic-rag-assistant)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
1. **Repository klonen**
```bash
git clone https://github.com/fcyber/ai-engineering-hub.git
```

2. **In das gewünschte Projektverzeichnis navigieren**
```bash
cd ai-engineering-hub/01-agentic-rag-assistant
```

3. **Umgebungsvariablen einrichten**
```bash
cp .env.example .env
# .env mit Ihren GROQ_API_KEY-Schlüsseln bearbeiten
```

4. **Mit Docker Compose ausführen**
```bash
docker-compose up -d
```

5. **Logs anzeigen (optional)**
```bash
docker-compose logs -f
```

6. **Zugriff auf die Anwendung (optional)**
Besuchen Sie [http://localhost:7860](http://localhost:7860) im Browser.

7. **Container stoppen**
```bash
docker-compose down
```

**Das war's!** Das Projekt enthält ein vorkonfiguriertes `Dockerfile` und `docker-compose.yml` — keine zusätzliche Einrichtung erforderlich.

• • •

### 🤗 Option 3: Hugging Face Spaces

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/fcyber/)

```bash
# Keine Installation erforderlich! Klicken Sie auf das Abzeichen oben, um die Live-Demo zu testen.
# Oder klonen und lokal ausführen:
pip install huggingface-hub
huggingface-cli download fcyber/agentic-rag-assistant
python app.py  # Gradio-Apps werden mit python ausgeführt

```
