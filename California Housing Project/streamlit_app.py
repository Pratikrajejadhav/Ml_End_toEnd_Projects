
import numpy as np
import pickle
import pandas as pd
import streamlit as st 



pickle_in = open("linear_housing_model.pkl","rb")
regressior=pickle.load(pickle_in)


def main():
    st.title("Housing Price")
    MedInc = st.text_input("MedInc"," ")
    HouseAge = st.text_input("HouseAge"," ")
    AveRooms = st.text_input("AveRooms"," ")
    AveBedrms = st.text_input("AveBedrms"," ")
    Population = st.text_input("Population"," ")
    AveOccup = st.text_input("AveOccup"," ")
    Latitude = st.text_input("Latitude"," ")
    Longitude = st.text_input("Longitude"," ")
    result=""
    if st.button("Predict"):
        result=regressior.predict([[eval(MedInc), eval(HouseAge), eval(AveRooms), 
                                           eval(AveBedrms),eval(Population), eval(AveOccup), 
                                           eval(Latitude), eval(Longitude)]])
    st.success('The output is {}'.format(result))
    st.write(result)

if __name__=='__main__':
    main()
    
    
    