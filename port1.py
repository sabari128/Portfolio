# import streamlit as st
# from PIL import Image
# import pandas as pd
# import plotly.express as px

# # Page configuration
# st.set_page_config(
#     page_title="Sabarinathan S | Python Developer",
#     page_icon="🐍",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS
# st.markdown("""
# <style>
#     :root {
#         --primary: #2563eb;
#         --secondary: #1e40af;
#         --accent: #f59e0b;
#     }
    
#     .main {
#         background-color: #f8fafc;
#     }
    
#     .sidebar .sidebar-content {
#         background: linear-gradient(180deg, var(--primary), var(--secondary));
#         color: white;
#     }
    
#     .profile-img {
#         border-radius: 50%;
#         border: 4px solid white;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     }
    
#     .card {
#         background: white;
#         border-radius: 10px;
#         padding: 1.5rem;
#         margin-bottom: 1rem;
#         box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
#         border-left: 4px solid var(--accent);
#     }
    
#     .skill-pill {
#         display: inline-block;
#         padding: 0.25rem 0.75rem;
#         margin: 0.25rem;
#         background-color: #e0e7ff;
#         border-radius: 9999px;
#         color: var(--secondary);
#         font-weight: 500;
#     }
    
#     .social-icon {
#         font-size: 1.5rem;
#         margin-right: 1rem;
#         color: white;
#     }
    
#     h1, h2, h3 {
#         color: var(--secondary);
#     }
# </style>
# """, unsafe_allow_html=True)

# # Sidebar
# with st.sidebar:
#     # Profile image - you can add your own image
#     col1, col2, col3 = st.columns([1,3,1])
#     with col2:
#         try:
#             profile_img = Image.open("profile.jpg")
#         except:
#             profile_img = Image.new('RGB', (200, 200), color=(73, 109, 137))
#         st.image(profile_img, width=150, use_column_width=False, clamp=True, 
#                  channels="RGB", output_format="JPEG")
    
#     st.markdown("<h1 style='text-align: center;'>Sabarinathan S</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; color: var(--accent); font-weight: 600;'>Python Developer | Data Analyst</p>", unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Contact Info
#     st.markdown("""
#     <div style='padding: 0.5rem;'>
#         <p><i class='fas fa-envelope social-icon'></i> sabarinathan1202s@gmail.com</p>
#         <p><i class='fas fa-phone social-icon'></i> +91 9342952824</p>
#         <p><i class='fas fa-map-marker-alt social-icon'></i> Salem, Tamil Nadu</p>
#         <p><i class='fab fa-linkedin social-icon'></i> linkedin.com/in/sabari12</p>
#         <p><i class='fab fa-github social-icon'></i> github.com/sabari128</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Main content
# tab1, tab2, tab3, tab4 = st.tabs(["About", "Skills", "Projects", "Background"])

# with tab1:
#     st.markdown("""
#     <div class='card'>
#         <h2>👋 About Me</h2>
#         <p>Dedicated and passionate Python developer with expertise in data analysis and problem-solving. 
#         Known for innovative mindset and commitment to continuous learning. Combines technical skills 
#         with strong communication abilities to deliver outstanding results.</p>
        
#         <h3>What I Bring</h3>
#         <ul>
#             <li>Strong foundation in Python programming and data analysis</li>
#             <li>Experience with full project lifecycle from concept to deployment</li>
#             <li>Ability to quickly learn and adapt to new technologies</li>
#             <li>Team player with leadership qualities</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)

# with tab2:
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         <div class='card'>
#             <h2>💻 Technical Skills</h2>
#             <div>
#                 <span class='skill-pill'>Python</span>
#                 <span class='skill-pill'>Data Analysis</span>
#                 <span class='skill-pill'>SQL</span>
#                 <span class='skill-pill'>Java</span>
#                 <span class='skill-pill'>Streamlit</span>
#                 <span class='skill-pill'>Power BI</span>
#                 <span class='skill-pill'>UIPath</span>
#                 <span class='skill-pill'>Arduino</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class='card'>
#             <h2>📊 Tools & Technologies</h2>
#             <div>
#                 <span class='skill-pill'>Google Colab</span>
#                 <span class='skill-pill'>StarUML</span>
#                 <span class='skill-pill'>Whisper Model</span>
#                 <span class='skill-pill'>Deep Learning</span>
#                 <span class='skill-pill'>Sentiment Analysis</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("""
#         <div class='card'>
#             <h2>🌟 Soft Skills</h2>
#             <div>
#                 <span class='skill-pill'>Communication</span>
#                 <span class='skill-pill'>Team Management</span>
#                 <span class='skill-pill'>Time Management</span>
#                 <span class='skill-pill'>Problem Solving</span>
#                 <span class='skill-pill'>Leadership</span>
#                 <span class='skill-pill'>Adaptability</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class='card'>
#             <h2>🗣️ Languages</h2>
#             <div>
#                 <span class='skill-pill'>Tamil (Native)</span>
#                 <span class='skill-pill'>English (Fluent)</span>
#                 <span class='skill-pill'>Telugu (Conversational)</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

# with tab3:
#     st.markdown("""
#     <div class='card'>
#         <h2>🤖 Hexa Bot</h2>
#         <p><strong>Bluetooth car with obstacle avoidance using Arduino</strong></p>
#         <ul>
#             <li>Team member in developing an intelligent vehicle system</li>
#             <li>Implemented obstacle detection and avoidance mechanisms</li>
#             <li>Technologies: C, Python, Arduino</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class='card'>
#         <h2>🎙️ Speech-to-Image Live Conversion</h2>
#         <p><strong>Infosys Internship Project</strong></p>
#         <ul>
#             <li>Developed a system to convert speech to generated images in real-time</li>
#             <li>Features: Audio recording, transcription, sentiment analysis, image generation</li>
#             <li>Tech stack: Google Colab, Streamlit, Python, Whisper model</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)

# with tab4:
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         <div class='card'>
#             <h2>🎓 Education</h2>
#             <h3>BE Computer Science</h3>
#             <p>Malendra Engineering College, Namakkal</p>
#             <p>CGPA: 8.2</p>
            
#             <h3>HSC (2022)</h3>
#             <p>Shri Swamy Matric Hr Sec School</p>
#             <p>Score: 83%</p>
            
#             <h3>SSLC (2020)</h3>
#             <p>Shri Swamy Matric Hr Sec School</p>
#             <p>Score: 95%</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class='card'>
#             <h2>🏆 Certifications</h2>
#             <ul>
#                 <li>NPTEL Java Certification</li>
#                 <li>Typewriting Junior (First class)</li>
#                 <li>Blood Camp Volunteer</li>
#                 <li>NSS Special Camp (One week)</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("""
#         <div class='card'>
#             <h2>👥 Organizations</h2>
#             <ul>
#                 <li>NSS Volunteer</li>
#                 <li>Class Committee Member</li>
#                 <li>Coders Club</li>
#                 <li>UIPath Committee Member</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
        
#         st.markdown("""
#         <div class='card'>
#             <h2>ℹ️ Personal Info</h2>
#             <ul>
#                 <li><strong>Date of Birth:</strong> 12.02.2005</li>
#                 <li><strong>Gender:</strong> Male</li>
#                 <li><strong>Nationality:</strong> Indian</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.markdown("<p style='text-align: center;'>© 2023 Sabarinathan S | Built with Streamlit</p>", unsafe_allow_html=True)

import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import requests # Import the requests library

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
        with a strong background in **Python, SQL, and Data Analysis**.
        I leverage an innovative mindset and problem-solving skills to achieve outstanding results.
        Dedicated to continuous learning and professional growth, I thrive on tackling complex challenges
        and exemplify leadership and expertise.
        """
    )
    # Navigation links in the header
    st.markdown("""
    <div style="display: flex; gap: 15px; margin-top: 25px;">
        <a href="#about-me-section" class="st-bu">About Me</a>
        <a href="#skills-section" class="st-bu">My Skills</a>
        <a href="#projects-section" class="st-bu">My Projects</a>
    </div>
    """, unsafe_allow_html=True)

    # --- MOVED: CONNECT WITH ME SECTION as buttons (Still in Header) ---
    st.markdown("---") # Separator for visual clarity
    st.subheader("Explore My Presence")
    st.write("Click on the buttons below to explore my profiles and connect directly.")

    # Create columns for the buttons
    col1, col2, col3 = st.columns(3) # Creates 3 columns for LinkedIn, GitHub, Email

    with col1:
        st.link_button("🔗 LinkedIn", "https://linkedin.com/in/sabari12")
    with col2:
        st.link_button("🐙 GitHub", "https://github.com/sabari128")
    with col3:
        st.link_button("📧 Email (Direct)", "mailto:sabarinathan1202s@gmail.com")


st.markdown("---") # Visual separator

# --- NAVIGATION (Using Tabs for organized sections) ---
tab_about_me, tab_skills, tab_projects, tab_contact = st.tabs(["About Me", "Skills", "Projects", "Contact Me"])

# --- ABOUT ME SECTION ---
with tab_about_me:
    st.markdown("<h2 id='about-me-section'>About Me</h2>", unsafe_allow_html=True) # Anchor for direct linking

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

        # --- RESUME DOWNLOAD BUTTON (remains here) ---
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
        <span class="skill-badge">Data Analysis <span class="skill-icon">📊</span></span>
        <span class="skill-badge">Java <span class="skill-icon">☕</span></span>
        <span class="skill-badge">Streamlit <span class="skill-icon">🚀</span></span>
        <span class="skill-badge">PowerBI <span class="skill-icon">📈</span></span>
        <span class="skill-badge">StarUML <span class="skill-icon"> UML</span></span>
        <span class="skill-badge">UIPath Studio <span class="skill-icon">🤖</span></span>
        <span class="skill-badge">C <span class="skill-icon">💻</span></span>
        <span class="skill-badge">Google Colab <span class="skill-icon">☁️</span></span>
        <span class="skill-badge">Deep Learning <span class="skill-icon">🧠</span></span>
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

# --- CONTACT ME SECTION (New Tab) ---
with tab_contact:
    st.title("📩 Get in Touch!")
    st.write("I'm always eager to connect! Feel free to reach out via the methods below or send me a message directly.")

    st.subheader("Direct Contact Information")
    st.markdown("""
    - 📧 **Email:** [sabarinathan1202s@gmail.com](mailto:sabarinathan1202s@gmail.com)
    - 🔗 **LinkedIn:** [linkedin.com/in/sabari12](https://www.linkedin.com/in/sabari12)
    - 🐙 **GitHub:** [github.com/sabari128](https://github.com/sabari128)
    - 📞 **Contact No:** [9342952824](tel:9342952824)
    """)

    st.markdown("---")

    # Contact Form
    st.subheader("📬 Send Me a Message")
    st.write("Fill out the form below and I'll get back to you as soon as possible.")
    st.warning("💡 **Important Note:** This form uses Formspree for actual message and file delivery. After submission, check your email for the first message from Formspree to confirm your email address.")


    with st.form("contact_form"):
        user_name = st.text_input("Your Name *")
        user_email = st.text_input("Your Email *")
        user_message = st.text_area("Your Message *")
        uploaded_file = st.file_uploader("Attach your resume/portfolio (Optional)", type=["pdf", "doc", "docx", "txt", "jpg", "jpeg", "png"])

        submitted = st.form_submit_button("Send Message")

        # --- Formspree Integration Logic ---
        formspree_endpoint_url = "YOUR_FORMSPREE_ENDPOINT_URL_HERE" # <<< IMPORTANT: REPLACE THIS WITH YOUR ACTUAL FORMSPREE URL

        if submitted:
            if not user_name:
                st.error("⚠️ Please enter your name.")
            elif not user_email:
                st.error("⚠️ Please enter your email.")
            elif not user_message:
                st.error("⚠️ Please enter your message.")
            else:
                try:
                    # Prepare data for Formspree
                    payload = {
                        "name": user_name,
                        "email": user_email,
                        "message": user_message
                    }
                    files = {}
                    if uploaded_file is not None:
                        # Formspree expects the file name as the field name
                        files["attachment"] = (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)

                    response = requests.post(formspree_endpoint_url, data=payload, files=files)

                    if response.status_code == 200:
                        st.success("✅ Message Sent Successfully! I'll get back to you soon.")
                        st.balloons() # Visual confirmation
                    else:
                        st.error(f"❌ Failed to send message. Please try again. (Error: {response.status_code} - {response.text})")
                        st.info("Ensure your Formspree endpoint URL is correct and your email is confirmed on Formspree.")

                except requests.exceptions.RequestException as e:
                    st.error(f"❌ An error occurred while sending the message: {e}")
                    st.info("Please check your internet connection or Formspree setup.")

    st.markdown("---")

# --- FOOTER ---
st.markdown("""
<br><br><br>
<div style="text-align: center; color: #7f8c8d;" class="footer-text">
    <p>&copy; 2025 Sabarinathan S. Built with ❤️ and Streamlit.</p>
</div>
""", unsafe_allow_html=True)