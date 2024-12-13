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
            <p>CyberSecurity Analyst</p>
            <p class='info-text'>Specialized in Analysis </p>
            <a href='https://www.linkedin.com/in/musasibeko61' target='_blank'>LinkedIn</a> | 
            <a href='#' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col3:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D5603AQHD0EFsdU_gYw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1708725952719?e=1739404800&v=beta&t=EKCtvsSrodaJDzOLg5UaBA9vhzPYnZ4yES_mBov2slE' alt='Maryam Sikander' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Yashwanth Doraswamy</h3>
            <p>AI Engineer</p>
            <p class='info-text'>Specialist in Machine Learning</p>
            <a href='https://www.linkedin.com/in/yashwanthdoraswamy/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/yashvicky' target='_blank'>GitHub</a>
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
            <a href='https://www.linkedin.com/in/hassan-mehmood-01a3a9247/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/HassanMehmood413' target='_blank'>GitHub</a>
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
            <a href='https://www.linkedin.com/in/manjunath-rathod-7307b6203?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/Vikram299' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col6:
    st.markdown(
        """<div class='card'>
            <img src='https://avatars.githubusercontent.com/u/149602572?v=4' alt='TAYYAB SAJJAD' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Muhammad Bilal</h3>
            <p>AI Researcher</p>
            <p class='info-text'>Specialist in AI </p>
            <a href='https://www.linkedin.com/in/muhammad-bilal-a75782280/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/bilal77511' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )


# Third Row (New Members)
team_col7, team_col8 = st.columns(2)  

with team_col7:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D4D03AQHyH8IOKkxo7A/profile-displayphoto-shrink_400_400/B4DZN23fbWHMAg-/0/1732866084253?e=1739404800&v=beta&t=6OCixH9nxtvKgJvSHjeMG04EPilSrO0lnIotdCF1NWM' alt='Teammate' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Ali Usama</h3>
            <p>Flutter Developer @</p>
            <p class='info-text'>Expert in Andriod</p>
            <a href='https://www.linkedin.com/in/ali-usam4/' target='_blank'>LinkedIn</a> | 
            <a href='https://github.com/Ali-Usam4' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

with team_col8:
    st.markdown(
        """<div class='card'>
            <img src='https://media.licdn.com/dms/image/v2/D4D03AQH48RESdcgtaA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1694808605243?e=1739404800&v=beta&t=KV-CoDAkrjwz5BXbgEQOMQ_yXBeFa2OndjoZs7goc2U' alt='Mentor' style='width:100px;height:100px;border-radius:50%;'>
            <h3>Koyelia Ghosh Roy</h3>
            <p>Project Mentor</p>
            <p class='info-text'>Generative AI Leader @ EXL </p>
            <a href='https://www.linkedin.com/in/koyeliacsmcbap/' target='_blank'>LinkedIn</a> | 
            <a href='#' target='_blank'>GitHub</a>
        </div>""",
        unsafe_allow_html=True
    )

# Contact Section
st.markdown("<h2 class='sub-title'>Get in Touch</h2>", unsafe_allow_html=True)
st.markdown(
    """<div class='card'>
        <h3>Contact Information</h3>
        <p><strong>Email:</strong> oppoibrahim23@gmail.com</p>
        <p><strong>GitHub Repository:</strong> <a href='https://github.com/bilal77511/genai_hack' target='_blank'>genai_hack</a></p>
        <p class='info-text'>We're always happy to hear from you! Feel free to reach out with questions, suggestions, or collaboration opportunities.</p>
    </div>""",
    unsafe_allow_html=True
)
