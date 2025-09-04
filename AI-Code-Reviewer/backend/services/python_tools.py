import subprocess
import tempfile

def analyze(code, language=None):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp1:
        temp1.write(code.encode("utf-8"))
        temp1.flush()
        flake = subprocess.run(
            ["flake8", temp1.name, "--format=%(row)d:%(col)d: %(code)s %(text)s"],
            capture_output=True, text=True
        )
        lint_issues = flake.stdout.strip().split("\n") if flake.stdout else []

    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp2:
        temp2.write(code.encode("utf-8"))
        temp2.flush()
        r = subprocess.run(
            ["radon", "cc", temp2.name, "-j"],
            capture_output=True, text=True
        )
        complexity = r.stdout.strip()

    return {"lint": lint_issues, "complexity": complexity}

def format_code(code, language=None):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w+") as temp:
        temp.write(code)
        temp.flush()
        subprocess.run(["black", temp.name], capture_output=True, text=True)
        temp.seek(0)
        formatted = temp.read()
    return {"original": code, "formatted": formatted}
