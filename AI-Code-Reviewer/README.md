# 🧠 AI-Code-Reviewer  

AI-Code-Reviewer is a **Hybrid Ai powered multi-language automated code review platform** that helps developers analyze, review, and improve their code efficiently.

For cloud deployed repository vew **Ai-Code-Reviewer**: [Repository](https://github.com/Krishna-S-27/Ai-Code-Reviewer)

### ✨ Features  
- ✔️ **Linting**: Python, JavaScript, C/C++  
- ✔️ **Complexity Analysis**: Understand code maintainability  
- ✔️ **AI-Powered Review**: Java & Go (style, best practices, improvements)  
- ✔️ **PDF Report Generation**: Export clean review reports  

### 🏗️ Tech Stack  
- **Backend**: FastAPI (Python)  
- **Frontend**: Streamlit (with custom CSS for professional UI)  
- **Deployment**: Render (for cloud hosting)  

### 🚀 Live Demo  
- 🔗 **Backend API**: [AI-Code-Reviewer Backend](https://ai-code-reviewer-backend-udx1.onrender.com)  
- 🎨 **Frontend UI**: [AI-Code-Reviewer Frontend](https://ai-code-reviewer-frontend-3pi1.onrender.com)  

---


## 📌 Project Idea

Developers often spend time fixing style issues, handling code smells, and  
checking complexity before a proper review. This tool automates those steps.

👉 You paste/upload your code → The backend runs linters & AI analysis →  
Frontend displays results (lint, complexity, AI suggestions) → You can download  
a **professional PDF review report**.

This makes code reviews **faster, consistent, and AI-assisted**.

---

## ⚙️ Features

- 🔍 **Linting**: Python (`pylint`), JavaScript (`eslint`), C/C++ (`cpplint`)  
- 📊 **Complexity**: Python (`radon`), JS/Go (`gocyclo`), C++ (`lizard`)  
- 🤖 **AI Review**: Uses AI prompts for deeper feedback (Java, Go, Python)  
- 📄 **PDF Reports**: Generates downloadable reports for sharing with teams  
- 🎨 **Modern UI**: Streamlit + custom CSS styling  
- ☁️ **Deployment Ready**: Works on Render (backend + frontend)

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), Python, Linting Tools  
- **Frontend**: [Streamlit](https://streamlit.io/), Custom CSS  
- **AI Review**: Integrated with LLM (AI prompts for code analysis)  
- **Complexity**: `radon`, `lizard`, `gocyclo`  
- **Deployment**: [Render](https://render.com/)  

---

## 🚀 How It Works

1. **User Input**  
   - Paste code in textarea OR upload a file (`.py`, `.js`, `.cpp`, `.java`, `.go`).  

2. **Backend Processing**  
   - Chooses appropriate toolset based on language.  
   - Runs linters & complexity analyzers if available.  
   - If AI-only language → sends code to AI reviewer service.  

3. **Results**  
   - Lint warnings (style, unused vars, missing semicolons, etc.)  
   - Cyclomatic complexity & metrics  
   - AI feedback with suggestions  
   - Option to generate/download a **PDF report**  

4. **Frontend**  
   - Streamlit UI displays results in clean sections.  
   - Download button lets user save PDF locally.  

---

## 🖥️ Local Development

### 1. Clone Repository
```bash
git clone https://github.com/Krishna-S-27/AI-Code-Reviewer.git
cd AI-Code-Reviewer
2. Backend Setup
cd backend
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt
uvicorn main:app --reload
Backend will run on → http://127.0.0.1:8000

3. Frontend Setup
bash
Copy code
cd ../frontend
pip install -r requirements.txt
streamlit run app.py
Frontend will run on → http://localhost:8501

Note: add your api key in root file and save .env 

🌐 Deployment (Render)
Backend
Push project to GitHub.

On Render → Create New Web Service → Connect repo → Select backend/.

Build Command:

pip install -r requirements.txt

Start Command:

uvicorn main:app --host 0.0.0.0 --port 10000

Frontend

Change the backend url to the backend render url as current repository is from locol host.
Create another Render Web Service → point to frontend/.

Build Command:

pip install -r requirements.txt
Start Command:

streamlit run app.py --server.port 10000 --server.address 0.0.0.0
✅ Now you can open the frontend Render URL → enter backend Render URL in sidebar → Start reviewing code!
```
---

## 👨‍💻 Credits  

Built by `Krishna Shalawadi` using FastAPI, Streamlit, and AI.  

