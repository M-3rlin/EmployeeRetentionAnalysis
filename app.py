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
