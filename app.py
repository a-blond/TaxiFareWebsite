import streamlit as st
import datetime
import requests
from PIL import Image

image = Image.open("image/taxi.jpg")
st.image(image, caption='Le Wagon', use_column_width=False)

'''
# Predict you taxi's fare in NYC
'''
"## When do you want to take the cab?"
pu_date = st.date_input(
    "Pick up date",
    datetime.date(2021, 6, 26))

pu_time = st.time_input('Pick up time', datetime.time(0, 00))

pu_datetime = f"{pu_date} {pu_time}"

"## From where do you want to take the cab?"
pu_lon = st.number_input("What's your pick up longitude?",
                         value = 40.7614327)

pu_lat = st.number_input("What's your pick up latitude?",
                         value = 73.9798156)

"## Where do you want to go?"
do_lon = st.number_input("What's your drop-off longitude?",
                         value = 50.6413111)

do_lat = st.number_input("What's your drop-off latitude?",
                         value = 73.7803331)

"## Finally, how many passenger do you want to take on board?"
passenger = st.number_input("Number of passenger",
                            min_value = 1,
                            max_value = 8,
                            step = 1)

url = 'https://taxifare.lewagon.ai/predict'

params={"pickup_datetime" : pu_datetime ,
        "pickup_longitude" : pu_lon,
        "pickup_latitude" : pu_lat,
        "dropoff_longitude" : do_lon,
        "dropoff_latitude" : do_lat,
        "passenger_count" : passenger}

response = requests.get(url, params = params).json()

answer = round(response["prediction"],2)
"# Our prediction for your ride"
if st.button('Get fare'):
    # print is visible in server output, not in the page
    print('button clicked!')
    f"$ {answer}"