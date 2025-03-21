#!/bin/bash

# Create the main project directory and subdirectories
mkdir -p veritas_one_frontend/app
mkdir -p veritas_one_frontend/Frontend

# Create __init__.py files to mark directories as packages
touch veritas_one_frontend/app/__init__.py
touch veritas_one_frontend/Frontend/__init__.py

# Create a sample streamlit_app.py in the Frontend folder
cat << 'EOF' > veritas_one_frontend/Frontend/streamlit_app.py
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
EOF

# Create a sample routers.py in the app folder
cat << 'EOF' > veritas_one_frontend/app/routers.py
# Sample content for routers.py

def fax():
    return "fax function placeholder"

def ifax():
    return "ifax function placeholder"
EOF

# Create a basic requirements.txt file
cat << 'EOF' > veritas_one_frontend/requirements.txt
streamlit
pandas
EOF

# Create a simple README.md file
cat << 'EOF' > veritas_one_frontend/README.md
# Veritas One Frontend

This is the frontend for Veritas One built with Streamlit.
EOF

echo "Project setup complete."
echo "To run the Streamlit app, execute the following commands:"
echo "cd veritas_one_frontend/Frontend"
echo "streamlit run streamlit_app.py"