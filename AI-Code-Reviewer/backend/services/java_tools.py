from utils.file_handler import save_code_to_tempfile
from services.ai_reviewer import run_ai_reviewer

def analyze(code, language="java"):
    # Save to temp file just for workflow consistency (optional)
    save_code_to_tempfile(code, ".java")

    # AI review only
    ai_review = run_ai_reviewer(code, language="Java")
    return {"ai_review": ai_review}


def format_code(code, language="java"):
    # AI-powered formatting suggestions
    ai_review = run_ai_reviewer(
        f"Please reformat this Java code according to Google Java Style Guide:\n\n{code}",
        language="Java"
    )
    return {"ai_review": ai_review}
