import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Prediction")

hours = st.number_input("Hours Studied")
scores = st.number_input("Previous Scores")
activities = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)
sleep = st.number_input("Sleep Hours")
papers = st.number_input(
    "Sample Question Papers Practiced"
)

if activities == "Yes":
    activities = 1
else:
    activities = 0

if st.button("Predict"):

    prediction = model.predict([[
        hours,
        scores,
        activities,
        sleep,
        papers
    ]])

    st.success(
        f"Predicted Performance Index: {prediction.2f}"
    )