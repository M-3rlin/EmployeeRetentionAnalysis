# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Employee Retention Tool", layout="wide")
st.title("Employee Retention Intelligence System")
st.markdown("---")

# Load data and model directly
try:
    df = pd.read_csv('clean_employee_data.csv')
    model = joblib.load('model.pkl')

    # success message verifying online and connected
    st.success("System Status: Online | Connected to Local Server")
    st.balloons()
    
    # preview data
    st.subheader("Data Snapshot")
    st.dataframe(df.head())

except FileNotFoundError:
    st.error("Error: ensure 'clean_employee_data.csv' and 'model.pkl' are in this folder.")

# Building out sidebar for User Inputs
st.sidebar.header("User Input Features")

def user_input_features():
    # Numeric inputs (sliders make for easy adjustment)
    age = st.sidebar.slider('Age', 18, 60, 30)
    daily_rate = st.sidebar.slider('Daily Rate', 100, 1500, 800)
    distance_from_home = st.sidebar.slider('Distance From Home (km)', 1, 30, 10)
    years_at_company = st.sidebar.slider('Years At Company', 0, 40, 5)
    
    # Categorical inputs (drop-down menus)
    department = st.sidebar.selectbox('Department', 
                                      ['Sales', 'Research & Development', 'Human Resources'])
    
    business_travel = st.sidebar.selectbox('Business Travel', 
                                           ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    
    job_role = st.sidebar.selectbox('Job Role', 
                                    ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                     'Manufacturing Director', 'Healthcare Representative', 
                                     'Manager', 'Sales Representative', 
                                     'Research Director', 'Human Resources'])

    # Store in a dictionary
    data = {
        'Age': age,
        'DailyRate': daily_rate,
        'DistanceFromHome': distance_from_home,
        'YearsAtCompany': years_at_company,
        'Department': department,
        'BusinessTravel': business_travel,
        'JobRole': job_role
    }
    
    # Convert to DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Call the function to capture inputs
input_df = user_input_features()

# Display the inputs on the main page to verify they update
st.subheader('Employee Profile to Assess')
st.dataframe(input_df)