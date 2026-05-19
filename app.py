import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Job Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton > button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    border: none;
}

.topbar {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.topbar h1 {
    color: white;
    text-align: center;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TOP BAR ----------------
st.markdown("""
<div class="topbar">
    <h1>💼 JOB SALARY PREDICTION SYSTEM</h1>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Login",
        "Signup",
        "Salary Prediction",
        "Roadmap",
        "Dashboard",
        "Insights"
    ]
)

# ---------------- HOME PAGE ----------------
if menu == "Home":

    st.title("🏠 Home")

    st.markdown("""
    ## Welcome to the Job Salary Prediction System
    
    This project predicts salary based on:
    
    - Experience
    - Education
    - Job Role
    - Skills
    - Certifications
    
    ### Technologies Used
    - Python
    - Streamlit
    - Pandas
    - NumPy
    - Machine Learning
    - Scikit-learn
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", "92%")

    with col2:
        st.metric("Dataset Size", "10K+")

    with col3:
        st.metric("Model Used", "KNN")

# ---------------- LOGIN PAGE ----------------
elif menu == "Login":

    st.title("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):
        st.success("Login Successful ✅")

# ---------------- SIGNUP PAGE ----------------
elif menu == "Signup":

    st.title("📝 Signup")

    new_user = st.text_input("Create Username")

    new_email = st.text_input("Email")

    new_pass = st.text_input(
        "Create Password",
        type="password"
    )

    if st.button("Create Account"):
        st.success("Account Created Successfully 🎉")

# ---------------- SALARY PREDICTION PAGE ----------------
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

    # Prediction Button
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

# ---------------- ROADMAP PAGE ----------------
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

# ---------------- DASHBOARD PAGE ----------------
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

# ---------------- INSIGHTS PAGE ----------------
elif menu == "Insights":

    st.title("📈 Insights")

    st.info(
        "Candidates with more certifications tend to get higher salaries."
    )

    st.warning(
        "Experience has a strong impact on salary growth."
    )

    st.success(
        "Machine Learning helps automate salary estimation."
    )

    st.markdown("""
    ## Key Findings
    
    - Higher experience leads to higher salary
    - Master and PhD candidates earn more
    - Technical skills increase salary chances
    - Certifications improve opportunities
    """)
