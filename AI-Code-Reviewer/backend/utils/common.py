import subprocess
import shutil

def run_cmd(cmd, input_text=None):
    result = subprocess.run(cmd, input=input_text, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def which(tool):
    return shutil.which(tool)

def tool_or_msg(tool, install_msg):
    path = which(tool)
    if not path:
        return None, {"lint": [install_msg], "complexity": "N/A"}
    return path, None
