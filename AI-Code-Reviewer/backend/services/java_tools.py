from utils.file_handler import save_code_to_tempfile
from services.ai_reviewer import run_ai_reviewer

def analyze(code, language="java"):
    save_code_to_tempfile(code, ".java")
    ai_review = run_ai_reviewer(code, language="Java")
    return {"ai_review": ai_review}


def format_code(code, language="java"):
    ai_review = run_ai_reviewer(
        f"Please reformat this Java code according to Google Java Style Guide:\n\n{code}",
        language="Java"
    )
    return {"ai_review": ai_review}
