# 🎨 Professional Portfolio - Sabarinathan

An attractive and professional portfolio website built with Python Streamlit that showcases your resume, projects, skills, and contact information.

## ✨ Features

- **🏠 Home Page**: Stunning landing page with quick stats and highlights
- **📄 Resume Analysis**: Automatic PDF resume parsing and analysis
- **💼 Projects Section**: Showcase your best projects with descriptions and links
- **🛠️ Skills Display**: Visual representation of technical and soft skills
- **📬 Contact Page**: Easy-to-use contact form and social media links
- **🎨 Modern UI**: Gradient backgrounds, hover effects, and responsive design
- **📱 Responsive**: Works perfectly on desktop, tablet, and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or navigate to the portfolio directory**:
   ```bash
   cd c:\Portfolio
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run portfolio.py
   ```

4. **Open your browser**:
   The application will automatically open in your default browser at `http://localhost:8501`

## 📝 Customization Guide

### 1. Update Personal Information

Edit the following sections in `portfolio.py`:

- **Profile Name & Title** (Lines 124-126): Update your name and professional title
- **Contact Information** (Line 462-464): Add your email, phone, and location
- **Social Media Links**: Replace placeholder URLs with your actual profiles:
  - LinkedIn: `https://linkedin.com/in/your-profile`
  - GitHub: `https://github.com/your-username`
  - Email: `your.email@example.com`

### 2. Update Projects

In the "Projects" section (starting around line 332), customize:
- Project titles
- Descriptions
- Technologies used
- GitHub repository links

### 3. Modify Skills

Update the skills sections (around line 393) to match your expertise:
- Programming languages
- Frameworks & libraries
- Databases
- Tools & technologies
- Soft skills
- Skill proficiency percentages

### 4. GitHub Stats

Replace `your-username` in the GitHub stats URLs (around line 371) with your actual GitHub username.

### 5. Color Scheme

To change the color theme, modify the gradient colors in the CSS section:
- Current primary: `#667eea` (purple-blue)
- Current secondary: `#764ba2` (purple)

Find and replace these hex codes with your preferred colors.

## 📂 Project Structure

```
Portfolio/
│
├── portfolio.py              # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── Sabarinathan Resume.pdf  # Your resume PDF
```

## 🎯 Features Breakdown

### Home Page
- Professional header with gradient background
- Quick statistics cards (projects, skills, experience)
- About me section with highlights
- Responsive grid layout

### Resume Page
- Automatic PDF parsing and text extraction
- Resume download button
- Content analysis (word count, character count)
- Section detection (education, experience, skills, etc.)

### Projects Page
- Beautiful project cards with descriptions
- Technology tags
- GitHub repository links
- GitHub statistics integration

### Skills Page
- Organized skill categories
- Visual skill tags
- Proficiency bars with percentages
- Comprehensive technology stack display

### Contact Page
- Contact information display
- Interactive contact form
- Social media badges
- Multiple ways to connect

## 🔧 Troubleshooting

### Resume not loading?
- Ensure `Sabarinathan Resume.pdf` is in the same directory as `portfolio.py`
- Check file permissions
- Verify the PDF is not corrupted

### Port already in use?
Run Streamlit on a different port:
```bash
streamlit run portfolio.py --server.port 8502
```

### Styling issues?
- Clear browser cache
- Try a different browser
- Ensure you're using the latest version of Streamlit

## 🌟 Enhancement Ideas

- Add a blog section
- Integrate with GitHub API for real-time stats
- Add a dark/light mode toggle
- Include certifications and achievements
- Add animations and transitions
- Integrate Google Analytics
- Add testimonials section
- Create a download button for project showcases

## 📦 Dependencies

- **Streamlit**: Web application framework
- **PyPDF2**: PDF parsing library
- **Pillow**: Image processing library

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio!

## 📄 License

This project is open source and available for personal use.

## 💡 Tips

1. **Keep it Updated**: Regularly update your projects and skills
2. **High-Quality Resume**: Ensure your PDF resume is well-formatted
3. **Professional Photos**: Add a professional profile photo if desired
4. **Regular Backups**: Keep backups of your portfolio files
5. **Test Responsiveness**: Check on different devices and screen sizes
6. **SEO**: Consider deploying to Streamlit Cloud for better visibility

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

### Deploy to Heroku

1. Create a `Procfile`:
   ```
   web: sh setup.sh && streamlit run portfolio.py
   ```

2. Create a `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. Deploy to Heroku using Git

## 📞 Support

If you have any questions or need help customizing your portfolio, feel free to reach out!

---

**Built with ❤️ using Python & Streamlit**

Last Updated: May 27, 2026
