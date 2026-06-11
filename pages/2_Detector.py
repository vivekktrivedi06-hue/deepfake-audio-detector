import streamlit as st
import joblib
import numpy as np
import time
from src.feature_extraction import extract_features

st.set_page_config(
    page_title="Detector | Deepfake Audio",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Authentication Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.switch_page("app.py")

# Load Model Safely
@st.cache_resource
def load_model():
    return joblib.load("models/deepfake_model.pkl")

model = load_model()

# Premium SaaS UI Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: #f8fafc !important;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .page-header {
        animation: slideUp 0.5s ease-out forwards;
        margin-bottom: 32px;
    }
    
    .page-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }
    
    .page-subtitle {
        color: #64748b;
        font-size: 1.05rem;
    }

    /* Custom Upload Box styling applied to native component via wrapper */
    .upload-wrapper {
        background: #ffffff;
        border: 2px dashed #cbd5e1;
        border-radius: 16px;
        padding: 16px;
        transition: all 0.3s ease;
        animation: slideUp 0.6s ease-out forwards;
        margin-bottom: 24px;
    }
    .upload-wrapper:hover {
        border-color: #3b82f6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
    }

    /* Result Cards */
    .result-container {
        border-radius: 16px;
        padding: 32px;
        margin-top: 24px;
        animation: slideUp 0.5s ease-out forwards;
        border: 1px solid;
    }
    
    .card-real {
        background: #f0fdf4;
        border-color: #bbf7d0;
    }
    
    .card-fake {
        background: #fef2f2;
        border-color: #fecaca;
    }

    .result-title {
        font-size: 1.5rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }
    
    .title-real { color: #15803d; }
    .title-fake { color: #b91c1c; }

    .result-desc {
        color: #475569;
        font-size: 0.95rem;
        margin-bottom: 24px;
    }

    .confidence-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 8px;
    }

    .confidence-score {
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .score-real { color: #16a34a; }
    .score-fake { color: #dc2626; }

    /* Button Override */
    div.stButton > button {
        background: #3b82f6 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        background: #2563eb !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(59, 130, 246, 0.2) !important;
    }
    
    /* Progress Bar Override */
    .stProgress > div > div > div > div {
        background-color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <div class="page-title">Audio Analysis Console</div>
    <div class="page-subtitle">Upload audio files (.wav, .mp3) for instant forensic verification.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="upload-wrapper">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drop audio file here", type=["wav", "mp3"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    st.audio(uploaded_file)
    st.markdown('<br>', unsafe_allow_html=True)

    if st.button("Execute Deep Analysis Pipeline"):
        # Save temp file
        with open("temp.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Extracting features and classifying anomalies..."):
            time.sleep(0.5) # Slight delay for smooth UI transition perception
            features = extract_features("temp.wav")

            if features is not None:
                pred = model.predict([features])[0]
                conf = np.max(model.predict_proba([features])) * 100

                if pred == 1: # FAKE
                    st.markdown(f"""
                    <div class="result-container card-fake">
                        <div class="result-title title-fake">🚨 Synthetic Audio Detected</div>
                        <div class="result-desc">The structural markers of this audio heavily match known generative AI patterns and synthetic speech models.</div>
                        <div class="confidence-label">Confidence Matrix</div>
                        <div class="confidence-score score-fake">{conf:.1f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(conf))
                else: # REAL
                    st.markdown(f"""
                    <div class="result-container card-real">
                        <div class="result-title title-real">✅ Authentic Human Audio</div>
                        <div class="result-desc">Acoustic analysis indicates natural vocal cord vibration and normal ambient variance. No synthetic artifacts detected.</div>
                        <div class="confidence-label">Confidence Matrix</div>
                        <div class="confidence-score score-real">{conf:.1f}%</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.progress(int(conf))
            else:
                st.error("Processing Error: Could not extract features from the audio file.")