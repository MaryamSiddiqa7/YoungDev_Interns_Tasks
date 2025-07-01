# Import necessary module
import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Maryam Siddiqa | Digital Resume", page_icon=":briefcase:", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        body {
            background-color: #d9d9d9;
        }
        .main-header {
            background-color: #1b2b44;
            padding: 30px 0;
            text-align: center;
            color: white;
        }
        .main-header h1 {
            font-size: 45px;
            margin-bottom: 5px;
            letter-spacing: 2px;
        }
        .main-header h5 {
            font-weight: 300;
            color: #dcdcdc;
        }
        .section-title {
            font-size: 22px;
            margin-top: 30px;
            font-weight: bold;
            color: #1b2b44;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        .container {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div class="main-header">
    <h1>👩‍💻 Maryam Siddiqa</h1>
    <h5>Aspiring Software Developer | Tech Enthusiast | Problem Solver | Driven to Innovate & Learn</h5>
</div>
""", unsafe_allow_html=True)

# ---- LAYOUT ----
left_col, right_col =st.columns([1, 2])

# ---- LEFT COLUMN ----
with left_col:
    st.markdown('<div class="container">',unsafe_allow_html=True)
    st.markdown('<div class="section-title">📬 Contact</div>',unsafe_allow_html=True)
    st.write("📧 maryamsiddiqa.227@gmail.com")
    st.write("📱 +923152263485")
    st.write("👥 [Facebook](https://www.facebook.com/share/1YrAoCa9h5/)")
    st.write("💼 [GitHub](https://github.com/MaryamSiddiqa7)")
    st.markdown('<div class="section-title">🎓 Education</div>',unsafe_allow_html=True)
    st.write("""
**Bachelor of Engineering in Computer Systems (In Progress)**  
NED University of Engineering & Technology | 2024 – 2028  

**Intermediate (Pre-Engineering)**  
Govt. Degree College Malir Cantt | 2022 – 2024  

**Matriculation (Science Group)**  
Muhammad Ali Jauhar Academy | 2020 – 2022
""")

    st.markdown('<div class="section-title">🛠️ Skills</div>',unsafe_allow_html=True)
    st.write("""
- **Programming & Tools:** Python, Git, GUI Development  
- **Databases:** Practical experience in handling structured data and file-based storage  
- **Problem Solving:** Strong analytical thinking and ability to break down complex tasks  
- **Project Management:** Skilled in organizing, prioritizing, and managing multiple tasks effectively  
- **Collaboration:** Able to work independently and in cross-functional teams with clear communication  
- **Attention to Detail:** Focused, organized, and adaptable in fast-paced environments  
""")

    st.markdown('</div>',unsafe_allow_html=True)

# ---- RIGHT COLUMN ----
with right_col:
    st.markdown('<div class="container">',unsafe_allow_html=True)

    st.markdown('<div class="section-title">💡 Career Summary</div>',unsafe_allow_html=True)
    st.write("""
Highly motivated and detail-oriented professional with a deep interest in technology and its real-world 
applications. Known for a proactive mindset, fast learning ability, and strong analytical skills. 
Demonstrates a natural curiosity for solving complex problems, exploring emerging tools, and 
developing scalable, efficient solutions. Committed to continuous growth and excellence, with a strong 
drive to contribute meaningfully in collaborative, high-impact environments.
""")

    st.markdown('<div class="section-title">📜 Courses & Certifications</div>',unsafe_allow_html=True)
    st.write("""
- **Google IT Automation with Python**, Coursera | 2025  
- **Foundation of AI**, United Latino Students Association | 2025  
- **Crash Course on Python**, Coursera | 2025  
- **Get Started with Python**, Coursera | 2025  
- **Data Science & Analytics**, HP Life | 2025  
- **English Language Advanced**, Delhi English Language Centre | 2023  
- **Diploma in Microsoft Office**, MSQ Foundation | 2021  
""")

    st.markdown('<div class="section-title">👩‍💼 Internship</div>',unsafe_allow_html=True)
    st.write("**Python Developer Intern** | YoungDev Interns (2025)")

    st.markdown('<div class="section-title">💼 Experience</div>',unsafe_allow_html=True)
    st.write("**Teacher**")
    st.write("Comprehensive Model School | 2022-2023  \nMuhammad Ali Jauhar Academy | 2023-2024")
    st.write("""
- Fostered a positive and engaging learning environment  
- Assessed and evaluated student progress and performance  
- Contributed to curriculum development
""")

    st.markdown('<div class="section-title">📂 Projects</div>',unsafe_allow_html=True)
    st.write("""
- Database Management System  
- Car Rental System  
""")

    st.markdown('<div class="section-title">🏆 Achievements & Awards</div>',unsafe_allow_html=True)
    st.markdown("""
**Awarded for Exemplary Teaching Impact**  
- Muhammad Ali Jauhar Academy | 2024
""")

    st.markdown('</div>',unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("---")
st.write("© 2025 Maryam Siddiqa | Built with ❤️ using Streamlit")

