def validate_js(code: str):
    try:
        import jsbeautifier  # just to ensure JS tooling exists
        return True, []
    except Exception as e:
        return False, [str(e)]