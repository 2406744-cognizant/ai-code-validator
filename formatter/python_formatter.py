import black

def format_python(code):
    return black.format_str(code, mode=black.FileMode())