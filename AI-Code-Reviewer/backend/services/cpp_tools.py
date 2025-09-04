import json
from utils.common import run_cmd, which, tool_or_msg
from utils.file_handler import save_code_to_tempfile


def analyze(code, language=None):
    temp_path = save_code_to_tempfile(code, ".cpp")

    cpplint_path, msg = tool_or_msg(
        "cpplint",
        "cpplint not found. Install with: pip install cpplint"
    )
    lint_list = []
    if not msg:
        rc, out, err = run_cmd([cpplint_path, temp_path])
        if err:
            for line in err.splitlines():
                lint_list.append(line.strip())
    else:
        lint_list.append(msg)

    lizard_path, msg2 = tool_or_msg(
        "lizard",
        "lizard not found. Install with: pip install lizard"
    )
    complexity_summary = "N/A"
    if not msg2:
        rc, out, err = run_cmd([lizard_path, "-C", "10", temp_path])
        if rc == 0:
            complexity_summary = out.strip() or "No complexity issues"
        else:
            complexity_summary = "Lizard error: " + (err or "unknown error")
    else:
        complexity_summary = msg2

    return {"lint": lint_list, "complexity": complexity_summary}


def format_code(code, language=None):
    return {
        "original": code,
        "formatted": code,
        "note": "C++ formatting not implemented (consider clang-format)."
    }
