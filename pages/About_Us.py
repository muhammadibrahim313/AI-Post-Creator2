import streamlit as st
from utils import load_css

# Page Configuration
st.set_page_config(page_title="About Us", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>About Us</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Meet the Team Behind AI Post Creator</p>", unsafe_allow_html=True)

# Team Section
st.markdown("<h2 class='sub-title'>Meet Our Team</h2>", unsafe_allow_html=True)

# First Row
team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.markdown(
        """<div class='card'>
            <img src='https://avatars.githubusercontent.com/u/147333130?v=4' alt='M Ibrahim Qasmi' style='width:100px;height:100px;border-radius:50%;'>
            <h3>M Ibrahim Qasmi</h3>
            <p>Team Leader</p>
            <p class='info-text'>Specialist in Data Science</p>
            <a href='https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/muhammadibrahim313' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col2:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D4D35AQEnkHTdeZRKyA/profile-framedphoto-shrink_100_100/profile-framedphoto-shrink_100_100/0/1733436747657?e=1734382800&v=beta&t=FvaCcl1ygY0coLzHpdO6mKGZ48AvOcVW0qF3r9d__4I' alt='TIJANI .S. OLALEKAN' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Musawenkosi Sibeko</h3>
            <p>Software Engineer</p>
            <p class='info-text'>Specialized in Development</p>
            <a href='https://www.linkedin.com/in/sotijani/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/TSOlami' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col3:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D5603AQHD0EFsdU_gYw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1708725952719?e=1739404800&v=beta&t=EKCtvsSrodaJDzOLg5UaBA9vhzPYnZ4yES_mBov2slE' alt='Maryam Sikander' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Yashwanth Doraswamy</h3>
            <p>ML Engineer</p>
            <p class='info-text'>Specialist in Machine Learning</p>
            <a href='https://www.linkedin.com/in/maryamsikander/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/Maryam-Sikander' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

# Second Row
team_col4, team_col5, team_col6 = st.columns(3)

with team_col4:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D4E03AQGj5Gub8Ic3dw/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1722004693756?e=1739404800&v=beta&t=1DgpqNzH9FWppeiytgM6QzTOlb3wUYhzlohIXNA7-uQ' alt='Ahmad Fakhar' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Hassan Mehmood</h3>
            <p>Data Analyst</p>
            <p class='info-text'>Specialist in Data Analysis</p>
            <a href='https://www.linkedin.com/in/ahmad-fakhar77797' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/Ahmad-Fakhar' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col5:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D4D03AQHIyQKry_bncQ/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1727435482174?e=1739404800&v=beta&t=6yWvdGEAGl0Ztaswz0pVk2DKWbu0AKlwdidD5J-p5ug' alt='M Jawad' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Manjunatha Rathod</h3>
            <p>Data Analyst</p>
            <p class='info-text'>Specialist in Data Analysis</p>
            <a href='https://www.linkedin.com/in/muhammad-jawad-86507b201/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/mj-awad17/' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col6:
    st.markdown(
        """<div class='card'>
            <img src='https://avatars.githubusercontent.com/u/149602572?v=4' alt='TAYYAB SAJJAD' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Muhammad Bilal</h3>
            <p>AI Engineer</p>
            <p class='info-text'>Specialist in Web Development</p>
            <a href='https://www.linkedin.com/in/devtayyabsajjad' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/devtayyabsajjad' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

# Contact Section
st.markdown("<h2 class='sub-title'>Get in Touch</h2>", unsafe_allow_html=True)
st.markdown(
    """<div class='card'>
        <h3>Contact Information</h3>
        <p><strong>Email:</strong> team@aipostcreator.com</p>
        <p><strong>GitHub Repository:</strong> <a href='https://github.com/bilal77511/genai_hack' target='_blank'>genai_hack</a></p>
        <p class='info-text'>We're always happy to hear from you! Feel free to reach out with questions, suggestions, or collaboration opportunities.</p>
    </div>""",
    unsafe_allow_html=True
) 