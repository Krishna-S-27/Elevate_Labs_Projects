from utils.file_handler import save_code_to_tempfile
from services.ai_reviewer import run_ai_reviewer

def analyze(code, language="go"):
    save_code_to_tempfile(code, ".go")

    ai_review = run_ai_reviewer(code, language="Go")
    return {"ai_review": ai_review}


def format_code(code, language="go"):
    ai_review = run_ai_reviewer(
        f"Please reformat this Go code according to idiomatic Go style (gofmt/goimports):\n\n{code}",
        language="Go"
    )
    return {"ai_review": ai_review}
