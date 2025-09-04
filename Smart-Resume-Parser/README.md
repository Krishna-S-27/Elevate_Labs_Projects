# 📄 Smart Resume Parser  

An **AI-powered Resume Parser** that extracts structured candidate information, generates insights to evaluate resumes.

For cloud deployed code repository visit **Smart-Resume-Parser**: [Repository](https://github.com/Krishna-S-27/Smart-Resume-Parser)

---

## ✨ Features  

✅ Upload resumes in **PDF/DOCX** format  
✅ Extracts **Name, Email, Phone, Skills, Education, Experience, Projects, Certificates, Links, and Summary**. 
✅ Modern **Streamlit Dashboard** with custom UI/UX  
✅ Export parsed results into **JSON & CSV**  
✅ Backend built with **FastAPI**, integrated with **OpenRouter (gpt-oss-120b)**  
✅ Deployable on **Render Cloud**  

---

### 🚀 Live Demo  
- 🔗 **Backend API**: [Smart-Resume-Parser-Backend](https://smart-resume-parser-backend-url.onrender.com)  
- 🎨 **Frontend UI**: [Smart-Resume-Parser-Frontend](https://smart-resume-parser-frontend-url.onrender.com)  

---

## 🔎 How It Works  

The **Smart Resume Parser** follows a simple yet powerful workflow:  

1. **Upload Resume (PDF/DOCX)**  
   - Candidate uploads their resume from the frontend.  

2. **Text Extraction**  
   - Backend extracts raw text using **PyPDF2** (for PDFs) and **python-docx** (for DOCX).  

3. **Preprocessing**  
   - The extracted text is cleaned (removing headers, footers, unnecessary spaces).  

4. **AI Parsing (OpenRouter API)**  
   - Resume text is sent to **gpt-oss-120b(via OpenRouter API)** with a **JSON schema prompt**.  
   - AI returns structured data: Name, Email, Phone, Skills, Education, Experience, Projects, Links, Summary, etc.   

5. **Frontend Dashboard (Streamlit)**  
   - Results are displayed in a modern **dashboard view** (skills → tags, education/experience → timelines).  
   - Candidate can **download results in JSON/CSV** format.  

6. **Deployment**  
   - Both **backend (FastAPI)** and **frontend (Streamlit)** can be deployed on **Render Cloud** for production use.  

---

## 💡 Inspiration & Idea  

The idea for this project came from real-world hiring challenges:  

- Recruiters often **spend hours manually reading resumes**.  
- Many resumes are unstructured (different formats, missing details). 

👉 So, I decided to build an **AI-powered Resume Parser** that extracts structured details.  

This makes it useful for:  
- **Recruiters** → Quick screening of resumes  
- **Job Seekers** → Understanding strengths & weaknesses of their resume  
- **Developers/Students** → Automating resume reviews during placement drives  

---

## 🛠️ Tech Stack  

**Frontend:**  
- Streamlit (Python)  
- Custom CSS for professional dashboard  

**Backend:**  
- FastAPI (Python)  
- OpenRouter API (Mistral-7B Instruct model)  
- PyPDF2, python-docx (Resume text extraction)  

**Data Handling:**  
- JSON, CSV (Export)  
- Pandas  

**Deployment:**  
- Render Cloud (Backend & Frontend services)  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/your-username/smart-resume-parser.git
cd smart-resume-parser
2️⃣ Setup Backend
cd backend
pip install -r requirements.txt
Create a .env file:

OPENROUTER_API_KEY=your_openrouter_api_key
Run backend:
uvicorn app:app --host 0.0.0.0 --port 8000
3️⃣ Setup Frontend
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
🚀 Usage
Start backend (uvicorn) and frontend (streamlit).

Open frontend (default: http://localhost:8501).

Upload a resume (PDF/DOCX).

View extracted details (skills, education, experience, projects, links, summary).

Get AI-powered resume

Download results as JSON/CSV.

📦 Deployment (Render)
Create two Web Services on Render:

Backend: Python (FastAPI) → uvicorn app:app --host 0.0.0.0 --port 8000

Frontend: Streamlit → streamlit run streamlit_app.py --server.port 10000 --server.address 0.0.0.0

Add .env with your OPENROUTER_API_KEY.

Both services connect automatically via API.
```

---


# 🔮 Future Enhancements
Role-specific scoring system (e.g., Data Scientist, Web Developer)

Candidate-job matching (resume → job description)

Support for multilingual resumes

ATS (Applicant Tracking System) integration

---


## 👨‍💻 Developed by Krishna Shalawadi
