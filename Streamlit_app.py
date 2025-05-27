import streamlit as st
import tempfile
import subprocess
import os
import time
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="d CYBERVERSE METADATA INSPECTOR",
    page_icon="🏷️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    :root {
        --primary: #00f0ff;
        --secondary: #ff00ff;
        --dark: #0a0a12;
        --light: #f0f0ff;
        --accent: #7b2dff;
    }
    
    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
        background-color: var(--dark);
        color: var(--light);
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: var(--primary) !important;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
        letter-spacing: 2px;
    }
    
    .stApp {
        background-color: var(--dark);
        background-image: radial-gradient(circle at 20% 30%, rgba(123, 45, 255, 0.08) 0%, transparent 30%),
                          radial-gradient(circle at 80% 70%, rgba(0, 240, 255, 0.08) 0%, transparent 30%);
        overflow: hidden;
    }

    button, .stButton>button, .stFileUploader>div>div, .stCheckbox>div>div, input, textarea, select {
        outline: none !important;
        box-shadow: none !important;
        transition: none !important;
    }
    
    .stButton>button {
        border: 2px solid var(--primary) !important;
        background: rgba(10, 10, 20, 0.5) !important;
        color: var(--primary) !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        border-radius: 6px !important;
    }
    
    .stFileUploader>div>div {
        border: 2px dashed var(--primary) !important;
        background: rgba(10, 10, 20, 0.5) !important;
        color: var(--primary) !important;
        border-radius: 8px !important;
    }
    
    .stSuccess {
        background: rgba(0, 240, 255, 0.08) !important;
        border-left: 4px solid var(--primary) !important;
        border-radius: 0 8px 8px 0 !important;
    }
    
    .stError {
        background: rgba(255, 0, 100, 0.08) !important;
        border-left: 4px solid #ff0064 !important;
        border-radius: 0 8px 8px 0 !important;
    }
    
    .cyber-terminal {
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid var(--primary);
        border-radius: 8px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        color: var(--primary);
    }
    
    .metadata-line {
        padding: 8px 0;
        border-bottom: 1px solid rgba(0, 240, 255, 0.1);
    }
    
    .metadata-key {
        color: var(--secondary);
        font-weight: bold;
    }
    
    .metadata-value {
        color: var(--primary);
    }
    
    *:focus, *:active {
        outline: none !important;
        box-shadow: none !important;
    }
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        const size = Math.random() * 5 + 2;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}vw`;
        particle.style.top = `${Math.random() * 100}vh`;
        
        particle.style.animationDelay = `${Math.random() * 15}s`;
        
        document.body.appendChild(particle);
    }
});
</script>
""", unsafe_allow_html=True)

ascii_art = r"""
   ________  ______  __________ _    ____________  _____ ______
  / ____/\ \/ / __ )/ ____/ __ \ |  / / ____/ __ \/ ___// ____/
 / /      \  / __  / __/ / /_/ / | / / __/ / /_/ /\__ \/ __/   
/ /___    / / /_/ / /___/ _, _/| |/ / /___/ _, _/___/ / /___   
\____/   /_/_____/_____/_/ |_| |___/_____/_/ |_|/____/_____/   
                                                        
"""

st.markdown(f"""
<div style="text-align: center; margin-bottom: 30px;">
    <div style="color: var(--primary); font-size: 10px; opacity: 0.8; font-family: 'Courier New', monospace; white-space: pre; line-height: 1.2;">{ascii_art}</div>
    <h1 style="margin-top: -10px; font-size: 3em;">METADATA INSPECTOR</h1>
    <p style="color: var(--light); letter-spacing: 2px;">DIGITAL FORENSICS TOOL FOR DEEP FILE ANALYSIS</p>
    <div style="height: 2px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 10px auto; width: 50%;"></div>
</div>
""", unsafe_allow_html=True)

with stylable_container(
    key="uploader",
    css_styles="""
        {
            border: 2px dashed var(--primary);
            border-radius: 8px;
            padding: 40px;
            text-align: center;
            background: rgba(10, 10, 20, 0.5);
            margin-bottom: 30px;
        }
    """,
):
    uploaded_file = st.file_uploader("UPLOAD FILE FOR ANALYSIS", type=None, label_visibility="collapsed")

if uploaded_file:
    with st.spinner('ANALYZING DIGITAL FOOTPRINTS...'):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        with stylable_container(
            key="file_info",
            css_styles="""
                {
                    border-left: 4px solid var(--primary);
                    padding: 15px 20px;
                    background: rgba(0, 0, 0, 0.5);
                    margin-bottom: 20px;
                    border-radius: 0 8px 8px 0;
                }
            """,
        ):
            st.success(f"**FILE UPLOADED:** `{uploaded_file.name}` | **TYPE:** `{uploaded_file.type}`")
        
        try:
            result = subprocess.run(
                ["exiftool", tmp_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )


            if result.returncode != 0:
                with stylable_container(
                    key="error_container",
                    css_styles="""
                        {
                            border-left: 4px solid #ff0064;
                            padding: 15px 20px;
                            background: rgba(0, 0, 0, 0.5);
                            margin-bottom: 20px;
                            border-radius: 0 8px 8px 0;
                        }
                    """,
                ):
                    st.error(f"ANALYSIS FAILED: {result.stderr}")
            else:
                st.markdown("""
                <div style="margin: 30px 0;">
                    <h3 style="color: var(--secondary); text-align: center;">EXTRACTED METADATA</h3>
                    <div class="cyber-terminal">
                """, unsafe_allow_html=True)
                
                for line in result.stdout.strip().split("\n"):
                    if ": " in line:
                        key, value = line.split(": ", 1)
                        st.markdown(f"""
                        <div class="metadata-line">
                            <span class="metadata-key">{key.strip()}</span>: 
                            <span class="metadata-value">{value.strip()}</span>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("</div></div>", unsafe_allow_html=True)

        except Exception as e:
            with stylable_container(
                key="error_container",
                css_styles="""
                    {
                        border-left: 4px solid #ff0064;
                        padding: 15px 20px;
                        background: rgba(0, 0, 0, 0.5);
                        margin-bottom: 20px;
                        border-radius: 0 8px 8px 0;
                    }
                """,
            ):
                st.error(f"SYSTEM ERROR: {str(e)}")

        os.remove(tmp_path)

st.markdown("""
<div style="text-align: center; margin-top: 50px; color: var(--light); font-size: 0.8em; opacity: 0.7;">
    <div style="height: 1px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 20px auto; width: 30%;"></div>
    CYBERVERSE FORENSICS v3.0 | [SYSTEM: ONLINE] | [ANALYSIS: EXIFTOOL]
</div>
""", unsafe_allow_html=True)