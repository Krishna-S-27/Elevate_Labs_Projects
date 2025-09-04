import tempfile

def save_code_to_tempfile(code, suffix):
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w+", encoding="utf-8") as temp:
        temp.write(code)
        temp.flush()
        return temp.name
