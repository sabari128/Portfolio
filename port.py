
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

# --- HELPER FUNCTIONS ---
# Function to load local CSS file
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Could not find {file_name}. Custom CSS not applied. Please ensure style.css is in the same directory.")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sabarinathan S - Python Developer Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed" # Start with sidebar collapsed for a cleaner look
)

# Apply custom CSS
local_css("style.css")

# --- HEADER / HERO SECTION ---
with st.container():
    st.markdown("<h3 class='st-emotion-cache-1f0f3hv'>Hi, I am Sabarinathan S 👋</h3>", unsafe_allow_html=True)
    st.title("Aspiring Python Developer")
    st.write(
        """
        A dedicated and passionate individual committed to excellence,
        with a strong background in **Python, SQL, and Data Analyst*.
        I leverage an innovative mindset and problem-solving skills to achieve outstanding results.
        Dedicated to continuous learning and professional growth, I thrive on tackling complex challenges
        and exemplify leadership and expertise.
        """
    )


st.markdown("---") # Visual separator

# --- NAVIGATION (Using Tabs for organized sections) ---
tab_about_me, tab_skills, tab_projects = st.tabs(["About Me", "Skills", "Projects"])

# --- ABOUT ME SECTION ---
with tab_about_me:
    st.markdown("<h2 id='about-me'>About Me</h2>", unsafe_allow_html=True) # Anchor for direct linking

    col_pic, col_text = st.columns([1, 2])

    with col_pic:
        try:
            profile_image = Image.open('10.jpg') # Using relative path
            st.image(profile_image, width=300, caption="Sabarinathan S")
        except FileNotFoundError:
            st.warning("Profile picture '10.jpg' not found. Please add your image to the same directory.")
            st.image("https://via.placeholder.com/300x300?text=Your+Profile+Pic", caption="Placeholder Image")

    with col_text:
        st.write(
            """
            Hello! I'm **Sabarinathan S**, a **Computer Science Engineering** student from Mahendra Engineering College, Namakkal.
            I bring a strong academic foundation (CGPA 8.2) combined with practical experience.
            My journey into software development is driven by a desire to build impactful solutions.
            I am known for my kindness, politeness, and a positive outlook, which I believe are essential
            for effective teamwork and continuous improvement.
            """
        )
        st.write(
            """
            My core strengths lie in **innovative problem-solving** and a **dedication to continuous learning**.
            I thrive in environments that challenge me to expand my knowledge and apply it to real-world scenarios.
            """
        )

        st.subheader("Education")
        # MODIFIED: Education section as a bulleted list
        st.markdown("""
            - **BE Computer Science** - Mahendra Engineering College, Namakkal (CGPA 8.2)
            - **HSC** - Shri Swamy Matric Hr Sec School (2022) - 83%
            - **SSLC** - Shri Swamy Matric Hr Sec School (2020) - 95%
        """)

        st.subheader("Organizations Involved")
        st.markdown("""
            - NSS Volunteer
            - Class Committee member
            - Coders club
            - Uipath Committee member
        """)

        # --- MODIFIED: CONNECT WITH ME SECTION as buttons ---
        st.subheader("Let's Connect!")
        st.write("I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.")

        # Create columns for the buttons
        col1, col2, col3 = st.columns(3) # Creates 3 columns, adjust as needed

        with col1:
            st.link_button("🔗 LinkedIn", "https://linkedin.com/in/sabari12")
        with col2:
            st.link_button("🐙 GitHub", "https://github.com/sabari128")
        with col3:
            st.link_button("📧 Email", "mailto:sabarinathan1202s@gmail.com")

        # --- RESUME DOWNLOAD BUTTON ---
        st.markdown("---") # Separator before the download button for visual clarity
        st.write("Interested in more details? Download my full resume:")
        resume_path = "Sabarinathan Python Developer.pdf" # Using relative path
        try:
            with open(resume_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
                st.download_button(
                    label="⬇️ Download Resume",
                    data=PDFbyte,
                    file_name="Sabarinathan_Python_Developer_Resume.pdf",
                    mime="application/octet-stream",
                    help="Click to download my full resume in PDF format."
                )
        except FileNotFoundError:
            st.warning(f"Resume file '{resume_path}' not found. Please ensure it's in the same directory as this script.")

    st.markdown("---")

# --- SKILLS SECTION ---
with tab_skills:
    st.markdown("<h2 id='skills-section'>My Skills</h2>", unsafe_allow_html=True)
    st.write("A comprehensive overview of my technical and soft skills, developed through academic projects and personal initiatives.")

    st.subheader("Technical Expertise")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">
        <span class="skill-badge">Python <span class="skill-icon">🐍</span></span>
        <span class="skill-badge">SQL <span class="skill-icon">🗄️</span></span>
        <span class="skill-badge">Data Analyst <span class="skill-icon">📊</span></span>
        <span class="skill-badge">Java <span class="skill-icon">☕</span></span>
        <span class="skill-badge">Streamlit <span class="skill-icon">🚀</span></span>
        <span class="skill-badge">PowerBI <span class="skill-icon">📈</span></span>
        <span class="skill-badge">StarUML <span class="skill-icon"> UML</span></span>
        <span class="skill-badge">UIPath Studio <span class="skill-icon">🤖</span></span>
        <span class="skill-badge">Google Colab <span class="skill-icon">☁️</span></span>
        
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Core Competencies (Soft Skills)")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">
        <span class="skill-badge">Good Communication <span class="skill-icon">🗣️</span></span>
        <span class="skill-badge">Time Management <span class="skill-icon">⏰</span></span>
        <span class="skill-badge">Positive Outlook <span class="skill-icon">😊</span></span>
        <span class="skill-badge">Team Management <span class="skill-icon">🤝</span></span>
        <span class="skill-badge">Problem-Solving <span class="skill-icon">💡</span></span>
        <span class="skill-badge">Continuous Learning <span class="skill-icon">📚</span></span>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Certifications")
    st.markdown("""
        - NPTEL Certifications: Java
        - Typewriting Junior level (First class)
        - Blood camp volunteer
        - Special Camp in NSS (One week camp)
    """)

    st.markdown("---")

# --- PROJECTS SECTION ---
with tab_projects:
    st.markdown("<h2 id='projects-section'>My Projects</h2>", unsafe_allow_html=True)
    st.write("Showcasing my practical application of skills through diverse projects.")

    # Project 1: Hexa Bot
    st.subheader("1. Hexa Bot")
    col_hexaimg, col_hexadesc = st.columns([1, 2])
    with col_hexaimg:
        try:
            # Using relative path
            st.image("hexabot.jpg", caption="Hexa Bot in action") # Ensure this file exists
        except FileNotFoundError:
            st.warning("Project image 'hexabot.jpg' not found. Please add your image to the same directory.")
            st.image("https://via.placeholder.com/400x250?text=Hexa+Bot+Project", caption="Placeholder Image")
    with col_hexadesc:
        st.markdown("**Role:** Team member")
        st.markdown("**Languages Used:** C and Python")
        st.write(
            """
            A project focused on **Bluetooth car and obstacle avoidance using Arduino**.
            The bot is designed to sense obstacles in its path and automatically stop to avoid collisions,
            demonstrating foundational knowledge in robotics and embedded systems.
            """
        )
        st.link_button("View GitHub Repo", "https://github.com/sabari128/Hexabot")

    st.markdown("---")

    # Project 2: Infosys Internship - Speech-to-Image Live Conversion using Deep Learning
    st.subheader("2. Infosys Internship: Speech-to-Image Live Conversion using Deep Learning")
    col_infosysimg, col_infosysdesc = st.columns([1, 2])
    with col_infosysimg:
        try:
            # Using relative path
            st.image("img1.png", caption="Speech-to-Image Conversion") # Ensure this file exists
        except FileNotFoundError:
            st.warning("Project image 'img1.png' not found. Please add your image to the same directory.")
            st.image("https://via.placeholder.com/400x250?text=Speech-to-Image+AI", caption="Placeholder Image")
    with col_infosysdesc:
        st.markdown("**Tech Stack:** Google Colab, Streamlit, Python and various Deep Learning libraries")
        st.write(
            """
            This internship project involved developing a system for **live speech-to-image conversion**
            using advanced Deep Learning techniques. The process involved several key stages:
            """
        )
        st.markdown("""
            - **Audio Recording:** Capturing live audio input directly through your microphone.
            - **Transcription:** Converting recorded audio to text using the powerful **Whisper model**.
            - **Sentiment Analysis:** Classifying the sentiment (positive, neutral, negative) of the transcribed text.
            - **Image Generation:** Dynamically generating an image based on the transcription, specifically when the sentiment is classified as positive or neutral.
        """)
        st.write(
            """
            This project highlights my capabilities in **Deep Learning, Natural Language Processing (NLP),
            and building interactive applications with Streamlit**.
            """
        )
        st.link_button("View GitHub Repo", "https://github.com/sabari128/Speech-to-Image")

    st.markdown("---")

# --- FOOTER ---
st.markdown("""
<br><br><br>
<div style="text-align: center; color: #7f8c8d;" class="footer-text">
    <p>Find me online:</p>
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 15px;">
        <a href="mailto:sabarinathan1202s@gmail.com" target="_blank" style="text-decoration: none; color: #3498db; font-size: 1.1em;">
            📧 sabarinathan1202s@gmail.com
        </a>
        <a href="https://github.com/sabari128" target="_blank" style="text-decoration: none; color: #3498db; font-size: 1.1em;">
            🐙 github.com/sabari128
        </a>
        <a href="https://linkedin.com/in/sabari12" target="_blank" style="text-decoration: none; color: #3498db; font-size: 1.1em;">
            🔗 linkedin.com/in/sabari12
        </a>
    </div>
    <p style="margin-top: 20px;">&copy; 2025 Sabarinathan S. Built with ❤️ and Streamlit.</p>
</div>
""", unsafe_allow_html=True)


