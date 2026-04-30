from core.registry import LANGUAGE_REGISTRY


def main():
    print("=== Level‑1 Code Validator & Formatter ===\n")

    print("Supported languages:")
    for lang in LANGUAGE_REGISTRY:
        print(f"- {lang}")

    language = input("\nSelect language: ").strip().lower()

    if language not in LANGUAGE_REGISTRY:
        print("\n❌ Language not supported.")
        return

    print("\nPaste your code below.")
    print("Press Ctrl + D (Linux/macOS) when done.\n")

    code = ""
    try:
        while True:
            code += input() + "\n"
    except EOFError:
        pass

    if not code.strip():
        print("\n❌ No code provided.")
        return

    validator = LANGUAGE_REGISTRY[language]["validate"]
    formatter = LANGUAGE_REGISTRY[language]["format"]

    valid, errors = validator(code)

    if not valid:
        print("\n❌ Validation Errors:")
        for err in errors:
            print(f"- {err}")
        return

    formatted_code = formatter(code)

    print("\n✅ Code is valid.\n")
    print("✅ Formatted Code:\n")
    print(formatted_code)

    print(
        "\n💡 Tip: Paste this formatted code into Copilot / Claude / ChatGPT "
        "for logic improvement and best-practice suggestions."
    )


if __name__ == "__main__":
    main()