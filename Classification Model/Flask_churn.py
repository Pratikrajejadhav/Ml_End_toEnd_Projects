
import numpy as np
import joblib
import pandas as pd
from flask import Flask, request

#model.joblib is used to get the predictions on new data
# in this page np pd joblib we did not used it is masked
# yellow error 


app=Flask(__name__)

# joblib_in = open("'best_random_forest.joblib'","rb")
classifier=joblib.load(open('best_random_forest.joblib', 'rb'))


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["GET"])
def predict_note_authentication():
    input_cols=['gender', 'age', 'no_of_days_subscribed', 'multi_screen',
       'mail_subscribed', 'weekly_mins_watched', 'minimum_daily_mins',
       'maximum_daily_mins', 'weekly_max_night_mins', 'videos_watched',
       'maximum_days_inactive', 'customer_support_calls']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        print(val)
        list1.append(eval(val))
    


    prediction=classifier.predict([list1])   # list of list

    
    print(prediction)
    return "Hello, The Churn is"+ str(prediction)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)