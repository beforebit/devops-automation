# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 16:46:27 2018

@author: Deepak.J
"""

#import pickle
from flask import Flask, request
#from flasgger import Swagger    
#import numpy as np
#import pandas as pd
import json
#with open('./rf.pkl', 'rb') as model_file:
#    model = pickle.load(model_file)

app = Flask(__name__)

#swagger = Swagger(app)

@app.route("/predict")
def predict_iris():
    """Example endpoint returning a prediction of iris data
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
    """
    s_length = request.args.get("s_length")
#    s_width = request.args.get("s_width")
#    p_length = request.args.get("p_length")
#    p_width = request.args.get("p_width")

#    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str("Hello World" + s_length)


@app.route("/predict_file", methods=['POST'])
def predict_file():
    #return request.get_jsons()
    return str(request.files.get_json("input"))




if __name__=='__main__':
   app.run(port=8080)