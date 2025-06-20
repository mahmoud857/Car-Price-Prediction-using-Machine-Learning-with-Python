import numpy as np
import Joblib
import streamlit as st
from PIL import Image


loading_model = Joblib.load(open("car_price_prediction_model", "rb"))

def Car_Price_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loading_model.predict(input_data_reshaped)

    return prediction


def main():

    img=Image.open("dataset-cover.jpg")
    st.image(img, caption="Welcome To Car Price Prediction App", use_container_width=True)
    st.markdown("Welcome to the Car Price Prediction App — a tool designed to estimate car prices based on various features.")
    st.markdown("Simply fill in the required information and press 'Predict Car Price' to receive an instant prediction.")

    st.title("Car Price Prediction Web App")
    st.sidebar.markdown("-----")
    st.sidebar.markdown("🧑‍💻 Develop by : Mahmoud Hassan Mahmoud")
    st.sidebar.markdown(" Data scientist&Analytics||Machine Learning Engineer")
    st.sidebar.markdown("📧 Email: mahmoud.ai_0016@ai.kfs.edu.eg")
    st.sidebar.markdown("📞 Phone: +2 0 12 77 42 10 63")
    st.sidebar.markdown("🔗 LinkedIn: www.linkedin.com/in/mahmoudhassanmahmoud")
    st.sidebar.markdown("📄 GitHub: https://github.com/mahmoud857")
    st.sidebar.markdown("🌐 Portfilo: https://taplink.cc/mahmoudhassanmahmoud")
    st.sidebar.markdown("🔗 Kaggle: https://www.kaggle.com/mahmoudhassanmahmoud")



    Year = st.number_input("Year of the Car", min_value=1900, max_value=2050, value=2015)
    Present_Price = st.number_input("Present Price of the Car", min_value=0.0, step=0.01, value=5.0)
    Kms_Driven = st.number_input("Kilometers Driven", min_value=0, step=1000, value=0)


    fuel_type = st.selectbox("Fuel Type", ("Petrol", "Diesel", "CNG"))
    Fuel_Type = 0  
    if fuel_type == "Petrol":
        Fuel_Type = 0
    elif fuel_type == "Diesel":
        Fuel_Type = 1
    else:
        Fuel_Type = 2

    # Seller Type
    seller_type = st.selectbox("Seller Type", ("Individual", "Dealer"))
    Seller_Type = 0 if seller_type == "Individual" else 1

    # Transmission
    transmission_type = st.selectbox("Transmission Type", ("Manual", "Automatic"))
    Transmission = 0 if transmission_type == "Manual" else 1

    # Owner
    Owner = st.selectbox("Number of Previous Owners", (0, 1, 2, 3))

    Car_Price = ""

    if st.button("Predict Car Price"):
        input_data=[Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]
        Car_Price = Car_Price_prediction(input_data)
        st.success(Car_Price)

if __name__ == "__main__":
    main()
