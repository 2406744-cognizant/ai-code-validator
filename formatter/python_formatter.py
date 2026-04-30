import black

def format_python(code: str):
    return black.format_str(code, mode=black.FileMode())