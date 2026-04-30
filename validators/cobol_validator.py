def validate_cobol(code: str):
    errors = []
    upper = code.upper()

    if "IDENTIFICATION DIVISION" not in upper:
        errors.append("Missing IDENTIFICATION DIVISION")

    if "PROCEDURE DIVISION" not in upper:
        errors.append("Missing PROCEDURE DIVISION")

    if "STOP RUN." not in upper:
        errors.append("Missing STOP RUN statement")

    return len(errors) == 0, errors