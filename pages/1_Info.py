import streamlit as st

st.set_page_config(
    page_title="Platform Info | Deepfake Detector",
    page_icon="ℹ️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Authentication Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.switch_page("app.py")

# Premium SaaS Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: #f8fafc !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    @keyframes cascadeFade {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .header-section {
        animation: cascadeFade 0.6s ease-out both;
        margin-bottom: 40px;
        text-align: center;
        padding-top: 20px;
    }

    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 12px;
        letter-spacing: -0.02em;
    }

    .subtitle {
        font-size: 1.1rem;
        color: #64748b;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    .info-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: cascadeFade 0.6s ease-out both;
    }
    
    .info-card:nth-child(2) { animation-delay: 0.1s; }
    .info-card:nth-child(3) { animation-delay: 0.2s; }
    .info-card:nth-child(4) { animation-delay: 0.3s; }

    .info-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.05);
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 16px;
    }

    .icon-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 48px;
        height: 48px;
        border-radius: 12px;
        font-size: 1.5rem;
    }
    
    .blue-icon { background: #eff6ff; color: #3b82f6; }
    .purple-icon { background: #faf5ff; color: #a855f7; }
    .green-icon { background: #f0fdf4; color: #22c55e; }

    .card-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin: 0;
    }

    .card-text {
        color: #475569;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Button Override */
    div.stButton > button {
        background: #0f172a !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        border: none !important;
        transition: all 0.2s ease !important;
        margin-top: 24px;
    }
    div.stButton > button:hover {
        background: #334155 !important;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-section">
    <div class="title">System Architecture</div>
    <div class="subtitle">An overview of our enterprise-grade audio analysis and synthetic media detection pipeline.</div>
</div>
""", unsafe_allow_html=True)

# Section 1
st.markdown("""
<div class="info-card">
    <div class="card-header">
        <div class="icon-wrapper blue-icon">🧠</div>
        <h3 class="card-title">Core Technology</h3>
    </div>
    <div class="card-text">
        Powered by an advanced <strong>Random Forest Machine Learning</strong> model, the system analyzes hundreds of unique audio dimensions. It processes spectral layouts, rhythm, and tone consistency to separate genuine human voices from generated fakes.
    </div>
</div>
""", unsafe_allow_html=True)

# Section 2
st.markdown("""
<div class="info-card">
    <div class="card-header">
        <div class="icon-wrapper purple-icon">📊</div>
        <h3 class="card-title">Feature Extraction</h3>
    </div>
    <div class="card-text">
        We utilize <strong>Librosa</strong> to map raw audio into detailed mathematical features. By examining Mel-frequency cepstral coefficients (MFCCs), chroma, and spectral contrast, we identify unnatural digital artifacts invisible to the human ear.
    </div>
</div>
""", unsafe_allow_html=True)

# Section 3
st.markdown("""
<div class="info-card">
    <div class="card-header">
        <div class="icon-wrapper green-icon">💼</div>
        <h3 class="card-title">Enterprise Use Cases</h3>
    </div>
    <div class="card-text">
        Deployed for identity verification, fraud prevention, and media authenticity. Ensure that secure phone commands, executive voice notes, and customer service authentications are genuinely human.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Proceed to Detection Console →", use_container_width=True):
        st.switch_page("pages/2_Detector.py")