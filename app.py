import streamlit as st
import pandas as pd
import joblib

# 1. Load the saved model
# Make sure this file is in the same directory as app.py
model = joblib.load('predictive_maintenance_model.pkl')

# 2. Build the Webpage UI
st.title("⚙️ Predictive Maintenance Dashboard")
st.write("Enter the machine's current sensor readings to predict if it will fail.")

st.header("Sensor Inputs")
col1, col2 = st.columns(2)

with col1:
    air_temp = st.number_input("Air temperature [K]", min_value=250.0, max_value=350.0, value=300.0)
    process_temp = st.number_input("Process temperature [K]", min_value=250.0, max_value=350.0, value=310.0)
    rotational_speed = st.number_input("Rotational speed [rpm]", min_value=0, max_value=5000, value=1500)

with col2:
    torque = st.number_input("Torque [Nm]", min_value=0.0, max_value=100.0, value=40.0)
    tool_wear = st.number_input("Tool wear [min]", min_value=0, max_value=300, value=100)
    
    # Machine Type Dropdown
    machine_type = st.selectbox("Machine Quality Type", ["Low (L)", "Medium (M)", "High (H)"])

# 3. Process Inputs into the format the model expects
# Calculate the engineered features automatically
temp_diff = process_temp - air_temp
power_output = rotational_speed * torque

# Convert dropdown selection into the One-Hot Encoded format (Type_L, Type_M)
type_l = 1 if machine_type == "Low (L)" else 0
type_m = 1 if machine_type == "Medium (M)" else 0

# 4. Create the Predict Button
if st.button("Predict Machine Status", type="primary"):
    
    # Create the dataframe exactly how the model expects it
    input_data = pd.DataFrame({
        'Air temperature [K]': [air_temp],
        'Process temperature [K]': [process_temp],
        'Rotational speed [rpm]': [rotational_speed],
        'Torque [Nm]': [torque],
        'Tool wear [min]': [tool_wear],
        'Temp_Difference': [temp_diff],
        'Power_Output': [power_output],
        'Type_L': [type_l],
        'Type_M': [type_m]
    })
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.divider()
    if prediction[0] == 1:
        st.error("🚨 **ALERT:** The model predicts this machine is at high risk of FAILURE.")
    else:
        st.success("✅ **ALL GOOD:** The model predicts this machine is operating normally.")