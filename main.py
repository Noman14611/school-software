# main.py

import streamlit as st
from app import run_fee_app
from attendance import run_attendance_app

st.set_page_config(page_title="🏫 School Management", layout="wide")
st.sidebar.title("📂 Select App")

selected_app = st.sidebar.selectbox("Choose Application", [
    "📅 Attendance Tracker",
    "💰 Fee Submission"
])

if selected_app == "📅 Attendance Tracker":
    run_attendance_app()
elif selected_app == "💰 Fee Submission":
    run_fee_app()
