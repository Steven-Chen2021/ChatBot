
# 📘 System Specification – Embedded AI Chatbot with Admin Portal

## 1. Overview
An embeddable, floating AI chatbot for web applications, using Gemini AI to answer user questions based on unstructured documents in a specific folder. It includes an Admin Portal to manage prompts and file uploads. The backend is developed in Python with API-based architecture.

---

## 2. System Components

### 2.1 Frontend – Chatbot Widget
- **Tech**: Web Component (Lit)
- **Features**:
  - Embeddable/floating on any existing web page
  - Toggle button (open/minimize)
  - Chat interface with loading and typing indicators
  - Message history (session-based or persistent)
  - Supports light/dark mode (optional)

### 2.2 Frontend – Admin Portal
- **Tech**: Vue.js
- **Features**:
  - **Prompt Configuration**:
    - Set system prompt/instructions for Gemini
    - Upload or edit prompt templates (per department or use case)
  - **File Upload**:
    - Upload unstructured files (PDF, DOCX, TXT)
    - File tags or categories 
    - Auto-index on upload
  - **File Management**:
    - View list of indexed files with timestamp
    - Delete or reindex specific files
  - **Usage Log** :
    - View recent chat queries
    - Export logs or summary

---

## 3. Backend (Python API)
- **Framework**: FastAPI preferred (high performance, async-ready)
- **Endpoints**:
  - `/chat`: Accepts user query and returns Gemini response
  - `/admin/upload`: Handles file uploads
  - `/admin/prompts`: Get/set system prompt templates
  - `/admin/files`: List/delete/reindex files
  - `/status`: Health check

- **Modules**:
  - File Processor: Extracts text from PDF/DOCX/TXT
  - Vector Indexing: FAISS or ChromaDB (performs semantic search)
  - Prompt Engine: Combines system prompt + retrieved content + user query
  - Gemini Connector: Sends prompt to Gemini AI and returns answer

---

## 4. AI Chatbot – Gemini Integration
- **Model**: Gemini Pro or Enterprise
- **Prompt Flow**:
  - Load system prompt (configurable)
  - Retrieve top-N relevant content from file embeddings
  - Construct structured prompt (context + question)
  - Send to Gemini, return answer

---

## 5. File Management & Embedding
- **Storage**: Local folder or mounted volume (e.g., `/data/unstructured`)
- **Supported File Types**: PDF, DOCX, TXT
- **Indexing**: Scheduled or triggered by upload
- **Embedding Storage**: Local vector DB (e.g., FAISS/Chroma) or cloud option

---

## 6. Architecture Diagram
```
[ Web App ]
   ↓ embed
[ Floating Chat Widget ] ←→ [ Python Backend API ] ←→ [ Gemini AI ]
                                     ↑
                           [ Prompt Config & File Index ]
                                     ↑
                           [ Admin Portal (Web UI) ]
                                     ↑
                      [ File Uploads & Embeddings Storage ]
```

---

## 7. Integration & Deployment
- **Frontend Widget**: Simple script or Vue component
- **Backend**: Dockerized, API with environment-configurable settings
- **Admin Auth**: Basic login or OAuth2 for admin portal
- **Security**:
  - HTTPS, API keys/token-based access
  - File upload validation (file size, type)
  - Input sanitization & rate limiting

---

## 8. Optional Enhancements
- Multiple prompt presets per use case
- User feedback on chatbot answers
- WebSocket support for real-time chat
- File change monitor for automatic re-index
