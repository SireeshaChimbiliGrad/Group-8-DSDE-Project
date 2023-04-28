from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy as np
import pandas as pd
import pickle
model = pickle.load(open('model_updated.pkl','rb'))
#decorator to access the app
@app.route("/")
@app.route("/index_modified")
def index():
    return render_template("index_modified.html")

#decorator to access the service
@app.route("/cropPredict", methods=['GET', 'POST'])
def cropPredict():

    #extract form inputs
    average_rain_fall_mm_per_year = request.form.get("average_rain_fall_mm_per_year")
    pesticides_tonnes= request.form.get("pesticides_tonnes")
    avg_temp = request.form.get("avg_temp")
    Area = request.form.get("Area")
    Item = request.form.get("Item")


    array1 = np.array([Area,Item,average_rain_fall_mm_per_year,pesticides_tonnes,avg_temp])
    # from sklearn.preprocessing import MinMaxScaler
    # scaler=MinMaxScaler()
    # array1 = array1.reshape(1, -1)
    # input=scaler.fit_transform(array1)
    #extract data from json

    pred = model.predict([array1])

    # return render_template("index.html", average_rain_fall_mm_per_year = average_rain_fall_mm_per_year, pesticides_tonnes = pesticides_tonnes, avg_temp = avg_temp,Area=Area,Item=Item, data = pred[0])
    return render_template("index_modified.html", data = pred[0])

    # result = pred[0]
    # if(pred ==0):
    #     result = "Yes"
    # elif(pred==1):
    #     result = "No"
    # elif(pred==2):
    #     result = "May be"
        

    # output = {
    #     "Area": Area, 
    #     "Item": Item, 
    #     "average_rain_fall_mm_per_year": average_rain_fall_mm_per_year, 
    #     "pesticides_tonnes": pesticides_tonnes, 
    #     "avg_temp": avg_temp,
    # }
    #url for car classification api
    #url = "http://localhost:5000/api"
    #url = "https://dsm-car-model.herokuapp.com/api"

 
    #post data to url
    #results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    