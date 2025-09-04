# app.py — Streamlit frontend for AI-Code-Reviewer
# ------------------------------------------------
# Features
# - Professional single-page UI with sidebar controls
# - Paste code OR upload a file
# - Calls your FastAPI backend: /api/analyze, /api/report
# - Shows AI review (Java/Go) and linter output (JS/C++/Python) elegantly
# - Lets you download the generated PDF report
#
# How to run:
#   1) pip install -r requirements.txt  (streamlit, requests, python-dotenv)
#   2) streamlit run app.py
#
# Optional: create a .env in the same folder with BACKEND_URL=http://127.0.0.1:8000

import io
import os
import time
import base64
import requests
import streamlit as st
from typing import Tuple, Dict, Any

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# ----------------------------------
# Config
# ----------------------------------
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
ANALYZE_ENDPOINT = f"{BACKEND_URL}/api/analyze"
REPORT_ENDPOINT = f"{BACKEND_URL}/api/report"

SUPPORTED_LANGS = [
    "python",
    "javascript",
    "java",
    "cpp",
    "go",
]

LANG_LABELS = {
    "python": "Python",
    "javascript": "JavaScript",
    "java": "Java (AI-only)",
    "cpp": "C/C++",
    "go": "Go (AI-only)",
}

# ----------------------------------
# Styling (CSS)
# ----------------------------------
st.set_page_config(page_title="AI-Code-Reviewer", page_icon="🧠", layout="wide")

CUSTOM_CSS = """
/* Global */
:root {
  --brand: #6C63FF;
  --bg: #0f172a;
  --panel: #111827;
  --text: #e5e7eb;
  --muted: #9ca3af;
  --accent: #22d3ee;
}

/* Page background */
[data-testid="stAppViewContainer"] > .main {
  background: radial-gradient(1000px 500px at 10% 10%, #0b1220, var(--bg));
  color: var(--text);
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0b1020 0%, #0c1224 100%);
  border-right: 1px solid #1f2937;
}

/* Cards */
.block-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 18px 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

/* Headings */
h1, h2, h3 {
  color: #f9fafb;
}

/* Buttons */
.stButton > button {
  background: linear-gradient(90deg, var(--brand), var(--accent));
  color: black;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  padding: 0.6rem 1rem;
  transition: transform 0.05s ease-in-out;
}
.stButton > button:active {
  transform: translateY(1px) scale(0.99);
}

/* Code blocks */
pre, code, .stCodeBlock {
  background: #0b1220 !important;
  border: 1px solid #1f2937 !important;
}

/* Metrics */
.kpi {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 10px 14px;
  border-radius: 12px;
  font-size: 0.9rem;
}
"""

st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)

# ----------------------------------
# Small helpers
# ----------------------------------

def _multipart_for_code(code: str, filename: str = "code.txt") -> Tuple[Dict[str, Any], Dict[str, Any]]:
    files = {
        "file": (filename, code.encode("utf-8"), "text/plain")
    }
    data = {}
    return data, files


def _multipart_for_upload(uploaded) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    if uploaded is None:
        return {}, {}
    bytes_data = uploaded.getvalue() if hasattr(uploaded, "getvalue") else uploaded.read()
    files = {
        "file": (uploaded.name, bytes_data, uploaded.type or "application/octet-stream")
    }
    data = {}
    return data, files


def call_backend(endpoint: str, language: str, files: Dict[str, Any]) -> Dict[str, Any]:
    data = {"language": language}
    try:
        resp = requests.post(endpoint, data=data, files=files, timeout=120)
        if resp.status_code == 200:
            try:
                return resp.json()
            except Exception:
                return {"_raw": resp.content, "_headers": dict(resp.headers)}
        else:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def download_button_bytes(filename: str, data: bytes, mime: str = "application/octet-stream"):
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:{mime};base64,{b64}" download="{filename}">📄 Download {filename}</a>'
    st.markdown(href, unsafe_allow_html=True)

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("🧠 AI-Code-Reviewer")
st.sidebar.caption("Frontend for your FastAPI backend")

selected_lang = st.sidebar.selectbox("Language", SUPPORTED_LANGS, format_func=lambda x: LANG_LABELS.get(x, x))

# ✅ Only Analyze & Report
mode = st.sidebar.radio("Action", ["Analyze", "Report"], index=0)

st.sidebar.markdown("---")
st.sidebar.subheader("Backend")
st.sidebar.text_input("Backend URL", value=BACKEND_URL, key="backend_url")
if st.sidebar.button("Apply URL"):
    burl = st.session_state.get("backend_url") or BACKEND_URL
    st.session_state["_BACKEND_URL"] = burl
    st.toast(f"Using backend: {burl}")

if "_BACKEND_URL" in st.session_state:
    _b = st.session_state["_BACKEND_URL"]
    ANALYZE_ENDPOINT = f"{_b}/api/analyze"
    REPORT_ENDPOINT = f"{_b}/api/report"

st.sidebar.markdown("---")
st.sidebar.write("Tip: Paste code below or upload a file.")

# ----------------------------------
# Header
# ----------------------------------
st.title("AI-Code-Reviewer")
st.write(
    "Upload code or paste it below, choose a language, and run analysis. "
    "Java & Go use AI-only review. JS/Python/C++ show linter output if tools are present."
)

# ----------------------------------
# Input area: paste or upload
# ----------------------------------
col1, col2 = st.columns([2, 1], gap="large")
with col1:
    code_input = st.text_area(
        "Paste your code here",
        height=280,
        placeholder="// Paste code...\n",
    )
with col2:
    uploaded = st.file_uploader("...or upload a file", type=["py", "js", "java", "cpp", "cc", "c", "go", "txt"])

# ----------------------------------
# Action buttons
# ----------------------------------
colA, colB = st.columns([1, 1])
run_clicked = False
if mode == "Analyze":
    run_clicked = colA.button("🔍 Analyze", use_container_width=True)
else:  # Report
    run_clicked = colB.button("📄 Generate Report (PDF)", use_container_width=True)

# ----------------------------------
# Execute
# ----------------------------------
if run_clicked:
    if uploaded is not None:
        data, files = _multipart_for_upload(uploaded)
        filename_display = uploaded.name
    elif code_input.strip():
        ext_map = {"python": ".py", "javascript": ".js", "java": ".java", "cpp": ".cpp", "go": ".go"}
        pseudo_name = f"pasted{ext_map.get(selected_lang, '.txt')}"
        data, files = _multipart_for_code(code_input, filename=pseudo_name)
        filename_display = pseudo_name
    else:
        st.warning("Please paste code or upload a file first.")
        st.stop()

    with st.spinner("Contacting backend..."):
        start = time.time()
        if mode == "Analyze":
            result = call_backend(ANALYZE_ENDPOINT, selected_lang, files)
        else:  # Report
            result = call_backend(REPORT_ENDPOINT, selected_lang, files)
        elapsed = time.time() - start

    st.markdown(
        f"<div class='kpi'>📄 <b>File</b>: {filename_display} &nbsp;&nbsp; ⏱️ <b>Time</b>: {elapsed:.2f}s</div>",
        unsafe_allow_html=True,
    )
    st.markdown("\n")

    # ------------------------------
    # Handle PDF (report endpoint)
    # ------------------------------
    if mode == "Report":
        if "_raw" in result and isinstance(result.get("_raw"), (bytes, bytearray)):
            st.success("✅ Report generated successfully.")
            st.download_button(
                label="📄 Download Report",
                data=result["_raw"],
                file_name="code_review_report.pdf",
                mime=result.get("_headers", {}).get("content-type", "application/pdf") or "application/pdf",
            )
        else:
            st.error("Failed to generate report.")
            st.json(result)
        st.stop()


    # ------------------------------
    # Show analysis results
    # ------------------------------
    if "error" in result:
        st.error(result["error"])
        st.stop()

    if "ai_review" in result:
        with st.expander("🤖 AI Review", expanded=True):
            st.markdown(result["ai_review"])

    if "lint" in result or "complexity" in result:
        colL, colR = st.columns(2)
        with colL:
            st.subheader("Lint")
            lint = result.get("lint")
            if isinstance(lint, list):
                if len(lint) == 0:
                    st.success("No lint issues found.")
                else:
                    st.code("\n".join(lint), language="bash")
            elif isinstance(lint, str):
                st.code(lint, language="bash")
            else:
                st.info("No lint output.")
        with colR:
            st.subheader("Complexity")
            comp = result.get("complexity")
            if isinstance(comp, str):
                st.code(comp or "N/A", language="bash")
            else:
                st.info("No complexity output.")

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")
st.caption("© AI-Code-Reviewer — Streamlit UI. Uses your local FastAPI backend.")
