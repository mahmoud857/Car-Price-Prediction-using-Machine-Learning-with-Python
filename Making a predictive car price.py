# This code is for making a prediction using a pre-trained car price prediction model.
# Importing necessary libraries
import pickle 
import pandas as pd 
import numpy as np 
# Loading the pre-trained model from a file
load_model=pickle.load(open("F:\ماشين ليرنج\مشاريع ماشين ليرنج end to end\Project 6 Car Price Prediction using Machine Learning with Python\car_price_prediction_model","rb"))
# The input data for prediction
# The input data consists of the following features:
input_data=(2014,5.59,27000,0,1,1,0)


# Converting the input data into a numpy array
# The input data is reshaped to match the model's expected input shape
input_data_asarray=np.asarray(input_data)
input_data_reshape=input_data_asarray.reshape(1,-1)

# Making a prediction using the loaded model
prediction=load_model.predict(input_data_reshape)
# The prediction is the estimated price of the car based on the input features
# Displaying the predicted price
print("the predicted price of the car is :",prediction[0])