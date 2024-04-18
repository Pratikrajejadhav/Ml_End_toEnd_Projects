
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to get the predictions on new data
# in this page np pd pickle we did not used it is masked
# yellow error 


app=Flask(__name__)

pickle_in = open("linear_housing_model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["GET"])
def predict_note_authentication():
    input_cols=['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
                'Population', 'AveOccup', 'Latitude', 'Longitude']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))


    prediction=classifier.predict([list1])   # list of list

    
    print(prediction)
    return "Hello, The House Prediction is"+str(prediction)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)