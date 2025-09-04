from fastapi import APIRouter, UploadFile, File, Form
from services import python_tools, javascript_tools, java_tools, cpp_tools, go_tools, reporter

router = APIRouter(prefix="/api", tags=["Code Analysis"])

# Tool mapping
ANALYZE_MAP = {
    "python": python_tools,
    "javascript": javascript_tools,
    "js": javascript_tools,
    "typescript": javascript_tools,
    "java": java_tools,
    "cpp": cpp_tools,
    "c++": cpp_tools,
    "c": cpp_tools,
    "go": go_tools,
}

@router.post("/analyze")
async def analyze_code(language: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    code = content.decode("utf-8")

    lang = language.lower()
    tool = ANALYZE_MAP.get(lang)
    if not tool:
        return {"error": "Language " + language + " not supported yet."}

    return tool.analyze(code, language=lang)

@router.post("/format")
async def format_code(language: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    code = content.decode("utf-8")

    lang = language.lower()
    tool = ANALYZE_MAP.get(lang)
    if not tool:
        return {"error": "Language " + language + " not supported yet."}

    return tool.format_code(code, language=lang)

from fastapi.responses import FileResponse
import time
import os

@router.post("/report")
async def generate_report(language: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    code = content.decode("utf-8")

    # Generate report path with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join("backend", "reports", f"code_review_report_{language}_{timestamp}.pdf")

    # Call your reporter to actually generate the file
    reporter.create_pdf_report(language, code, report_path)

    # Return the file as a downloadable PDF
    return FileResponse(
        path=report_path,
        filename=f"code_review_report_{language}.pdf",
        media_type="application/pdf"
    )
