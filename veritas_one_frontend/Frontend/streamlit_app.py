import streamlit as st
import pandas as pd
import os
import sys

# Optionally, adjust the PYTHONPATH so that 'app' is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from the app package (make sure routers.py exists in the app folder)
from app.routers import fax, ifax

# Configure the Streamlit page
st.set_page_config(page_title="Veritas One", layout="wide")

# Simple welcome page
st.title("Welcome to Veritas One")
st.image("logo.png", width=200)  # Ensure you have a logo image file in the correct location
st.subheader("Your Personal Health Record & Data Empowerment")
st.write("This is the main Streamlit app. Expand this file with your UI code.")
