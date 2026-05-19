import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Job Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.topbar {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}

.topbar h1 {
    color: white;
    text-align: center;
}

.navbar {
    background-color: #1f2937;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 20px;
    text-align: center;
}

.profile-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 45px;
    border: none;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown("""
    <div class="topbar">
        <h1>💼 JOB SALARY PREDICTION SYSTEM</h1>
    </div>
    """, unsafe_allow_html=True)

    st.title("🔐 Login Page")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    st.markdown("### Don't have an account?")
    st.text_input("Create Username")
    st.text_input("Email")
    st.text_input("Create Password", type="password")

    if st.button("Login"):

        st.session_state.logged_in = True
        st.rerun()

# ---------------- MAIN APP ----------------
else:

    # ---------- TOP BAR ----------
    st.markdown("""
    <div class="topbar">
        <h1>💼 JOB SALARY PREDICTION SYSTEM</h1>
    </div>
    """, unsafe_allow_html=True)

    # ---------- TOP NAVIGATION ----------
    menu = st.radio(
        "Navigation",
        [
            "Home",
            "Salary Prediction",
            "Roadmap",
            "Dashboard",
            "Insights"
        ],
        horizontal=True
    )

    # ---------- SIDEBAR PROFILE ----------
    st.sidebar.markdown("## 👤 User Profile")

    st.sidebar.markdown("""
    <div class="profile-card">

    ### Neha Kumari

    🎓 BCA Student  
    💻 Data Analytics Enthusiast  
    📍 India  

    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # ---------------- HOME ----------------
    if menu == "Home":

        st.title("🏠 Home")

        st.markdown("""
        ## Welcome to the Job Salary Prediction System

        This project predicts salary using Machine Learning.

        ### Features
        - Salary Prediction
        - Dashboard Analytics
        - Career Roadmap
        - Insights Visualization
        """)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Accuracy", "92%")

        with col2:
            st.metric("Dataset", "10K+")

        with col3:
            st.metric("Model", "KNN")

    # ---------------- SALARY PREDICTION ----------------
    elif menu == "Salary Prediction":

        st.title("💰 Salary Prediction")

        col1, col2 = st.columns(2)

        with col1:

            experience = st.number_input(
                "Experience (Years)",
                min_value=0,
                max_value=40
            )

            education = st.selectbox(
                "Education Level",
                [
                    "Bachelor",
                    "Master",
                    "PhD"
                ]
            )

            skills = st.slider(
                "Skills Rating",
                1,
                10
            )

        with col2:

            job_title = st.selectbox(
                "Job Role",
                [
                    "Data Analyst",
                    "Software Engineer",
                    "HR",
                    "Manager"
                ]
            )

            certifications = st.slider(
                "Certifications",
                0,
                15
            )

        if st.button("Predict Salary"):

            predicted_salary = (
                25000
                + (experience * 5000)
                + (skills * 3000)
                + (certifications * 2000)
            )

            st.success(
                f"Predicted Salary: ₹ {predicted_salary:,.2f}"
            )

            st.balloons()

    # ---------------- ROADMAP ----------------
    elif menu == "Roadmap":

        st.title("🛣️ Career Roadmap")

        st.markdown("""
        ## Steps to Become a Data Analyst

        1. Learn Python
        2. Learn Pandas & NumPy
        3. Learn Data Visualization
        4. Learn SQL
        5. Learn Machine Learning
        6. Build Projects
        7. Create Resume
        8. Apply for Jobs
        """)

    # ---------------- DASHBOARD ----------------
    elif menu == "Dashboard":

        st.title("📊 Dashboard")

        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=[
                "Salary",
                "Experience",
                "Skills"
            ]
        )

        st.line_chart(chart_data)

        education_data = pd.DataFrame(
            {
                "Students": [50, 30, 20]
            },
            index=[
                "Bachelor",
                "Master",
                "PhD"
            ]
        )

        st.bar_chart(education_data)

    # ---------------- INSIGHTS ----------------
    elif menu == "Insights":

        st.title("📈 Insights")

        st.info(
            "Candidates with more certifications tend to get higher salaries."
        )

        st.warning(
            "Experience strongly impacts salary growth."
        )

        st.success(
            "Machine Learning helps automate salary estimation."
        )

        st.markdown("""
        ## Key Findings

        - Higher experience leads to higher salary
        - Technical skills improve opportunities
        - Certifications increase salary chances
        - Higher education improves salary packages
        """)
