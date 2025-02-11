import streamlit as st
import pandas as pd
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8000/predict"  # Update with your actual FastAPI endpoint

def make_prediction(input_data):
    response = requests.post(FASTAPI_URL, json=input_data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error in prediction.")
        return None

# Streamlit App
st.set_page_config(page_title="Depression Prediction", page_icon=":brain:", layout="wide")

# Header section
st.title("Depression Prediction")
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            color: #2E8B57;
            font-size: 36px;
            font-weight: bold;
        }
        .description {
            font-size: 18px;
            color: #4B0082;
        }
    </style>
    """, unsafe_allow_html=True)

# Inputs section
st.subheader("Enter your details:")

# Use columns to organize inputs neatly
col1, col2 = st.columns(2)

with col1:
    # City selection
    city = st.selectbox("Select your City", ['Visakhapatnam', 'Bangalore', 'Srinagar', 'Varanasi', 'Jaipur', 'Pune', 'Thane', 'Chennai', 'Nagpur', 'Nashik', 'Vadodara', 'Kalyan', 'Rajkot', 'Ahmedabad', 'Kolkata', 'Mumbai', 'Lucknow', 'Indore', 'Surat', 'Ludhiana', 'Bhopal', 'Meerut', 'Agra', 'Ghaziabad', 'Hyderabad', 'Vasai-Virar', 'Kanpur', 'Patna', 'Faridabad', 'Delhi', 'Other'], index=None, placeholder="Select City...")
    Sleep_Duration = st.selectbox("Select Sleep Duration", ['Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours'], index=None, placeholder="Select Sleep Duration...")
    Majer = st.selectbox("Select your Major Degree", ["12th Grade (Higher Secondary School)", "Bachelor of Education", "Bachelor of Commerce", "Bachelor of Architecture", "Bachelor of Computer Applications", "Master of Science", "Bachelor of Technology", "Master of Computer Applications", "Master of Technology", "Bachelor of Hotel Management", "Bachelor of Science", "Master of Education", "Bachelor of Pharmacy", "Master of Commerce", "Bachelor of Medicine", "Bachelor of Surgery", "Bachelor of Business Administration", "Bachelor of Laws", "Bachelor of Engineering", "Bachelor of Arts", "Master of Pharmacy", "Doctor of Medicine", "Master of Business Administration", "Master of Arts", "Doctor of Philosophy", "Master of Laws", "Master of Hospital Management", "Master of Engineering", "Other qualifications (not specified)"], index=None, placeholder="Select Major Degree...")
    
    gender = st.radio("Gender", ["Female", "Male"], index=None)
    suicidal = st.radio("Ever had suicidal thoughts?", ["Yes", "No"], index=None)
    Family = st.radio("Family History of Mental Illness?", ["Yes", "No"], index=None)
    Dietary_abits = st.radio("Dietary Habits", ["Healthy", "Moderate", "Unhealthy"], index=None)
    
with col2:
    # Other Inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=25)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.0)
    work_study_hours = st.number_input("Work/Study Hours", min_value=0, max_value=12, value=8)
    study_satisfaction = st.slider("Study Satisfaction", 1, 5, 3)
    academic_pressure = st.slider("Academic Pressure", 1, 5, 5)
    work_pressure = st.slider("Work Pressure", 1, 5, 5)
    job_satisfaction = st.slider("Job Satisfaction", 1, 5, 3)
    financial_stress = st.slider("Financial Stress", 1, 5, 5)

   
gender_map = {'Male': 1, 'Female': 0}
Gende = gender_map.get(gender)

city_counts = {
    "Kalyan": 1573, "Srinagar": 1374, "Hyderabad": 1340, "Vasai-Virar": 1291, "Lucknow": 1156,
    "Thane": 1142, "Ludhiana": 1113, "Agra": 1095, "Surat": 1078, "Kolkata": 1067, "Jaipur": 1037,
    "Patna": 1009, "Visakhapatnam": 971, "Pune": 968, "Ahmedabad": 951, "Bhopal": 935, "Chennai": 886,
    "Meerut": 825, "Rajkot": 816, "Delhi": 769, "Bangalore": 768, "Ghaziabad": 745, "Mumbai": 699,
    "Vadodara": 694, "Indore": 644, "Kanpur": 609, "Nashik": 547, "Faridabad": 462, "Nagpur": 456,'others': 1
}
Cit=city_counts.get(city)

Sleep_Duration_map = {'Less than 5 hours': 1, '7-8 hours': 2, '5-6 hours': 3, 'More than 8 hours': 4, 'Others': 1}
Sleep_Durat=Sleep_Duration_map.get(Sleep_Duration)

Dietary_Habits_map = {
    'Unhealthy': 1,  # Least healthy
    'Moderate': 2,   # In between
    'Healthy': 3    # Most healthy
}
Dietary_Habits=Dietary_Habits_map.get(Dietary_abits)

Suicidal_Thoughts_map = {'Yes': 1, 'No': 0}
Suicidal_Thoughts=Suicidal_Thoughts_map.get(suicidal)

Family_History_Mental_Illness_map = {'Yes': 1, 'No': 0}
Family_History_Mental_Illness=Family_History_Mental_Illness_map.get(Family)

category_full_Majer = {
    "12th Grade (Higher Secondary School)": "Class 12","Bachelor of Education": "B.Ed","Bachelor of Commerce": "B.Com","Bachelor of Architecture": "B.Arch","Bachelor of Computer Applications": "BCA","Master of Science": "MSc","Bachelor of Technology": "B.Tech","Master of Computer Applications": "MCA","Master of Technology": "M.Tech","Bachelor of Hotel Management": "BHM","Bachelor of Science": "BSc","Master of Education": "M.Ed","Bachelor of Pharmacy": "B.Pharm","Master of Commerce": "M.Com","Bachelor of Medicine, Bachelor of Surgery": "MBBS","Bachelor of Business Administration": "BBA","Bachelor of Laws": "LLB","Bachelor of Engineering": "BE","Bachelor of Arts": "BA","Master of Pharmacy": "M.Pharm","Doctor of Medicine": "MD","Master of Business Administration": "MBA","Master of Arts": "MA","Doctor of Philosophy": "PhD","Master of Laws": "LLM","Master of Hospital Management": "MHM","Master of Engineering": "ME","Other qualifications (not specified)": "Others"
}
Degree=category_full_Majer.get(Majer)
category_counts = {
    "Class 12": 6080, "B.Ed": 1867, "B.Com": 1506, "B.Arch": 1478, "BCA": 1433, "MSc": 1190, "B.Tech": 1152,
    "MCA": 1044, "M.Tech": 1022, "BHM": 925, "BSc": 888, "M.Ed": 821, "B.Pharm": 810, "M.Com": 734,
    "MBBS": 696, "BBA": 696, "LLB": 671, "BE": 613, "BA": 600, "M.Pharm": 582, "MD": 572, "MBA": 562,
    "MA": 544, "PhD": 522, "LLM": 482, "MHM": 191, "ME": 185, "Others": 35
}
Deg=category_counts.get(Degree)

Prid=[Gende, age, Cit, academic_pressure, work_pressure,
       cgpa, study_satisfaction, job_satisfaction, Sleep_Durat,
       Dietary_Habits, Deg, Suicidal_Thoughts, work_study_hours,
       financial_stress, Family_History_Mental_Illness]

st.markdown("---")
if st.button("Predict"):
    st.subheader("Prediction Result:")
    result = make_prediction(Prid)
    if result:
        st.success(f"The probability of having depression: {result}")
    else:
        st.error("Error in prediction.")


# Add some styling for better UI experience
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px 20px;
            width: 200px;
        }
    </style>
    """, unsafe_allow_html=True)

# Ensure the button is displayed
st.markdown(
    """
    <style>
        .block-container {
            padding: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)
