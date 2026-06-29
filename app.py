import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Prediction")

hours = st.number_input("Hours Studied", min_value=0.0)

scores = st.number_input("Previous Scores", min_value=0.0)

activities = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

sleep = st.number_input("Sleep Hours", min_value=0.0)

papers = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0.0
)

# Convert Yes/No to 1/0
activities = 1 if activities == "Yes" else 0

if st.button("Predict"):

    data = [[
        hours,
        scores,
        activities,
        sleep,
        papers
    ]]

    prediction = model.predict(data)

    st.success(
        f"Predicted Performance Index: {prediction[0]:.2f}"
    )