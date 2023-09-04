# Importing necessary packages
import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Set page title and other configurations
st.set_page_config(page_title="Dashboard | Pharmaceutical Sales Prediction Model", layout="wide")

# Function to load the model
def load_model(file):
    try:
        with open(file, 'rb') as model_file:
            calculator = pickle.load(model_file)
        return calculator
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

# Define the function for prediction
@st.cache()
def prediction(Store, StoreType, DayOfWeek, Promo, StateHoliday, Year, Month, Day, Open, Weekofmonth, SchoolHoliday,
                WeekOfYear, days_to_from_hol, Assortment, CompetitionDistance, CompetitionOpenSinceMonth,
                CompetitionOpenSinceYear, Promo2, Promo2SinceWeek, Promo2SinceYear, PromoInterval):

    # Pre-processing user input
    if Promo == 1:
        Promo = 1
    else:
        Promo = 0

    if StateHoliday == "a":
        StateHoliday = 1
    elif StateHoliday == "b":
        StateHoliday = 2
    elif StateHoliday == "c":
        StateHoliday = 3
    else:
        StateHoliday = 0

    if StoreType == "a":
        StoreType = 1
    elif StoreType == "b":
        StoreType = 2
    elif StoreType == "c":
        StoreType = 3
    else:
        StoreType = 4

    if Assortment == "a":
        Assortment = 0
    elif Assortment == "b":
        Assortment = 1
    else:
        Assortment = 2

    if Promo2 == 1:
        Promo2 = 1
    else:
        Promo2 = 0

    if Promo2SinceWeek == 1:
        Promo2SinceWeek = 1
    else:
        Promo2SinceWeek = 0

    if Promo2SinceYear == 1:
        Promo2SinceYear = 1
    else:
        Promo2SinceYear = 0

    # Making predictions

# Main function for the Streamlit app
def main():
    # Front-end elements of the web page
    st.markdown("<h1 style='color:#0b4eab;font-size:36px;border-radius:10px;'>Dashboard | Pharmaceutical Sales Prediction Model </h1>",
                unsafe_allow_html=True)

    st.sidebar.header("Upload Model")

    # Allow the user to upload the model file
    model_file = st.sidebar.file_uploader("Final_model_04-09-2023-13-06-16-448561.joblib)", type=["joblib"])

    if model_file is not None:
        calculator = load_model(model_file)

    # Input fields for user data
    Store = st.number_input('Enter Store number/Id')
    StoreType = st.selectbox('Select StoreType', ("a", "b", "c", "d"))
    DayOfWeek = st.number_input('Enter DayOfWeek')
    Promo = st.selectbox('Are you in Promo', (1, 0))
    StateHoliday = st.selectbox('Is it StateHoliday', ("a", "b", "c"))
    SchoolHoliday = st.selectbox('Is it SchoolHoliday', (1, 0))
    Year = st.number_input('Enter Year')
    Month = st.number_input('Enter Month')
    Day = st.number_input('Enter Day')
    WeekOfYear = st.number_input('Enter WeekOfYear')
    Weekofmonth = st.number_input('Enter Weekofmonth')

    days_to_from_hol = st.number_input('Enter numbers of days to/from Holiday')
    Assortment = st.selectbox('Choose Assortment', ("a", "b", "c"))
    CompetitionDistance = st.number_input('Enter Competition distance')
    CompetitionOpenSinceMonth = st.number_input('Enter new Competition distance of this month')
    CompetitionOpenSinceYear = st.number_input('Enter new Competition distance of this year')
    Promo2 = st.selectbox('Are you in Promo2', (1, 0))
    Promo2SinceWeek = st.selectbox('Are you in Promo2 this week', (1, 0))
    Promo2SinceYear = st.selectbox('Are you in Promo2 this Year', (1, 0))
    result = ""
    Open = 1
    PromoInterval = 1.0

    # When 'Predict' is clicked, make the prediction and display the result
    if st.button("Predict"):
        result = prediction(Store, StoreType, DayOfWeek, Promo, StateHoliday, Year, Month, Day, Open, Weekofmonth, SchoolHoliday,
                            WeekOfYear, days_to_from_hol, Assortment, CompetitionDistance, CompetitionOpenSinceMonth,
                            CompetitionOpenSinceYear, Promo2, Promo2SinceWeek, Promo2SinceYear, PromoInterval)
        st.success('Your Sales is {}'.format(result))

if __name__ == '__main__':
    main()
