import streamlit as st
from core.registry import LANGUAGE_REGISTRY

st.set_page_config(
    page_title="Level‑1 Code Validator & Formatter",
    layout="wide",
)

st.title("Level‑1 Code Validator & Formatter")
st.caption(
    "Deterministic validation & formatting. "
    "AI is intentionally external (Copilot / Claude / ChatGPT)."
)

# ---- Language Selection ----
language = st.selectbox(
    "Select Language",
    options=list(LANGUAGE_REGISTRY.keys())
)

# ---- Code Input ----
code = st.text_area(
    "Paste your code here",
    height=250,
    placeholder="Paste code here..."
)

# ---- Action Button ----
if st.button("Validate & Format"):
    if not code.strip():
        st.error("Please paste some code.")
    else:
        validator = LANGUAGE_REGISTRY[language]["validate"]
        formatter = LANGUAGE_REGISTRY[language]["format"]

        valid, errors = validator(code)

        if not valid:
            st.error("Validation errors found:")
            for err in errors:
                st.write(f"- {err}")
        else:
            formatted = formatter(code)
            st.success("Code is valid ✅")

            st.subheader("Formatted Code")
            st.code(formatted, language=language)

            st.info(
                "💡 Tip: Paste this formatted code into Copilot / Claude / ChatGPT "
                "for logic improvements and best practices."
            )
