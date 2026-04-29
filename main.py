from validators.python_validator import validate_python
from formatter.python_formatter import format_python
from ai.ai_review import ai_review

language = input("Language: ").lower()
print("Paste code (Ctrl+D to finish):")

code = ""
while True:
    try:
        code += input() + "\n"
    except EOFError:
        break

valid, errors = validate_python(code)

if valid:
    formatted = format_python(code)
    print("\n✅ Formatted Code:\n", formatted)
else:
    print("\n❌ Errors:", errors)

print("\n🤖 AI Review:")
print(ai_review(language, code))
