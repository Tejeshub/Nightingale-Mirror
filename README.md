<div align="center">

# 📊 EquityLens AI

### *Institutional-Grade Multi-Agent Equity Research Platform for Indian Small & Mid Cap Companies*

**EquityLens AI** automates institutional-grade equity research using multiple AI agents that collect, verify, debate, and synthesize financial information into evidence-backed reports with confidence scores and source citations.

### 🚀 Live Frontend Demo - https://nightingale-mirror.vercel.app
### ⚡ Live Backend API - https://nightingale-mirror-backend.onrender.com
### 📺 Youtbue Video - https://www.youtube.com/watch?v=Yt4_0WRjuKI


[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)](https://react.dev)
[![Vite](https://img.shields.io/badge/Vite-5-646CFF?style=flat-square&logo=vite)](https://vitejs.dev)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql)](https://postgresql.org)
[![Gemini](https://img.shields.io/badge/Gemini-Pro-4285F4?style=flat-square&logo=google)](https://ai.google.dev)
[![Groq](https://img.shields.io/badge/Groq-Llama3-f3652b?style=flat-square)](https://groq.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

</div>

---

## ✨ Key Features

- 🤖 **Multi-Agent AI Research** — Employs a specialized team of AI agents (Ingestion, Fundamental, Sentiment, Alternative Data) orchestrated by a Coordinator to autonomously conduct exhaustive research.
- 🔎 **Semantic Search** — Powerful natural language query engine to instantly find relevant financial data, filings, and qualitative metrics.
- 🏢 **Company Discovery** — Seamlessly filter and discover Indian Small & Mid Cap equities based on dynamic screening criteria.
- 📑 **AI Reports** — Generates complete, beautifully formatted, and objective equity research reports, simulating a top-tier financial analyst.
- 💬 **Research Copilot (QA Agent)** — Interactive chatbot contextually aware of the currently analyzed company, capable of answering specific financial queries.
- 🧠 **Agent Reasoning** — Full transparency into the multi-agent debate process; watch as agents propose arguments, verify claims, and reach a consensus.
- ⭐ **Watchlists** — Curate and track personalized lists of compelling equities to monitor their long-term performance and narrative shifts.
- ⚖️ **Comparative Analysis** — Evaluate multiple companies side-by-side using the dedicated Comparator agent to discover relative valuation and strategic advantages.
- 🎯 **Confidence Scoring** — Every insight and generated report is accompanied by an AI-calculated confidence score, providing a clear gauge of data reliability.
- 🔗 **Source Citation** — Claims are traced back to their origins (earnings transcripts, market news, specific filings), ensuring traceability and trust.

---

## 🖼️ Screenshots

**Landing Page — Gateway to EquityLens AI**
<div align="center">
  <img src="screenshots/01-home-hero.png" alt="EquityLens AI Landing Page">
</div>

---

**Market Discovery — Find the Next Multi-Bagger**
<div align="center">
  <img src="screenshots/02-discover-market.png" alt="Market Discovery">
</div>

---

**Smart Search — Semantic Querying**
<div align="center">
  <img src="screenshots/03-smart-search.png" alt="Smart Search">
</div>

---

**Company Overview — The Dashboard**
<div align="center">
  <img src="screenshots/04-company-overview.png" alt="Company Overview">
</div>

---

**Price Chart & News — Contextual Market Data**
<div align="center">
  <img src="screenshots/05-price-chart-news.png" alt="Price Chart & News">
</div>

---

**Financial Statements — Standardized Fundamentals**
<div align="center">
  <img src="screenshots/06-financial-statements.png" alt="Financial Statements">
</div>

---

**AI Research Report — Analyst-Grade Synthesis**
<div align="center">
  <img src="screenshots/07-ai-research-report.png" alt="AI Research Report">
</div>

---

**Research Copilot — Your Personal Analyst**
<div align="center">
  <img src="screenshots/08-research-copilot.png" alt="Research Copilot">
</div>

---

**Agent Reasoning — Transparency in Action**
<div align="center">
  <img src="screenshots/09-agent-reasoning.png" alt="Agent Reasoning">
</div>

---

**Watchlists — Track Your Portfolio**
<div align="center">
  <img src="screenshots/10-watchlists.png" alt="Watchlists">
</div>

---

**Live Multi-Agent Analysis — Watching the Debate**
<div align="center">
  <img src="screenshots/11-analysis-loading.png" alt="Live Multi-Agent Analysis">
</div>

---

**Comparative Research Report — Relative Valuation**
<div align="center">
  <img src="screenshots/12-comparative-analysis.png" alt="Comparative Research Report">
</div>

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User([👤 User]) --> FE[React Frontend]
    FE --> BE[FastAPI Backend]
    
    subgraph Engine [AI Research Engine]
        BE --> Agents[🤖 AI Agents]
        Agents --> LLM1[Gemini]
        Agents --> LLM2[Groq]
    end
    
    subgraph Data [Data & Persistence]
        Agents --> VDB[(ChromaDB)]
        Agents --> RDB[(PostgreSQL)]
    end
    
    subgraph External [External Tools]
        Agents --> FC[Firecrawl Web Scraper]
        Agents --> Exa[Exa Web Search]
    end

    style User fill:#4f46e5,color:#fff
    style FE fill:#61dafb,color:#000
    style BE fill:#059669,color:#fff
    style Agents fill:#9333ea,color:#fff
    style VDB fill:#ea580c,color:#fff
    style RDB fill:#336791,color:#fff
```

---

## 🧠 Multi-Agent Architecture

The core of EquityLens AI is its collaborative multi-agent framework. Agents are designed to handle specific domains of research, debate conflicting viewpoints, and synthesize a cohesive final report.

```mermaid
flowchart TD
    Coord[👑 Coordinator Agent] --> Ingest[📥 Ingestion Agent]
    
    Ingest --> Fund[📊 Fundamental Debater]
    Ingest --> Sent[📰 Sentiment Debater]
    Ingest --> Alt[🌐 Alternative Data Debater]
    
    Fund --> Debate{Debate & Verification}
    Sent --> Debate
    Alt --> Debate
    
    Debate --> Coord
    
    Coord --> Comp[⚖️ Comparator Agent]
    Coord --> QA[💬 QA Agent / Research Copilot]
    Coord --> Report[📝 Report Generator]

    style Coord fill:#dc2626,color:#fff
    style Ingest fill:#ea580c,color:#fff
    style Fund fill:#2563eb,color:#fff
    style Sent fill:#16a34a,color:#fff
    style Alt fill:#9333ea,color:#fff
    style Debate fill:#4b5563,color:#fff
```

---

## 🔍 RAG Pipeline

EquityLens AI implements an advanced Retrieval-Augmented Generation (RAG) pipeline to ensure all generated insights are anchored in verified, ingested financial data.

```mermaid
flowchart LR
    Docs[📄 Financial Documents] --> Chunk[✂️ Chunking]
    Chunk --> Embed[🧠 Embedding]
    Embed --> Chroma[(ChromaDB)]
    
    Query[User Query / Agent Request] --> Retriever[🔎 Retriever]
    Chroma -.-> Retriever
    
    Retriever --> LLM[🤖 Gemini / Groq]
    LLM --> Answer[✅ Verified Answer & Citation]

    style Docs fill:#64748b,color:#fff
    style Chroma fill:#ea580c,color:#fff
    style LLM fill:#4f46e5,color:#fff
    style Answer fill:#16a34a,color:#fff
```

---

## 💻 Tech Stack

### Frontend

| Technology | Purpose |
|---|---|
| **React** | Component-based UI library |
| **Vite** | Blazing fast build tool and dev server |
| **TypeScript** | Type-safe JavaScript |
| **Tailwind CSS** | Utility-first CSS styling framework |
| **shadcn/ui** | Accessible and customizable UI components |

### Backend

| Technology | Purpose |
|---|---|
| **FastAPI** | High-performance Python web framework |
| **Python 3.10+** | Core backend language |

### AI & Data

| Technology | Purpose |
|---|---|
| **Gemini** | Primary LLM for generative reasoning and QA |
| **Groq** | Ultra-fast inference for specific agent tasks |
| **ChromaDB** | Vector database for RAG semantic search |
| **PostgreSQL** | Relational database for structured financial data |
| **Exa** | Intelligent web search API |
| **Firecrawl** | Specialized web scraping for financial reports |
| **PyPDF** | Parsing and extracting data from PDF filings |

### Deployment

| Component | Platform |
|---|---|
| **Frontend** | Vercel |
| **Backend** | Render |

---

## 🗂️ Folder Structure

```text
Nightingale-Mirror/
├── backend/
│   ├── agents/                   # Multi-agent logic (Coordinator, Debaters, Copilot)
│   ├── data/                     # Data processing utilities
│   ├── rag/                      # Retrieval-Augmented Generation modules
│   ├── storage/                  # Database models and interaction layers
│   ├── tools/                    # Search, scraper, and external API wrappers
│   ├── config.py                 # Environment configuration
│   ├── main.py                   # FastAPI application entrypoint
│   └── requirements.txt          # Python backend dependencies
│
├── frontend/
│   └── insight-navigator/        # React/Vite Frontend Application
│       ├── src/                  # React components, pages, and contexts
│       ├── package.json          # Node.js dependencies
│       └── tailwind.config.js    # Tailwind CSS configuration
│
├── screenshots/                  # UI showcase images
└── README.md                     # This file
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tejesh/Nightingale-Mirror.git
cd Nightingale-Mirror
```

### 2. Backend Setup

```bash
cd backend

# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
# From the root directory, navigate to the frontend folder
cd frontend/insight-navigator

# Install dependencies
npm install  # or yarn install / pnpm install
```

### 4. Run the Application Locally

**Start the Backend (FastAPI):**
```bash
# In the backend/ directory
uvicorn main:app --reload --port 8000
```

**Start the Frontend (Vite):**
```bash
# In the frontend/insight-navigator/ directory
npm run dev
```

The frontend will be available at `http://localhost:5173` (or port 3000 depending on Vite config), and the backend API at `http://localhost:8000`.

---

## 🔐 Environment Variables

Create `.env` files in the respective directories before running the application.

### Backend (`backend/.env`)

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Google Gemini API key for the core LLM |
| `GROK_API_KEY` | Groq API key for fast inference models |
| `EXA_API_KEY` | Exa API key for intelligent web search |
| `LLAMA_CLOUD_API_KEY` | Llama Cloud API key for advanced parsing |
| `FIRECRAWL_API_KEY` | Firecrawl API key for scraping web data |
| `POSTGRES_URL` | Connection string for PostgreSQL database |
| `CHROMA_PERSIST_DIR` | Local directory to persist ChromaDB vectors |
| `ALLOWED_ORIGINS` | CORS origins (e.g., `http://localhost:5173,http://localhost:3000`) |

### Frontend (`frontend/insight-navigator/.env`)

| Variable | Description |
|---|---|
| `VITE_API_URL` | Backend URL (e.g., `http://localhost:8000` for local dev) |

---

## 📡 API Endpoints

The FastAPI backend exposes several core endpoints to power the platform. *(Full interactive documentation available at `/docs` when running the backend).*

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Application health check and status |
| `POST` | `/analyze` | Triggers the multi-agent pipeline to generate a comprehensive equity research report |
| `POST` | `/ask` | Queries the Research Copilot (QA Agent) with context-aware financial questions |

---

## 🚀 Deployment

- **Frontend (Vercel):** The React/Vite application is highly optimized for static and edge deployment. Connect the repository to Vercel and set the Root Directory to `frontend/insight-navigator`. Ensure `VITE_API_URL` is set to the production backend URL.
- **Backend (Render):** The FastAPI application is deployed as a Web Service on Render. Set the Start Command to `uvicorn main:app --host 0.0.0.0 --port $PORT` and configure all necessary environment variables.

---

## 🗺️ Roadmap

> [!NOTE]  
> EquityLens AI is continuously evolving. Here is a glimpse of what is planned for the future:

- [ ] **Real-Time Market Data Integration:** Connect to live market streams (e.g., Alpha Vantage, Yahoo Finance).
- [ ] **Enhanced Portfolio Tracking:** Advanced metrics for watchlists including P&L tracking and risk analysis.
- [ ] **Export Functionality:** Download generated AI Research Reports as PDF or Word documents.
- [ ] **Expanded Agent Capabilities:** Introduce dedicated agents for Macroeconomic Analysis and Regulatory Risk.
- [ ] **User Authentication:** Personalized accounts to save histories, settings, and custom research criteria.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Future Improvements

* Add persistent user authentication and session management.
* Implement asynchronous task queues (e.g., Celery) to prevent timeout on extremely long analysis tasks.
* Expand peer comparison logic dynamically beyond static metrics.

