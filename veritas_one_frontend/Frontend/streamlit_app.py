import streamlit as st
import pandas as pd

# Configure the Streamlit page
st.set_page_config(page_title="Veritas One", layout="wide")

# Sidebar Navigation with all pages
pages = [
    "Welcome",
    "About Us",
    "Create Account",
    "Login",
    "Dashboard (User Profile)",
    "Encounter Record",
    "Settings & Privacy",
    "Notifications",
    "Search",
    "FAQs & Support",
    "Security & Privacy Disclosures"
]
selected_page = st.sidebar.selectbox("Navigation", pages)

# ----- Welcome Page -----
if selected_page == "Welcome":
    st.title("Welcome to Veritas One")
    st.image("logo.png", width=200)  # Ensure logo.png is in the current working directory
    st.subheader("Your Personal Health Record & Data Empowerment")
    st.write(
        """
        At Veritas One, we provide you with a free, unified electronic health record (EMR)—a single place where all your medical data is securely stored, always available, and completely under your control.

        But that’s just the beginning. Unlike other platforms, we empower you to take control of your health data, allowing you to monetize it on your own terms while contributing to groundbreaking medical research and industry innovation.

        We believe your health data is one of your most valuable assets—and you should be the one to control it.

        Most hospitals, insurance companies, and tech companies already collect and use your patient data—but they do it behind closed doors, without compensating you.

        We’re different. We put you in control, allowing you to:

        - **Improve Your Own Healthcare:** Faster, better care – doctors make better decisions when they see your full medical history.
        - **Easier Second Opinions:** No more faxing records or re-explaining your history.
        - **Avoid Duplicate Tests & Procedures:** Save time, money, and unnecessary treatments.
        - **Advance Medicine & Improve Patient Care (If You Choose To):** Help researchers discover new treatments and improve existing ones.
        - **Earn Money From Your Data (Only If You Opt In):** Receive a portion of the profits generated from your data.

        At Veritas One, you own your health data, you control its use, and you benefit from it.
        """
    )
    st.subheader("How Your Health Data is Stored & Used")
    st.write(
        """
        At Veritas One, we use a three-database system to keep your identifiable and de-identified data separate. This ensures your privacy while still allowing you to benefit from data sharing.

        **Your Personal Health Record (Your Unified EMR - Secure & Private)**
        - **What it includes:**
          - Your entire medical history—lab results, imaging, medications, provider notes, and more.
          - Data from all your past providers, hospitals, and clinics, even across different systems.
          - Ongoing updates—whenever you visit a doctor, your records are automatically updated.
        - **How it helps you:**
          - No more scrambling to track down old records.
          - No more repeating tests because one hospital can’t see what another ordered.
          - A single, comprehensive record helps you get better care.
        - **How it’s used:**
          - For personal use—access, manage, and share your records anytime.
          - For your medical care—share records instantly with doctors or family.
          - For optional personalized opportunities—if you opt in, we can match you with clinical trials, new medications, or exclusive savings.

        **Your De-Identified Data (For Research & Medical Advancements - Always Anonymous)**
        - **What it includes:**
          - Medical conditions, treatments, lab values, and imaging findings (all personal identifiers removed).
        - **Why it matters:**
          - Helps researchers identify trends in diseases and treatment effectiveness.
          - Supports public health efforts.

        **Limited Identifiable Dataset**
        - Your data is already being monetized by others—unlike them, you control your identifiable data and decide whether to opt in for personalized opportunities.
        """
    )
    # Define the table data for sharing options
    table_data = {
        "Sharing Option": [
            "Strict Privacy Mode (No Sharing)",
            "De-Identified Research Only",
            "Full Data Sharing (Research + Ads)"
        ],
        "How Your Data is Used": [
            "Your data is stored for your personal use only.",
            "Your anonymous health data is used to improve medicine and public health.",
            "Your de-identified data is used for research, AND if you opt in, limited identifiable data (such as medications) can be used for personalized health offers."
        ],
        "Compensation": [
            "No compensation.",
            "You receive 5% of research profits.",
            "You receive 15% of total profits."
        ]
    }
    df = pd.DataFrame(table_data)
    st.table(df)

# ----- About Us Page -----
elif selected_page == "About Us":
    st.title("About Veritas One")
    st.subheader("Empowering Patients Through Transparent Data Management")
    st.write(
        """
        At Veritas One, our vision is to empower patients by putting control of their healthcare data directly in their hands.
        Founded by Dr. Brandon Thomas Gaston MD—a resident physician at Massachusetts General Hospital & Harvard Medical School—we are on a mission to revolutionize how medical records and imaging data are managed and shared.

        Our free, unified electronic health record (EMR) platform consolidates your medical data from every provider and hospital into one secure, patient-centered repository. By integrating advanced technologies—from real-time FHIR API connections to secure DICOM imaging retrieval—Veritas One ensures that your complete medical history is always accessible, streamlining care, reducing repetitive tests, and enabling more informed clinical decisions.

        What sets us apart is our ethical, patient-first approach to data sharing. You decide how your information is used with three customizable sharing modes:
        - **Strict Privacy Mode:** Your data is for your eyes only.
        - **De-Identified Research Only:** Contribute anonymously to research while earning a share of the profits.
        - **Full Data Sharing (Research + Ads):** Opt in for personalized health offers and greater rewards.

        Join us on our journey to redefine the future of healthcare—where your data, your decisions, and your health truly come first.

        For inquiries, please reach out at: bgaston@mgh.harvard.edu
        """
    )

# ----- Create Account Page -----
elif selected_page == "Create Account":
    st.title("Create Account")
    st.write("Fill out the form below to create your account.")
    with st.form("create_account_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        email = st.text_input("Email")
        st.write("Digital Health Record Release Agreement")
        agree = st.checkbox("I agree to the digital health record release.")
        st.write("Select your data sharing option:")
        sharing_option = st.radio(
            "Data Sharing Options",
            (
                "Strict Privacy Mode (No Sharing)",
                "De-Identified Research Only (5% of research profits)",
                "Full Data Sharing (Research +