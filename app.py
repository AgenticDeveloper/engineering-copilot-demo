import streamlit as st

# Title and description
st.set_page_config(page_title="Engineering Copilot", layout="wide")
st.title("🛠️ Engineering Copilot Demo")
st.markdown("""
Ask questions about engineering SOPs, deviation handling, or process documents.
This demo simulates a GenAI-powered assistant retrieving answers from technical files.
""")

# User input
query = st.text_input("🔍 Ask a question (e.g., 'What is the OQ process for the XYZ reactor?')")

# Sample simulated response
if query:
    st.markdown("#### 🤖 Copilot Answer:")
    st.success(f"""
Based on historical OQ documentation and deviation reports for 'XYZ reactor':
- The OQ protocol includes sensor calibration, alarm verification, and flow rate tests.
- Common deviations include inaccurate temperature probes and missed log entries.
- Suggested CAPA: pre-validation checklist and sensor double-check routine.

_Source: XYZ_OQ_Protocol_2023.pdf, DeviationReport_XYZ_March2024.docx_
""")
    st.markdown("---")
    st.markdown("📎 **References**")
    st.write("- `XYZ_OQ_Protocol_2023.pdf`")
    st.write("- `DeviationReport_XYZ_March2024.docx`")

# Footer
st.sidebar.markdown("Developed for GSK demo | Sigmoid |
