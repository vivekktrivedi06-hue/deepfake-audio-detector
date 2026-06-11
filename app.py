import streamlit as st
import re

st.set_page_config(
    page_title="Login | Deepfake Detector",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Premium Light Theme & Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: radial-gradient(circle at 50% 0%, #ffffff 0%, #f3f4f6 100%) !important;
    }
    
    [data-testid="stSidebar"] {
        display: none;
    }
    
    @keyframes fadeSlideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
        100% { transform: translateY(0px); }
    }

    .login-container {
        animation: fadeSlideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
        max-width: 450px;
        margin: 60px auto;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(229, 231, 235, 0.8);
        border-radius: 24px;
        padding: 48px 40px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
    }
    
    .brand-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 16px;
        animation: float 4s ease-in-out infinite;
    }
    
    .login-title {
        text-align: center;
        font-size: 1.75rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }
    
    .login-subtitle {
        text-align: center;
        font-size: 0.95rem;
        color: #6b7280;
        margin-bottom: 32px;
    }

    /* Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px 24px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2) !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# If already logged in, redirect
if st.session_state["authenticated"]:
    st.switch_page("pages/1_Info.py")

# Login UI
st.markdown('<div class="login-container"><div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="brand-icon">🛡️</div>', unsafe_allow_html=True)
st.markdown('<div class="login-title">Welcome Back</div>', unsafe_allow_html=True)
st.markdown('<div class="login-subtitle">Sign in to access the verification console.</div>', unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("Work Email", placeholder="name@company.com")
    password = st.text_input("Password", type="password", placeholder="••••••••")
    submit = st.form_submit_button("Authenticate")
    
    if submit:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not email or not password:
            st.error("Please fill in both email and password.")
        elif not re.match(email_regex, email):
            st.error("Please enter a valid email format.")
        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")
        else:
            # Simple validation passed
            st.session_state["authenticated"] = True
            st.success("Authentication successful! Redirecting...")
            st.switch_page("pages/1_Info.py")

st.markdown('</div></div>', unsafe_allow_html=True)