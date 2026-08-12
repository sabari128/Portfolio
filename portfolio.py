import streamlit as st
import streamlit.components.v1 as components
import PyPDF2
from pathlib import Path
import base64
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Sabarinathan - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS — premium dark glassmorphism theme with animated aurora background
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --grad: linear-gradient(120deg, #22d3ee 0%, #818cf8 45%, #f472b6 100%);
        --grad-soft: linear-gradient(120deg, #38bdf8 0%, #818cf8 55%, #e879f9 100%);
        --primary: #818cf8;
        --accent: #f472b6;
        --cyan: #22d3ee;
        --ink: #e2e8f0;
        --muted: #94a3b8;
        --glass: rgba(255,255,255,0.05);
        --glass-brd: rgba(255,255,255,0.10);
    }

    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

    /* Animated aurora background */
    .stApp {
        background:
            radial-gradient(1000px 600px at 12% -8%, rgba(34,211,238,0.18), transparent 60%),
            radial-gradient(900px 620px at 105% 12%, rgba(244,114,182,0.16), transparent 60%),
            radial-gradient(1000px 700px at 50% 120%, rgba(129,140,248,0.20), transparent 60%),
            linear-gradient(160deg, #060814 0%, #0b1024 45%, #0a0f22 100%);
        background-attachment: fixed;
        color: var(--ink);
    }
    .stApp::before {
        content: ""; position: fixed; inset: 0; z-index: 0; pointer-events: none;
        background-image:
            linear-gradient(rgba(255,255,255,0.028) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.028) 1px, transparent 1px);
        background-size: 46px 46px;
        mask-image: radial-gradient(ellipse at 50% 0%, #000 40%, transparent 85%);
    }
    .block-container { position: relative; z-index: 1; }

    /* Base typography colors on dark */
    .stApp p, .stApp li, .stApp span, .stApp label { color: var(--ink); }
    h1, h2, h3, h4, h5 { font-family: 'Space Grotesk', 'Poppins', sans-serif; letter-spacing: .2px; }

    /* Animations */
    @keyframes fadeUp { from { opacity: 0; transform: translateY(26px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes floaty { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-9px); } }
    @keyframes shine  { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes glowPulse {
        0%,100% { box-shadow: 0 0 0 rgba(129,140,248,0.0), 0 22px 55px rgba(129,140,248,0.30); }
        50%     { box-shadow: 0 0 42px rgba(34,211,238,0.35), 0 22px 60px rgba(244,114,182,0.30); }
    }

    /* Glass cards */
    .card {
        background: var(--glass);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 14px 40px rgba(0,0,0,0.35);
        margin: 1rem 0;
        border: 1px solid var(--glass-brd);
        backdrop-filter: blur(16px) saturate(140%);
        -webkit-backdrop-filter: blur(16px) saturate(140%);
        transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease;
        animation: fadeUp .6s ease both;
        position: relative; overflow: hidden;
    }
    .card::after {
        content: ""; position: absolute; inset: 0; border-radius: 20px; padding: 1px; pointer-events: none;
        background: linear-gradient(135deg, rgba(34,211,238,0.5), rgba(129,140,248,0.2), rgba(244,114,182,0.5));
        -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
        -webkit-mask-composite: xor; mask-composite: exclude; opacity: 0; transition: opacity .35s ease;
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 26px 60px rgba(34,211,238,0.18), 0 10px 30px rgba(244,114,182,0.14);
        border-color: rgba(129,140,248,0.35);
    }
    .card:hover::after { opacity: 1; }

    /* Force legacy inline text colors to be readable on dark glass */
    .card p, .card li, .card ul, .card > span { color: #cbd5e1 !important; }
    .card p strong, .card li strong { color: #f1f5f9 !important; }
    .card h2, .card h3, .card h4 {
        background: var(--grad-soft); -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent; color: transparent !important;
    }
    .contact-info h2, .contact-info p { color: #ffffff !important; -webkit-text-fill-color: #ffffff; }

    /* Hero header */
    .profile-header {
        text-align: center;
        padding: clamp(2.4rem, 6vw, 4.4rem) 1.5rem;
        background:
            radial-gradient(700px 260px at 50% -20%, rgba(34,211,238,0.28), transparent 70%),
            linear-gradient(135deg, rgba(129,140,248,0.16), rgba(244,114,182,0.14));
        border: 1px solid var(--glass-brd);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        color: white;
        border-radius: 26px;
        margin-bottom: 2rem;
        animation: glowPulse 6s ease-in-out infinite, fadeUp .7s ease both;
        position: relative; overflow: hidden;
    }
    .profile-avatar {
        width: 118px; height: 118px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(34,211,238,0.25), rgba(244,114,182,0.25));
        border: 2px solid rgba(255,255,255,0.5);
        display: flex; align-items: center; justify-content: center;
        font-size: 3.1rem; margin: 0 auto 1rem auto;
        animation: floaty 4s ease-in-out infinite;
        backdrop-filter: blur(6px);
        box-shadow: 0 0 34px rgba(34,211,238,0.4);
    }
    .profile-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.1rem, 6.4vw, 3.6rem);
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #e0f2fe, #a5b4fc, #f9a8d4);
        -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0 6px 30px rgba(129,140,248,0.35);
    }
    .profile-title {
        font-size: clamp(0.95rem, 2.5vw, 1.35rem);
        font-weight: 300;
        color: #cbd5e1;
    }

    /* Hero status pill + tech chips */
    .status-pill {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 6px 16px; margin-bottom: 1.2rem;
        background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.4);
        color: #6ee7b7 !important; border-radius: 30px; font-size: .82rem; font-weight: 600;
    }
    .status-pill .dot {
        width: 9px; height: 9px; border-radius: 50%; background: #34d399;
        box-shadow: 0 0 0 0 rgba(52,211,153,0.7); animation: ping 1.6s ease-in-out infinite;
    }
    @keyframes ping { 0% { box-shadow: 0 0 0 0 rgba(52,211,153,0.6); } 70%,100% { box-shadow: 0 0 0 8px rgba(52,211,153,0); } }
    .hero-chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.55rem; margin-top: 1.3rem; }
    .hero-chips span {
        padding: 6px 14px; font-size: .82rem; font-weight: 500; color: #dbeafe !important;
        background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 30px;
        backdrop-filter: blur(6px);
    }
    .social-links { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.9rem; margin-top: 1.8rem; }
    .social-btn {
        padding: 11px 26px;
        background: rgba(255,255,255,0.06);
        color: #e2e8f0;
        text-decoration: none;
        border-radius: 30px;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.16);
        backdrop-filter: blur(8px);
        transition: all .3s ease;
        display: inline-block;
    }
    .social-btn:hover {
        transform: translateY(-3px) scale(1.04);
        background: var(--grad-soft);
        color: #0b1024;
        box-shadow: 0 10px 28px rgba(34,211,238,0.35);
        border-color: transparent;
    }

    /* Section headers */
    .section-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(1.5rem, 4vw, 2.1rem);
        font-weight: 700;
        background: var(--grad-soft);
        -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
        margin: 2.2rem 0 1rem 0;
        padding-bottom: 0.55rem;
        display: inline-block;
        position: relative;
    }
    .section-header::after {
        content: ""; position: absolute; left: 0; bottom: 0; height: 3px; width: 100%;
        background: var(--grad); border-radius: 3px; box-shadow: 0 0 14px rgba(34,211,238,0.5);
    }

    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: rgba(129,140,248,0.12);
        color: #dbeafe !important;
        padding: 8px 18px;
        border-radius: 30px;
        margin: 5px;
        font-size: 0.86rem;
        font-weight: 500;
        border: 1px solid rgba(129,140,248,0.35);
        transition: all .25s ease;
    }
    .skill-tag:hover {
        transform: translateY(-3px) scale(1.05);
        background: var(--grad-soft);
        color: #0b1024 !important;
        border-color: transparent;
        box-shadow: 0 8px 20px rgba(34,211,238,0.35);
    }

    /* Stat cards */
    .stat-card {
        background: var(--glass);
        border: 1px solid var(--glass-brd);
        backdrop-filter: blur(14px);
        color: white;
        padding: 1.6rem 1rem;
        border-radius: 18px;
        text-align: center;
        transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease;
        animation: fadeUp .6s ease both;
    }
    .stat-card:hover {
        transform: translateY(-8px);
        border-color: rgba(34,211,238,0.5);
        box-shadow: 0 18px 40px rgba(34,211,238,0.22);
    }
    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(1.9rem, 5vw, 2.8rem); font-weight: 700; margin-bottom: 0.3rem;
        background: var(--grad); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stat-label { font-size: 0.95rem; color: #cbd5e1; }

    /* Timeline */
    .timeline-item {
        border-left: 2px solid rgba(129,140,248,0.5);
        padding-left: 1.8rem; margin-left: 0.6rem; padding-bottom: 1.7rem; position: relative;
    }
    .timeline-item::before {
        content: ''; position: absolute; left: -9px; top: 4px;
        width: 15px; height: 15px; background: var(--grad); border: 2px solid #0b1024;
        border-radius: 50%; box-shadow: 0 0 0 4px rgba(34,211,238,0.20), 0 0 16px rgba(244,114,182,0.6);
    }

    /* Contact info */
    .contact-info {
        background: linear-gradient(135deg, rgba(34,211,238,0.14), rgba(244,114,182,0.14));
        border: 1px solid var(--glass-brd);
        backdrop-filter: blur(14px);
        color: white; padding: 2rem; border-radius: 20px; text-align: center;
        box-shadow: 0 16px 40px rgba(0,0,0,0.35);
    }

    /* Download button */
    .download-btn {
        background: var(--grad);
        background-size: 200% 200%;
        animation: shine 6s ease infinite;
        color: #0b1024;
        padding: 14px 38px; border-radius: 30px; text-decoration: none;
        font-weight: 700; font-size: 1.05rem; display: inline-block;
        transition: all .3s ease; border: none; cursor: pointer;
        box-shadow: 0 10px 30px rgba(129,140,248,0.35);
    }
    .download-btn:hover { transform: translateY(-3px) scale(1.04); box-shadow: 0 16px 40px rgba(34,211,238,0.5); }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0f22 0%, #0d1330 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    [data-testid="stSidebar"] .stRadio label {
        border-radius: 12px; padding: 6px 10px; transition: background .2s ease;
    }
    [data-testid="stSidebar"] .stRadio label:hover { background: rgba(129,140,248,0.12); }

    /* Sidebar mini profile + facts */
    .side-card {
        text-align: center; padding: 1.2rem 1rem; border-radius: 18px;
        background: linear-gradient(135deg, rgba(34,211,238,0.12), rgba(244,114,182,0.12));
        border: 1px solid rgba(255,255,255,0.12); backdrop-filter: blur(10px);
    }
    .side-avatar {
        width: 62px; height: 62px; margin: 0 auto 0.6rem; border-radius: 50%;
        display: flex; align-items: center; justify-content: center; font-size: 1.7rem;
        background: linear-gradient(135deg, rgba(34,211,238,0.3), rgba(244,114,182,0.3));
        border: 2px solid rgba(255,255,255,0.4); box-shadow: 0 0 22px rgba(34,211,238,0.4);
    }
    .side-name { font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 1.15rem; color: #f1f5f9 !important; }
    .side-role { font-size: .82rem; color: #cbd5e1 !important; margin-top: 2px; }
    .side-loc  { font-size: .78rem; color: #94a3b8 !important; margin-top: 6px; }

    .side-status {
        display: flex; align-items: center; justify-content: center; gap: 8px;
        margin: 1rem 0; padding: 8px 12px; border-radius: 30px; font-size: .8rem; font-weight: 600;
        background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.4); color: #6ee7b7 !important;
    }
    .side-status .s-dot { width: 9px; height: 9px; border-radius: 50%; background: #34d399; animation: ping 1.6s ease-in-out infinite; }

    .side-facts { display: flex; flex-direction: column; gap: 8px; }
    .side-facts .fact {
        display: flex; justify-content: space-between; align-items: center;
        padding: 9px 13px; border-radius: 12px;
        background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
        transition: all .25s ease;
    }
    .side-facts .fact:hover { border-color: rgba(34,211,238,0.5); transform: translateX(3px); }
    .side-facts .fact span { font-size: .8rem; color: #94a3b8 !important; }
    .side-facts .fact b { font-size: .82rem; color: #e2e8f0 !important; }

    .side-connect { display: flex; gap: 10px; }
    .side-connect a {
        flex: 1; text-align: center; padding: 10px 0; border-radius: 12px; text-decoration: none;
        font-weight: 700; font-size: .9rem; color: #e2e8f0 !important;
        background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); transition: all .25s ease;
    }
    .side-connect a:hover {
        background: var(--grad-soft); color: #0b1024 !important; border-color: transparent;
        transform: translateY(-3px); box-shadow: 0 8px 20px rgba(34,211,238,0.35);
    }

    /* Footer */
    .footer { text-align: center; padding: 2rem; color: var(--muted); margin-top: 3rem; }
    .footer p { color: var(--muted) !important; }

    /* Responsive tweaks */
    @media (max-width: 768px) {
        .card { padding: 1.4rem; }
        .social-links { gap: 0.6rem; }
        .social-btn { padding: 9px 18px; font-size: 0.9rem; }
        .profile-avatar { width: 92px; height: 92px; font-size: 2.5rem; }
    }

    /* Skill proficiency bars */
    .skill-row { margin-bottom: 1.15rem; }
    .skill-row-head { display: flex; justify-content: space-between; font-weight: 600; color: #e2e8f0 !important; margin-bottom: 7px; }
    .skill-row-head span { color: #e2e8f0 !important; }
    .skill-bar { background: rgba(255,255,255,0.07); border-radius: 30px; height: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.08); }
    .skill-bar > span {
        display: block; height: 100%; border-radius: 30px;
        background: var(--grad); box-shadow: 0 0 14px rgba(34,211,238,0.5);
        animation: growBar 1.3s cubic-bezier(.25,.8,.25,1) both;
    }
    @keyframes growBar { from { width: 0; } }

    /* Resume document view */
    .resume-doc h3 {
        margin: 1.4rem 0 0.4rem; font-size: 1.15rem;
        background: var(--grad-soft); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
    }
    .resume-doc .r-sub { color: var(--accent) !important; -webkit-text-fill-color: var(--accent); font-weight: 600; margin: 0.3rem 0 0.2rem; }
    .resume-doc p, .resume-doc li { color: #cbd5e1 !important; line-height: 1.7; }

    /* GitHub repo cards */
    .repo-card {
        flex: 1 1 220px; text-decoration: none; display: block;
        border: 1px solid rgba(255,255,255,0.10); border-radius: 16px;
        padding: 1.1rem; background: rgba(255,255,255,0.04); backdrop-filter: blur(10px); transition: all .3s ease;
    }
    .repo-card:hover { transform: translateY(-6px); border-color: rgba(34,211,238,0.5); box-shadow: 0 16px 34px rgba(34,211,238,0.20); }
    .repo-card h4 { margin: 0 0 .4rem; font-size: 1.05rem; background: var(--grad-soft); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
    .repo-card p { color: #94a3b8 !important; font-size: .88rem; margin: 0 0 .6rem; line-height: 1.5; }
    .repo-card .repo-lang { color: var(--cyan) !important; font-size: .78rem; font-weight: 600; }

    /* Streamlit widget theming */
    .stExpander, [data-testid="stExpander"] { border-radius: 14px; border: 1px solid rgba(255,255,255,0.08) !important; background: rgba(255,255,255,0.03); }
    .stTextInput input, .stTextArea textarea { color: #e2e8f0; }

    #MainMenu {visibility: hidden;}
    header[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)

# Function to read PDF resume
def read_resume_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Function to create download link for PDF
def get_pdf_download_link(file_path, link_text):
    try:
        with open(file_path, "rb") as f:
            bytes_data = f.read()
            b64 = base64.b64encode(bytes_data).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="Sabarinathan_Resume.pdf" class="download-btn">{link_text}</a>'
            return href
    except Exception as e:
        return f"Error: {str(e)}"

# Sidebar navigation
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🎯 Navigation")
    page = st.radio(
        "Navigation",
        ["🏠 Home", "💼 Experience", "🚀 Projects", "🛠️ Skills", "🏆 Certifications", "📄 Resume", "📬 Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="side-card">
        <div class="side-avatar">👨‍💻</div>
        <div class="side-name">Sabarinathan S</div>
        <div class="side-role">Software &amp; Automation Engineer</div>
        <div class="side-loc">📍 Salem, Tamil Nadu</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="side-status"><span class="s-dot"></span> Available for opportunities</div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Quick Facts")
    st.markdown("""
    <div class="side-facts">
        <div class="fact"><span>💼 Experience</span><b>2 Internships</b></div>
        <div class="fact"><span>🎓 CGPA</span><b>8.4 / 10</b></div>
        <div class="fact"><span>🤖 Focus</span><b>Automation · Python</b></div>
        <div class="fact"><span>🏆 Certs</span><b>UiPath · PL-500</b></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔗 Connect")
    st.markdown("""
    <div class="side-connect">
        <a href="https://linkedin.com/in/sabari12" target="_blank" title="LinkedIn">in</a>
        <a href="https://github.com/sabari128" target="_blank" title="GitHub">GH</a>
        <a href="mailto:sabarinathan1202s@gmail.com" title="Email">@</a>
        <a href="tel:+919342952824" title="Call">📞</a>
    </div>
    """, unsafe_allow_html=True)
    

# Main content based on navigation
if "Home" in page:
    # Profile Header
    st.markdown("""
    <div class="profile-header">
        <div class="status-pill"><span class="dot"></span> Open to Automation / Python roles</div>
        <div class="profile-avatar">👨‍💻</div>
        <div class="profile-name">SABARINATHAN S</div>
        <div class="profile-title">Software &amp; Automation Engineer</div>
        <div class="profile-title">Python | Selenium | Power Automate | RPA</div>
        <div class="hero-chips">
            <span>🐍 Python</span><span>🤖 RPA</span><span>🧪 Selenium</span>
            <span>⚡ Power Automate</span><span>🎭 Playwright</span>
        </div>
        <div class="social-links">
            <a href="https://linkedin.com/in/sabari12" target="_blank" class="social-btn">
                💼 LinkedIn
            </a>
            <a href="https://github.com/sabari128" target="_blank" class="social-btn">
                🐙 GitHub
            </a>
            <a href="mailto:sabarinathan1202s@gmail.com" class="social-btn">
                📧 Email
            </a>
            <a href="tel:+919342952824" class="social-btn">
                📱 Call
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4+</div>
            <div class="stat-label">Automation Apps</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Internships</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">8.4</div>
            <div class="stat-label">CGPA</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">2</div>
            <div class="stat-label">Certifications</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # About Me Section
    st.markdown('<div class="section-header">👨‍💻 About Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="font-size: 1.1rem; line-height: 1.8; color: #334155;">
            🚀 Aspiring <strong>Software &amp; Automation Engineer</strong> with hands-on expertise in
            <strong>Python, Selenium, Playwright, Microsoft Power Automate, and SOAP APIs</strong>.
            I build enterprise automation solutions that streamline operations and dramatically reduce manual effort.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #334155;">
            Currently interning at <strong>Lumen Technologies India</strong>, where I've delivered
            <strong>4 automation applications</strong> using Python, Selenium, SOAP UI, and Power Automate to
            automate web &amp; API testing workflows. I hold a <strong>CGPA of 8.4</strong> in BE Computer Science
            from Mahendra Engineering College, and I'm a certified <strong>UiPath &amp; Power Automate RPA Developer</strong>.
            I bring a strong problem-solving mindset and a passion for workflow automation and innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Highlights
    st.markdown('<div class="section-header">✨ Highlights</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #6366f1;">🎓 Education</h3>
            <p style="font-size: 1rem; line-height: 1.6;">
                BE Computer Science &amp; Engineering — Mahendra Engineering College, Namakkal (CGPA: 8.4)<br>
                HSC — Shri Swamy Matric Hr Sec School (2022) — 83%<br>
                SSLC — Shri Swamy Matric Hr Sec School (2020) — 95%
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #6366f1;">⚙️ Automation Focus</h3>
            <p style="font-size: 1rem; line-height: 1.6;">
                Specialized in RPA and workflow automation with Selenium, Playwright, Power Automate,
                and SOAP APIs — turning repetitive manual processes into reliable automated pipelines.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #6366f1;">🤝 Leadership</h3>
            <p style="font-size: 1rem; line-height: 1.6;">
                Overall Student Coordinator for a 24-hour departmental hackathon, Class Committee Member,
                and active NSS &amp; UiPath Committee volunteer. Strong communication and team collaboration.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #6366f1;">🚀 Growth Mindset</h3>
            <p style="font-size: 1rem; line-height: 1.6;">
                Committed to continuous learning — certified in UiPath &amp; Power Automate RPA development,
                always exploring new tools and best practices in automation and software engineering.
            </p>
        </div>
        """, unsafe_allow_html=True)

elif "Experience" in page:
    st.markdown('<div class="section-header">💼 Professional Experience</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="timeline-item">
            <h2 style="color: #6366f1; margin-bottom: 0.2rem;">Automation Engineer Intern</h2>
            <h4 style="color: #ec4899; margin-top: 0;">Lumen Technologies India · Feb 2026 – Aug 2026 (Stipend)</h4>
            <p style="font-size: 1rem; line-height: 1.7; color: #475569;">
                Developed and delivered <strong>4 automation applications</strong> using Python, Selenium, SOAP UI,
                and Microsoft Power Automate to streamline core business processes. Automated web and API testing
                workflows, <strong>significantly reducing manual effort</strong> and improving operational efficiency.
            </p>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Selenium</span>
            <span class="skill-tag">SOAP UI</span>
            <span class="skill-tag">Power Automate</span>
            <span class="skill-tag">API Testing</span>
        </div>
        <div class="timeline-item" style="padding-bottom: 0;">
            <h2 style="color: #6366f1; margin-bottom: 0.2rem;">Deep Learning Intern</h2>
            <h4 style="color: #ec4899; margin-top: 0;">Infosys Internship</h4>
            <p style="font-size: 1rem; line-height: 1.7; color: #475569;">
                Built a <strong>Speech-to-Image live conversion</strong> pipeline — recording audio, transcribing it
                with Whisper AI, running sentiment analysis, and generating images with Stable Diffusion for
                positive/neutral sentiment.
            </p>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">Whisper AI</span>
            <span class="skill-tag">Stable Diffusion</span>
            <span class="skill-tag">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">🏅 Achievements & Involvement</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <ul style="font-size: 1rem; line-height: 1.9; color: #475569;">
            <li><strong>Coders Club:</strong> Overall Student Coordinator for a 24-hour departmental hackathon.</li>
            <li><strong>Class Committee Member:</strong> Liaison between students and faculty on academic & administrative matters.</li>
            <li><strong>NSS Volunteer:</strong> Community service including blood donation, Aadhaar, and eye camps.</li>
            <li><strong>UiPath Committee Member:</strong> Promoted RPA awareness through workshops and automation activities.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif "Resume" in page:
    st.markdown('<div class="section-header">📄 Resume Analysis</div>', unsafe_allow_html=True)
    
    # Download Resume Button
    resume_path = Path("Sabarinathan_Resume.pdf")
    if resume_path.exists():
        st.markdown(
            get_pdf_download_link(resume_path, "📥 Download Resume (PDF)"),
            unsafe_allow_html=True
        )
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Read and display resume content
        with st.spinner("Analyzing resume..."):
            resume_text = read_resume_pdf(resume_path)
            
            if resume_text and not resume_text.startswith("Error"):
                st.markdown("""
                <div class="card resume-doc">
                    <h3>🧑‍💼 Professional Summary</h3>
                    <p>Aspiring Software &amp; Automation Engineer skilled in Python, Selenium, Playwright,
                    Power Automate and SOAP APIs — delivering enterprise automation that streamlines
                    operations and reduces manual effort.</p>
                    <h3>🎓 Education</h3>
                    <p class="r-sub">BE Computer Science &amp; Engineering — Mahendra Engineering College, Namakkal</p>
                    <p>CGPA: 8.4 &nbsp;•&nbsp; HSC (2022): 83% &nbsp;•&nbsp; SSLC (2020): 95%</p>
                    <h3>💼 Experience</h3>
                    <p class="r-sub">Automation Engineer Intern — Lumen Technologies India (Feb 2026 – Aug 2026)</p>
                    <p>Delivered 4 automation applications using Python, Selenium, SOAP UI and Power Automate;
                    automated web &amp; API testing workflows, significantly reducing manual effort.</p>
                    <p class="r-sub">Deep Learning Intern — Infosys</p>
                    <p>Built a Speech-to-Image live conversion pipeline with Whisper AI, sentiment analysis and Stable Diffusion.</p>
                    <h3>🚀 Projects</h3>
                    <ul>
                        <li><strong>Deepfake Detection (Live Video Calls)</strong> — OpenCV, MediaPipe, TensorFlow/PyTorch, Streamlit.</li>
                        <li><strong>Speech-to-Image Live Conversion</strong> — Whisper AI, Stable Diffusion, Streamlit.</li>
                        <li><strong>Hexa Bot</strong> — Bluetooth car with obstacle avoidance (Arduino, C, Python).</li>
                    </ul>
                    <h3>🛠️ Technical Skills</h3>
                    <p><strong>Languages:</strong> Python, SQL, Automation &nbsp;•&nbsp;
                    <strong>Tools:</strong> Streamlit, Power BI, StarUML, UiPath Studio, Power Automate</p>
                    <h3>🏆 Certifications</h3>
                    <p>UiPath Automation Developer Associate &nbsp;•&nbsp; Microsoft Power Automate RPA Developer (PL-500)</p>
                    <h3>🤝 Organizations</h3>
                    <p>NSS Volunteer &nbsp;•&nbsp; Class Committee Member &nbsp;•&nbsp; Coders Club (Overall Coordinator) &nbsp;•&nbsp; UiPath Committee Member</p>
                </div>
                """, unsafe_allow_html=True)

                with st.expander("📄 View raw extracted resume text"):
                    st.text(resume_text)
                
                # Resume Analysis
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="section-header">🔍 Resume Insights</div>', unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    word_count = len(resume_text.split())
                    st.markdown(f"""
                    <div class="card" style="text-align: center;">
                        <h2 style="color: #667eea;">{word_count}</h2>
                        <p>Total Words</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    char_count = len(resume_text)
                    st.markdown(f"""
                    <div class="card" style="text-align: center;">
                        <h2 style="color: #667eea;">{char_count}</h2>
                        <p>Total Characters</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    lines = resume_text.count('\n') + 1
                    st.markdown(f"""
                    <div class="card" style="text-align: center;">
                        <h2 style="color: #667eea;">{lines}</h2>
                        <p>Total Lines</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Key sections detected
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("### 📌 Detected Sections")
                
                sections = []
                keywords = ['education', 'experience', 'skills', 'projects', 'certifications', 
                           'contact', 'objective', 'summary', 'achievements', 'languages']
                
                for keyword in keywords:
                    if keyword.lower() in resume_text.lower():
                        sections.append(keyword.capitalize())
                
                if sections:
                    for section in sections:
                        st.markdown(f'<span class="skill-tag">✓ {section}</span>', unsafe_allow_html=True)
                else:
                    st.info("No standard sections detected. The resume might have a unique format.")
                
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error(resume_text)
    else:
        st.error("Resume file not found. Please ensure 'Sabarinathan_Resume.pdf' is in the same directory.")

elif "Projects" in page:
    st.markdown('<div class="section-header">💼 Featured Projects</div>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea;">🤖 Deepfake Detection Using Live Video Calls</h2>
        <p style="font-size: 1rem; line-height: 1.6; color: #555;">
            <strong>Description:</strong> A real-time deepfake detection system that analyzes live video calls to determine authenticity. 
            The system detects whether a person attending a live video interview is real or fake by analyzing facial movements, 
            head position, lip sync, and expressions, and sends authenticity notifications.
        </p>
        <p><strong>Role:</strong> Collaborated with Team Members</p>
        <p><strong>Technologies:</strong></p>
        <span class="skill-tag">Python</span>
        <span class="skill-tag">OpenCV</span>
        <span class="skill-tag">MediaPipe</span>
        <span class="skill-tag">TensorFlow/PyTorch</span>
        <span class="skill-tag">Streamlit</span>
        <br><br>
        <a href="https://github.com/sabari128/Deepfake-Detection-using-live-calls" target="_blank" style="color: #667eea; font-weight: 600;">
            🔗 View on GitHub →
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea;">🎤 Speech-to-Image Live Conversion using Deep Learning</h2>
        <p style="font-size: 1rem; line-height: 1.6; color: #555;">
            <strong>Description:</strong> An innovative project completed during Infosys Internship that converts speech to images in real-time. 
            The system records audio through microphone, transcribes it to text using Whisper model, performs sentiment analysis, 
            and generates images based on the transcription if sentiment is positive or neutral.
        </p>
        <p><strong>Features:</strong></p>
        <ul style="line-height: 1.8;">
            <li>Audio Recording through microphone</li>
            <li>Speech-to-Text transcription using Whisper AI</li>
            <li>Sentiment Analysis classification</li>
            <li>Image Generation using Stable Diffusion</li>
        </ul>
        <p><strong>Technologies:</strong></p>
        <span class="skill-tag">Python</span>
        <span class="skill-tag">Google Colab</span>
        <span class="skill-tag">Streamlit</span>
        <span class="skill-tag">Whisper AI</span>
        <span class="skill-tag">Stable Diffusion</span>
        <br><br>
        <a href="https://github.com/sabari128/Speech-to-Image" target="_blank" style="color: #667eea; font-weight: 600;">
            🔗 View on GitHub →
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
    <div class="card">
        <h2 style="color: #667eea;">🚗 Hexa Bot - Bluetooth Car with Obstacle Avoidance</h2>
        <p style="font-size: 1rem; line-height: 1.6; color: #555;">
            <strong>Description:</strong> An Arduino-based robotics project featuring a Bluetooth-controlled car with intelligent 
            obstacle avoidance capabilities. The system uses sensors to detect obstacles in real-time and automatically stops 
            to avoid collisions, demonstrating IoT and embedded systems expertise.
        </p>
        <p><strong>Role:</strong> Team Member</p>
        <p><strong>Technologies:</strong></p>
        <span class="skill-tag">Arduino</span>
        <span class="skill-tag">C</span>
        <span class="skill-tag">Python</span>
        <span class="skill-tag">Bluetooth</span>
        <span class="skill-tag">Sensors</span>
        <br><br>
        <a href="https://github.com/sabari128/Hexabot" target="_blank" style="color: #667eea; font-weight: 600;">
            🔗 View on GitHub →
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # GitHub Stats
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📈 GitHub Activity</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="color:#475569; margin-top:0;">Explore my open-source repositories 👇</p>
        <div style="display:flex; flex-wrap:wrap; gap:1rem; margin-bottom:1rem;">
            <a href="https://github.com/sabari128/Deepfake-Detection-using-live-calls" target="_blank" class="repo-card">
                <h4>🤖 Deepfake Detection</h4>
                <p>Real-time authenticity checks on live video calls.</p>
                <span class="repo-lang">Python · OpenCV · MediaPipe</span>
            </a>
            <a href="https://github.com/sabari128/Speech-to-Image" target="_blank" class="repo-card">
                <h4>🎤 Speech-to-Image</h4>
                <p>Speech → sentiment → generated image pipeline.</p>
                <span class="repo-lang">Whisper AI · Stable Diffusion</span>
            </a>
            <a href="https://github.com/sabari128/Hexabot" target="_blank" class="repo-card">
                <h4>🚗 Hexa Bot</h4>
                <p>Bluetooth car with obstacle avoidance.</p>
                <span class="repo-lang">Arduino · C · Python</span>
            </a>
        </div>
        <div style="text-align:center;">
            <a href="https://github.com/sabari128" target="_blank" class="download-btn">🐙 Visit My GitHub Profile</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif "Skills" in page:
    st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    
    # Programming Languages
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">💻 Languages</h3>
        <span class="skill-tag">Python</span>
        <span class="skill-tag">SQL</span>
        <span class="skill-tag">Automation Scripting</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Automation & Testing
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">🤖 Automation &amp; Testing</h3>
        <span class="skill-tag">Selenium</span>
        <span class="skill-tag">Playwright</span>
        <span class="skill-tag">Power Automate</span>
        <span class="skill-tag">UiPath Studio</span>
        <span class="skill-tag">SOAP UI</span>
        <span class="skill-tag">SOAP APIs</span>
        <span class="skill-tag">API Testing</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Frameworks & Libraries
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">🔧 Frameworks &amp; Libraries</h3>
        <span class="skill-tag">Streamlit</span>
        <span class="skill-tag">TensorFlow</span>
        <span class="skill-tag">PyTorch</span>
        <span class="skill-tag">OpenCV</span>
        <span class="skill-tag">MediaPipe</span>
        <span class="skill-tag">Whisper AI</span>
        <span class="skill-tag">Stable Diffusion</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Databases
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">🗄️ Databases</h3>
        <span class="skill-tag">SQL</span>
        <span class="skill-tag">MySQL</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Tools & Technologies
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">⚙️ Tools &amp; Platforms</h3>
        <span class="skill-tag">Power BI</span>
        <span class="skill-tag">StarUML</span>
        <span class="skill-tag">Google Colab</span>
        <span class="skill-tag">Git</span>
        <span class="skill-tag">VS Code</span>
        <span class="skill-tag">Arduino</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Areas of Interest
    st.markdown("""
    <div class="card">
        <h3 style="color: #6366f1;">🌟 Areas of Interest</h3>
        <span class="skill-tag">Workflow Automation</span>
        <span class="skill-tag">RPA Development</span>
        <span class="skill-tag">Python Development</span>
        <span class="skill-tag">Data Analysis</span>
        <span class="skill-tag">Problem Solving</span>
        <span class="skill-tag">Team Collaboration</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Skill Proficiency Bars
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 Skill Proficiency</div>', unsafe_allow_html=True)

    skills_proficiency = {
        "Python": 90,
        "Selenium": 85,
        "Power Automate": 85,
        "Playwright": 80,
        "SOAP / API Testing": 80,
        "UiPath (RPA)": 80,
        "SQL": 78,
        "Power BI": 70
    }

    bars = "".join(
        f'<div class="skill-row">'
        f'<div class="skill-row-head"><span>{skill}</span><span>{pct}%</span></div>'
        f'<div class="skill-bar"><span style="width:{pct}%"></span></div>'
        f'</div>'
        for skill, pct in skills_proficiency.items()
    )
    st.markdown(f'<div class="card">{bars}</div>', unsafe_allow_html=True)

elif "Certifications" in page:
    st.markdown('<div class="section-header">🏆 Certifications</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h2 style="color: #6366f1;">🤖 UiPath</h2>
            <h4 style="color: #ec4899;">Automation Developer Associate</h4>
            <p style="color: #475569; line-height: 1.6;">
                UiPath Academy Automation Developer Associate Training — hands-on RPA development,
                workflow design, and bot deployment.
            </p>
            <span class="skill-tag">RPA</span>
            <span class="skill-tag">UiPath Studio</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <h2 style="color: #6366f1;">⚡ Microsoft Power Automate</h2>
            <h4 style="color: #ec4899;">PL-500T00-A: RPA Developer</h4>
            <p style="color: #475569; line-height: 1.6;">
                Microsoft Power Automate RPA Developer training — building automated cloud &amp; desktop
                flows to streamline business processes.
            </p>
            <span class="skill-tag">Power Automate</span>
            <span class="skill-tag">Microsoft</span>
        </div>
        """, unsafe_allow_html=True)

elif "Contact" in page:
    st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)
    
    # Contact Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h2>📧 Email</h2>
            <p style="font-size: 1.1rem;">sabarinathan1202s@gmail.com</p>
            <br>
            <h2>📱 Phone</h2>
            <p style="font-size: 1.1rem;">+91 9342952824</p>
            <br>
            <h2>📍 Location</h2>
            <p style="font-size: 1.1rem;">9/196, Sakthi Nagar, Valasaiyur, Salem</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💬 Send Me a Message")
        # Rendered in a component iframe so the form actually submits (FormSubmit → email)
        components.html("""
        <html><head><style>
            * { box-sizing: border-box; font-family: 'Poppins', -apple-system, Segoe UI, sans-serif; }
            form { display: flex; flex-direction: column; gap: 0.8rem; }
            input, textarea {
                width: 100%; padding: 12px 15px; font-size: 0.95rem;
                border: 1px solid rgba(99,102,241,0.3); border-radius: 12px;
                background: #f8fafc; transition: border .2s ease, box-shadow .2s ease;
            }
            input:focus, textarea:focus {
                outline: none; border-color: #6366f1; background: #fff;
                box-shadow: 0 0 0 3px rgba(99,102,241,0.15);
            }
            textarea { min-height: 120px; resize: vertical; }
            button {
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
                color: #fff; border: none; padding: 13px; border-radius: 30px;
                font-weight: 600; font-size: 1rem; cursor: pointer; transition: transform .2s ease;
            }
            button:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(99,102,241,0.4); }
        </style></head><body>
        <form action="https://formsubmit.co/sabarinathan1202s@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="New message from your portfolio!">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <input type="text" name="subject" placeholder="Subject">
            <textarea name="message" placeholder="Your message..." required></textarea>
            <button type="submit">Send Message 🚀</button>
        </form>
        </body></html>
        """, height=430)
        st.caption("📌 Your first message triggers a one-time confirmation email from FormSubmit to activate delivery.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Social Media Links
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🌐 Connect With Me</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card" style="text-align: center;">
        <a href="https://linkedin.com/in/sabari12" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" 
                 alt="LinkedIn" style="margin: 10px;">
        </a>
        <a href="https://github.com/sabari128" target="_blank">
            <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" 
                 alt="GitHub" style="margin: 10px;">
        </a>
        <a href="mailto:sabarinathan1202s@gmail.com">
            <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" 
                 alt="Email" style="margin: 10px;">
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p>© 2026 Sabarinathan. All rights reserved.</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
