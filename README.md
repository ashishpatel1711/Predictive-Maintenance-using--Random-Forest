# Industrial Predictive Maintenance Model

## Overview
This project uses a Random Forest Classifier to predict machine failures based on sensor data. The goal is to identify potential breakdowns before they happen, minimizing downtime.
LIVE DEMO
https://predictive-maintenance-using--random-forest.streamlit.app/

## Data
The dataset contains 10,000 data points from industrial machines, including:
* Air and Process temperatures
* Rotational speed and Torque
* Tool wear

## Model Performance
* **Algorithm:** Random Forest Classifier
* **Accuracy:** 99.95%
* Successfully caught 66 out of 68 actual machine failures in testing.

## Key Features Created
* `Temp_Difference`: Difference between process and air temperature.
* `Power_Output`: Calculated using rotational speed and torque.
