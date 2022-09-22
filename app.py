#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import pickle
import streamlit as st

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

def welcome():
    return 'Welcome All'

# defining the function which will make the prediction using the data which the user inputs
def prediction(hotel, lead_time, country, market_segment,
       distribution_channel, is_repeated_guest, booking_changes,
       deposit_type, agent, days_in_waiting_list, customer_type, adr,
       required_car_parking_spaces, total_of_special_requests, guests,
       room, net_canceled):
    prediction = model.predict([[hotel, lead_time, country, market_segment,
       distribution_channel, is_repeated_guest, booking_changes,
       deposit_type, agent, days_in_waiting_list, customer_type, adr,
       required_car_parking_spaces, total_of_special_requests, guests,
       room, net_canceled]])
    print(prediction)
    return prediction

# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Hotel Booking Cancellation Prediction")
    
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = '''
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1>
    </div>
    '''
    
    # this line allwos us to display the front end aspects we have
    # defined in the code above
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxed in which the user can enter the data
    # required to make the prediction
    
    hotel = st.text_input("Hotel Type", "Type Here")
    lead_time = st.text_input("Lead Time", "Type Here")
    country = st.text_input("Country", "Type Here")
    market_segment = st.text_input("Market Segnment", "Type Here")
    distribution_channel = st.text_input("Distribution Channel", "Type Here")
    is_repeated_guest = st.text_input("Repeated Guest", "Type Here")
    booking_changes = st.text_input("Booking Changes", "Type Here")
    deposit_type = st.text_input("Deposit Type", "Type Here")
    agent = st.text_input("Agent", "Type Here")
    days_in_waiting_list = st.text_input("Days In Waiting List", "Type Here")
    customer_type = st.text_input("Customer Type", "Type Here")
    adr = st.text_input("ADR", "Type Here")
    required_car_parking_spaces = st.text_input("Car Parking Spaces", "Type Here")
    total_of_special_requests = st.text_input("Special Requests", "Type Here")
    guests = st.text_input("Guests", "Type Here")
    room = st.text_input("Room", "Type Here")
    net_canceled = st.text_input("Net Canceled", "Type Here")
    result=""
    
    # the line below ensures that wehn the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(hotel, lead_time, country, market_segment, distribution_channel, is_repeated_guest, booking_changes,deposit_type, agent, days_in_waiting_list, customer_type, adr,required_car_parking_spaces, total_of_special_requests, guests,room, net_canceled)
    st.success('The output is {}'.format(result))
    
if __name__ == '__main__':
    main()

