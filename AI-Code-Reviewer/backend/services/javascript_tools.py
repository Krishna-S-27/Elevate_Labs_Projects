import json
from utils.common import run_cmd, which, tool_or_msg


def analyze(code, language=None):
    """
    Analyze JavaScript/TypeScript code using ESLint via stdin.
    Avoids 'outside of base path' issues with temp files.
    """

    # Decide parser
    ext = ".ts" if language == "typescript" else ".js"

    # Ensure ESLint is available
    eslint_path, msg = tool_or_msg(
        "eslint",
        "ESLint not found on PATH. Install Node + ESLint (npm install -D eslint)."
    )
    if msg:
        return {"lint": [msg], "complexity": "N/A"}

    # Run ESLint with stdin
    code_rc, out, err = run_cmd([
        eslint_path,
        "-c", "eslint.config.mjs",
        "-f", "json",
        "--stdin",
        "--stdin-filename", f"dummy{ext}"   # tells ESLint the file type
    ], input_text=code)

    lint_list = []
    if out:
        try:
            data = json.loads(out)
            for file_res in data:
                for m in file_res.get("messages", []):
                    rule = m.get("ruleId") or "rule"
                    line = str(m.get("line") or 1)
                    col = str(m.get("column") or 1)
                    txt = m.get("message") or ""
                    lint_list.append(f"{line}:{col}: {rule} {txt}")
        except Exception as e:
            lint_list.append("ESLint parse error: " + str(e))
    elif err:
        lint_list.append("ESLint error: " + err)

    complexity_summary = "ESLint run completed"
    return {"lint": lint_list, "complexity": complexity_summary}


def format_code(code, language=None):
    """
    Format JavaScript/TypeScript code using Prettier.
    """

    prettier_path = which("prettier")
    if not prettier_path:
        return {
            "original": code,
            "formatted": code,
            "note": "Prettier not found on PATH. Install with: npm install -D prettier"
        }

    parser = "typescript" if language == "typescript" else "babel"

    rc, out, err = run_cmd(
        [prettier_path, "--parser", parser],
        input_text=code
    )

    if rc == 0 and out:
        return {"original": code, "formatted": out}
    return {
        "original": code,
        "formatted": code,
        "note": "Prettier failed: " + (err or "unknown error")
    }
