import streamlit as st
from scan_engine import handle_file

from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="Cloud DLP Scanner", layout="centered")

st.title("🔐 Data Leak Detection")
st.markdown("Upload a `.txt`, `.pdf`, or `.docx` file to scan for sensitive data.")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

if uploaded_file:
    with st.spinner("Scanning file..."):
        result = handle_file(uploaded_file.read(), uploaded_file.name)

    if result["status"] == "unsafe":
        st.error("❌ Sensitive info found!")
        for item in result["findings"]:
            st.write(f"- **{item['entity_type']}** → `{item['text']}` (Score: {round(item['score'], 2)})")
    else:
        st.success("✅ No sensitive data found!")
        st.markdown(f"[🔗 View uploaded file in Google Drive]({result['url']})", unsafe_allow_html=True)
