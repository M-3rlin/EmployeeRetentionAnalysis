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
    # variable name changes needed to be made to match clean CSV data headers
    data = {
        'age': age,
        'dailyrate': daily_rate,
        'distancefromhome': distance_from_home,
        'yearsatcompany': years_at_company,
        'department': department,
        'businesstravel': business_travel,
        'jobrole': job_role
    }
    
    # Convert to DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Call the function to capture inputs
input_df = user_input_features()

# Display the inputs on the main page to verify they update
st.subheader('Employee Profile to Assess')
st.dataframe(input_df)

# Create a "Predict" button
if st.button("Predict Retention Risk"):
    
    # remove the 'Attrition' answer key and copy the first employee's data to use as a background template for columns we didn't ask the user for
    X_raw = df.drop(columns=['Attrition'], errors='ignore')
    person = X_raw.iloc[[0]].copy()
    
    # replace the template's default values with the specific details the user entered in the sidebar
    person['age'] = input_df['age'].values[0]
    person['dailyrate'] = input_df['dailyrate'].values[0]
    person['distancefromhome'] = input_df['distancefromhome'].values[0]
    person['yearsatcompany'] = input_df['yearsatcompany'].values[0]
    person['department'] = input_df['department'].values[0]
    person['businesstravel'] = input_df['businesstravel'].values[0]
    person['jobrole'] = input_df['jobrole'].values[0]
    
    # add the user's data to the main list to convert words into numbers correctly, then grab that single row back out
    combined = pd.concat([X_raw, person], axis=0)
    combined_encoded = pd.get_dummies(combined)
    final_input = combined_encoded.tail(1)
    
    # --------------------------------------------------------------------------
    # Ensure the columns match exactly
    # --------------------------------------------------------------------------
    # check exactly which columns the model was trained on and force data to match
    # also deleting extras and filling in missing blanks with zeros.
    # --------------------------------------------------------------------------
    
    try:
        # get the columns the model expects
        model_cols = model.feature_names_in_
        
        # reindex forces our input to match that list exactly, filling missing gaps with 0
        final_input = final_input.reindex(columns=model_cols, fill_value=0)
        
    except AttributeError:
        st.error("Model does not have feature names saved. Please ensure sklearn version >= 1.0")

    # feed the data into the model to get the final verdict (Stay or Leave) and the percentage confidence
    prediction = model.predict(final_input)
    probability = model.predict_proba(final_input)

    # display a Red or Green alert on the screen depending on whether the model predicts the employee will leave or stay
    st.subheader("Prediction Result")
    
    if prediction[0] == 1:
        st.error(f"HIGH RISK: Employee is likely to LEAVE.")
        st.write(f"Confidence: {probability[0][1] * 100:.2f}%")
    else:
        st.success(f"LOW RISK: Employee is likely to STAY.")
        st.write(f"Confidence: {probability[0][0] * 100:.2f}%")