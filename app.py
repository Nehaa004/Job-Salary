import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Job Salary Prediction",
    page_icon="💼",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background-color: #f3f4f6;
}

.main-box {
    background-color: white;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.1);
}

.title {
    text-align: center;
    color: #2563eb;
    font-size: 35px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    border: none;
}

.link-btn {
    background: none;
    border: none;
    color: #2563eb;
    cursor: pointer;
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in and st.session_state.page == "login":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown('<div class="main-box">', unsafe_allow_html=True)

        st.markdown(
            '<p class="title">💼 Login</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="subtitle">Job Salary Prediction System</p>',
            unsafe_allow_html=True
        )

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if username != "" and password != "":

                st.session_state.logged_in = True
                st.success("Login Successful ✅")
                st.rerun()

            else:
                st.error("Please enter username and password")

        st.write("")

        st.write("Don't have an account?")

        if st.button("Go to Sign Up"):

            st.session_state.page = "signup"
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SIGNUP PAGE ----------------
elif not st.session_state.logged_in and st.session_state.page == "signup":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown('<div class="main-box">', unsafe_allow_html=True)

        st.markdown(
            '<p class="title">📝 Sign Up</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="subtitle">Create New Account</p>',
            unsafe_allow_html=True
        )

        new_user = st.text_input("Create Username")

        new_email = st.text_input("Email")

        new_password = st.text_input(
            "Create Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Create Account"):

            if (
                new_user != ""
                and new_email != ""
                and new_password != ""
            ):

                if new_password == confirm_password:

                    st.success("Account Created Successfully 🎉")

                    st.session_state.page = "login"

                else:
                    st.error("Passwords do not match")

            else:
                st.error("Please fill all fields")

        st.write("")

        st.write("Already have an account?")

        if st.button("Back to Login"):

            st.session_state.page = "login"
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN APP ----------------
else:

    st.title("💼 Job Salary Prediction System")

    st.success("Welcome! You are logged in.")

    menu = st.radio(
        "Navigation",
        [
            "Home",
            "Salary Prediction",
            "Dashboard",
            "Insights"
        ],
        horizontal=True
    )

    st.sidebar.title("👤 User Profile")

    st.sidebar.write("Neha Kumari")
    st.sidebar.write("BCA Student")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

    # ---------- HOME ----------
    if menu == "Home":

        st.header("🏠 Home")

        st.write("Welcome to the Job Salary Prediction Project.")

    # ---------- PREDICTION ----------
    elif menu == "Salary Prediction":

        st.header("💰 Salary Prediction")

        experience = st.number_input(
            "Experience",
            0,
            40
        )

        skills = st.slider(
            "Skills",
            1,
            10
        )

        certifications = st.slider(
            "Certifications",
            0,
            10
        )

        if st.button("Predict Salary"):

            salary = (
                25000
                + experience * 5000
                + skills * 3000
                + certifications * 2000
            )

            st.success(
                f"Predicted Salary: ₹ {salary:,.2f}"
            )

    # ---------- DASHBOARD ----------
    elif menu == "Dashboard":

        st.header("📊 Dashboard")

        st.line_chart({
            "Salary": [25000, 40000, 60000, 80000]
        })

    # ---------- INSIGHTS ----------
    elif menu == "Insights":

        st.header("📈 Insights")

        st.info(
            "Higher experience and certifications increase salary."
        )
