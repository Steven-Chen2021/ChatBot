# 🚀 Embedded AI Chatbot System – README

This project is an embeddable AI chatbot system powered by Gemini AI, designed for integration into existing web applications. It includes a floating chatbot widget, an Admin Portal for managing prompts and file uploads, and a Python FastAPI backend.

---

## 🔧 Tech Stack & Versions

### 🧩 Frontend – Chatbot Widget
- **Tech**: [Lit](https://lit.dev/) (Web Components)
- **Suggested Version**: `^3.0.0`
- **Why**: Lightweight, fast, and modern standard for building encapsulated web components.

### 🛠️ Frontend – Admin Portal
- **Tech**: [Vue.js](https://vuejs.org/)
- **Suggested Version**: `^3.4.0`
- **UI Library**: [Element Plus](https://element-plus.org/) `^2.5.0` or [Vuetify](https://vuetifyjs.com/) `^3.2.0`
- **Why**: Vue 3 offers Composition API and TypeScript support; Element Plus/Vuetify provides rich components for admin dashboards.

### 🔙 Backend API
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Suggested Version**: `^0.110.0`
- **Runtime**: Python `^3.11`
- **Why**: High-performance async API with automatic OpenAPI generation.

### 🔍 Semantic Search & Embedding
- **Vector DB**: [FAISS](https://github.com/facebookresearch/faiss) `1.7.4` or [ChromaDB](https://www.trychroma.com/) `^0.4.0`
- **Text Extraction**:
  - PDFs: `pdfplumber` `^0.10.0`
  - DOCX: `python-docx` `^1.1.0`
  - TXT: Native handling
- **Prompt/Embedding Management**: Custom module (Prompt Engine)

### 🤖 Gemini AI Integration
- **Model**: Gemini Pro or Gemini Enterprise
- **API Access**: Use official Gemini SDK or HTTPS call via Google AI Platform

---

## 📁 Project Structure

```
/chatbot-system
│
├── /frontend-widget     # Lit-based Web Component
├── /admin-portal        # Vue 3 + Element Plus or Vuetify
├── /backend-api         # FastAPI Python service
│   ├── /file_processor
│   ├── /vector_indexing
│   ├── /prompt_engine
│   └── /gemini_connector
├── /data/unstructured   # Uploaded documents
└── README.md
```

---

## ⚙️ Deployment

- **Containerization**: Use Docker for backend
- **Frontend Hosting**: Deploy to existing web server or static host
- **Security**:
  - Use HTTPS
  - Enable API token authentication
  - OAuth2 or simple login for Admin Portal
  - Sanitize inputs and validate uploads

---

## 🛡️ API Endpoints (Backend)

| Endpoint           | Method | Description                          |
|--------------------|--------|--------------------------------------|
| `/chat`            | POST   | Query Gemini with prompt+context     |
| `/admin/upload`    | POST   | Upload unstructured documents        |
| `/admin/prompts`   | GET/POST | Manage prompt templates            |
| `/admin/files`     | GET/DELETE | List or delete indexed files    |
| `/status`          | GET    | Health check                         |

---

## 🌱 Optional Enhancements

- Real-time chat via WebSockets
- Multiple prompt presets per use case
- Chat feedback and rating
- File watcher for auto-indexing

---

## 🧪 Recommended Dev Tools

- **Code Editor**: VSCode
- **Linting**: ESLint (for Vue/Lit), flake8 or ruff (for Python)
- **Testing**:
  - Frontend: Vitest/Jest
  - Backend: Pytest
- **CI/CD**: GitHub Actions / GitLab CI

---

## 🧠 License & Credits

This project uses:
- Google Gemini AI (commercial license may apply)
- FAISS/ChromaDB for vector indexing
- Open-source libraries as listed

---
