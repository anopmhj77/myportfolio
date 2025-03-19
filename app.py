import streamlit as st

css_file = "main.css"  # Ensure this file exists or remove it if not used

SOCIAL_MEDIA = {
    "Gmail": "mailto:anupmhj77@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/anupmhj/",
    "GitHub": "https://github.com",
    "Twitter": "https://x.com/anop_mhj",
}

# Set page title and layout
st.set_page_config(page_title="Anup Maharjan", layout="wide")

# Custom CSS for the timeline
st.markdown("""
<style>
.timeline {
    border-left: 4px solid #4CAF50;
    padding-left: 20px;
    margin-left: 10px;
}
.timeline-event {
    margin-bottom: 30px;
    position: relative;
}
.timeline-event::before {
    content: '';
    position: absolute;
    left: -30px;
    top: 5px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background-color: #4CAF50;
    border: 3px solid #fff;
}
.timeline-event h4 {
    margin: 0;
    font-size: 18px;
    color: #4CAF50;
}
.timeline-event p {
    margin: 5px 0;
    font-size: 14px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
with col1:
    st.write("")
with col2:
    st.image("E:/project/profoilo/assets/me.png", width=100)
with col3:
    st.title("Anup Maharjan")
    st.header("Data Scientist")
    st.write('\n')  # Removed extra indentation
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")  # Fixed indentation
with col4:
    st.write("")

# Career Summary
st.subheader("Career Summary")
st.write("""
As a Data Scientist, I excel at extracting meaningful insights from complex datasets to drive strategic decision-making. With expertise in machine learning, statistical analysis, and data visualization, I transform raw data into actionable intelligence. My ability to develop predictive models, automate processes, and interpret trends empowers businesses to optimize operations and enhance performance. Passionate about data-driven problem-solving, I continuously explore cutting-edge AI and big data technologies to deliver innovative solutions.
""")

# Create columns for Work Experiences, Area of Expertise, and Software Skills
col1, col2, col3 = st.columns([2, 1, 1])  

# Work Experiences in the first column (left side)
with col1:
    st.subheader("Work Experiences")

    # Timeline HTML
    st.markdown("""
    <div class="timeline">
        <div class="timeline-event">
            <h4>Feb 2020 - Nov 2022</h4>
            <p><strong>Data Entry</strong></p>
            <p>Jwagal, Kupondole, Lalitpur</p>
            <p> ✔️ Learn Basics: Understand data entry tools like Excel, Google Sheets, and databases.</p>
            <p> ✔️ Improve Typing: Practice typing speed (40-60 WPM) and accuracy using online tools.</p>
            <p> ✔️ Focus on Accuracy: Double-check entries for errors and maintain consistent formatting.</p>
            <p> ✔️ Organize Data: Keep files and databases well-organized and follow data security practices.</p>
        </div>
        <div class="timeline-event">
            <h4>2017 - 2020</h4>
            <p><strong>IT Helper</strong></p>
            <p>Lotus Finance</p>
            <p>Sunakothi, Lalitpur, Nepal</p>
            <p> ✔️ Learn Hardware & Software: Understand computer components, operating systems, and troubleshooting basics.</p>
            <p> ✔️ Master Networking: Learn IP addresses, routers, Wi-Fi setup, and basic network security.</p>
            <p> ✔️ Provide User Support: Assist with software installations, account setups, and resolving technical issues.</p>
            <p> ✔️ Organize Data: Keep files and databases well-organized and follow data security practices.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Area of Expertise and Software Skills in the middle column
with col2:
    # Area of Expertise
    st.subheader("Area of Expertise")
    st.write("- 📊 Data Analysis & Visualization")
    st.write("- 🗄️ Big Data Processing")
    st.write("- 💾 Database Management")
    st.write("- ⚙️ Automation & Optimization")

    # Software Skills
    st.subheader("Software Skills")
    st.write("- **Python 🐍 (🐼 Pandas, 📦 NumPy, 🔬 SciPy, 🤖 Scikit-learn)**")
    st.write("- **SQL (🐘 PostgreSQL, 🛢️ MySQL)**")
    st.write("- **📉 Matplotlib, 🌊 Seaborn, 📈 Plotly**")
    st.write("- **🔗 Git/🐙 GitHub (Octocat)**")

# Empty column for alignment
with col3:
    st.write("")  # Empty space to push content toward the middle

# Education
st.subheader("Education")
st.markdown("""
    <div class="timeline">
        <div class="timeline-event">
            <h4>Nov 2021 - Present</h4>
            <p><strong>Bachelors in Computer Application</strong></p>
            <p>Mega National College</p>
            <p>Kumaripati, Lalitpur, Nepal</p>
        </div>
        <div class="timeline-event">
            <h4>2014 - 2016</h4>
            <p><strong>Computer Science</strong></p>
            <p>United Academy</p>
            <p>Kumaripati, Lalitpur, Nepal</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Footer
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write("")
with col2:
    st.write("**Hi, it’s me Anup Maharjan available to do work**")
with col3:
    st.write("")