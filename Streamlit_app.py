import streamlit as st
import tempfile
import subprocess
import os

# Custom CSS for hacker-themed UI
with open("assets/cyberverse.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("## 🧠 CYBERVERSE METADATA INSPECTOR")
st.markdown("Upload any file (image, PDF, audio, etc.) to extract detailed metadata using **ExifTool**.")

uploaded_file = st.file_uploader("📤 Upload a file", type=None)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.success(f"✅ File uploaded: `{uploaded_file.name}`")
    st.markdown("---")

    try:
        result = subprocess.run(
            ["exiftool", tmp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True  # Important for Windows
        )

        if result.returncode != 0:
            st.error(f"❌ Error: {result.stderr}")
        else:
            st.markdown("### 🔍 Extracted Metadata")
            for line in result.stdout.strip().split("\n"):
                if ": " in line:
                    key, value = line.split(": ", 1)
                    st.write(f"**{key.strip()}**: {value.strip()}")

    except Exception as e:
        st.error(f"❌ Failed to run exiftool: {e}")

    os.remove(tmp_path)
