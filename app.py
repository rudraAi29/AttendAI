import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="AttendAI Dashboard", page_icon="📊", layout="wide")

st.title("📊 AttendAI - Smart Attendance Dashboard")
st.markdown("Real-time attendance tracking system powered by FastAPI and Computer Vision.")

# Backend API URL (pointing to your local server)
API_URL = "http://127.0.0.1:8000/students/"

# Refresh Button
if st.button("🔄 Refresh Attendance List"):
    st.rerun()

try:
    # Fetch student data from FastAPI backend
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        
        if students:
            st.subheader("📋 Class Attendance Status")
            
            # Display data in a clean table format
            for student in students:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{student['name']}**")
                with col2:
                    if student['status'] == "Present":
                        st.success("Present")
                    else:
                        st.error("Absent")
        else:
            st.info("No students registered in the database yet. Use the check-in script or Swagger UI to add some!")
    else:
        st.error("Failed to connect to the backend server.")
except Exception as e:
    st.error(f"Error connecting to FastAPI backend: {e}")