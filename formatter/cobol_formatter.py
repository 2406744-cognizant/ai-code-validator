def format_cobol(code: str):
    return "\n".join(
        line.strip().upper() for line in code.splitlines()
    )