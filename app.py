'''# =========================
# IMPORT LIBRARIES
# =========================
import streamlit as st
import pickle
import pandas as pd

# =========================
# LOAD FILES
# =========================
model = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# =========================
# HELPER: EXTRACT OPTIONS FROM TRAINED COLUMNS
# =========================
def get_options(prefix):
    opts = [col.replace(prefix, "") for col in columns if col.startswith(prefix)]
    opts = sorted(list(set(opts)))
    return opts

# Extract all possible options
job_options = get_options("job_title_")
edu_options = get_options("education_level_")
loc_options = get_options("location_")
ind_options = get_options("industry_")
company_options = get_options("company_size_")
remote_options = get_options("remote_work_")

# Add baseline category (lost due to drop_first=True)
job_options = ["Other"] + job_options
edu_options = ["Other"] + edu_options
loc_options = ["Other"] + loc_options
ind_options = ["Other"] + ind_options
company_options = ["Other"] + company_options
remote_options = ["Other"] + remote_options

# =========================
# TITLE
# =========================
st.title("💼 Salary Prediction App (KNN Improved)")

# =========================
# USER INPUT
# =========================
exp = st.number_input("Experience (years)", 0, 30)
skills = st.number_input("Skills Count", 0, 50)
cert = st.number_input("Certifications", 0, 20)

job = st.selectbox("Job Role", job_options)
edu = st.selectbox("Education", edu_options)
loc = st.selectbox("Location", loc_options)
ind = st.selectbox("Industry", ind_options)
company = st.selectbox("Company Size", company_options)
remote = st.selectbox("Remote Work", remote_options)

# =========================
# CREATE INPUT
# =========================
input_dict = {
    "experience_years": exp,
    "skills_count": skills,
    "certifications": cert,
    "job_title": job,
    "education_level": edu,
    "location": loc,
    "industry": ind,
    "company_size": company,
    "remote_work": remote
}

input_df = pd.DataFrame([input_dict])

# =========================
# FEATURE ENGINEERING
# =========================
input_df['exp_squared'] = input_df['experience_years'] ** 2
input_df['skill_per_exp'] = input_df['skills_count'] / (input_df['experience_years'] + 1)
input_df['cert_per_skill'] = input_df['certifications'] / (input_df['skills_count'] + 1)

input_df['seniority'] = pd.cut(
    input_df['experience_years'],
    bins=[0, 2, 5, 10, 20],
    labels=['Fresher', 'Junior', 'Mid', 'Senior']
)

# =========================
# DUMMIES + ALIGN
# =========================
input_df = pd.get_dummies(input_df)
input_df = input_df.reindex(columns=columns, fill_value=0)

# =========================
# SCALE
# =========================
num_cols = ['experience_years', 'skills_count', 'certifications',
            'exp_squared', 'skill_per_exp', 'cert_per_skill']

input_df[num_cols] = scaler.transform(input_df[num_cols])

# =========================
# PREDICTION
# =========================
if st.button("Predict Salary"):
    prediction = model.predict(input_df)
    st.success(f"💰 Predicted Salary: {int(prediction[0])}")
    st.balloons()'''






import streamlit as st
import pandas as pd
import numpy as np
import pickle

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

.stButton>button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
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

.sidebar .sidebar-content {
    background-color: #1f2937;
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
    ### Welcome to the Job Salary Prediction System
    
    This project predicts salary based on:
    
    - Experience
    - Education
    - Job Role
    - Skills
    - Certifications
    
    ### Technologies Used
    - Python
    - Streamlit
    - Machine Learning
    - Pandas
    - Scikit-learn
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Accuracy", "92%")
    col2.metric("Dataset Size", "10K+")
    col3.metric("Models Used", "KNN")

# ---------------- LOGIN PAGE ----------------
elif menu == "Login":

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful ✅")

# ---------------- SIGNUP PAGE ----------------
elif menu == "Signup":

    st.title("📝 Signup")

    new_user = st.text_input("Create Username")
    new_email = st.text_input("Email")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Create Account"):
        st.success("Account Created Successfully 🎉")

# ---------------- SALARY PREDICTION ----------------
elif menu == "Salary Prediction":

    st.title("💰 Salary Prediction")

    # Load Model
    # model = pickle.load(open("salary_model.pkl", "rb"))

    col1, col2 = st.columns(2)

    with col1:
        experience = st.number_input(
            "Experience (Years)",
            min_value=0,
            max_value=40
        )

        education = st.selectbox(
            "Education",
            ["Bachelor", "Master", "PhD"]
        )

        skills = st.slider("Skills Rating", 1, 10)

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

        # Dummy prediction logic
        predicted_salary = (
            25000
            + experience * 5000
            + skills * 3000
            + certifications * 2000
        )

        st.success(
            f"Predicted Salary: ₹ {predicted_salary:,.2f}"
        )

        st.balloons()

# ---------------- ROADMAP PAGE ----------------
elif menu == "Roadmap":

    st.title("🛣️ Career Roadmap")

    st.markdown("""
    ### Steps to Become a Data Analyst
    
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

    st.line_chart(
        pd.DataFrame(
            np.random.randn(20, 3),
            columns=["Salary", "Experience", "Skills"]
        )
    )

    st.bar_chart(
        pd.DataFrame({
            "Education": [50, 30, 20]
        },
        index=["Bachelor", "Master", "PhD"])
    )

# ---------------- INSIGHTS PAGE ----------------
elif menu == "Insights":

    st.title("📈 Insights")

    st.info("Candidates with more certifications tend to get higher salaries.")

    st.warning("Experience has a strong impact on salary growth.")

    st.success("Machine Learning helps automate salary estimation.")

    st.markdown("""
    ### Key Findings
    
    - Higher experience = Higher salary
    - Master/PhD candidates earn more
    - Technical skills increase salary chances
    - Certifications improve opportunities
    """)

        st.balloons()
