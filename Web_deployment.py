import numpy as np

import json

import os

import pickle

import joblib

from sklearn.svm import SVC

from azureml.core import Model

from operator import add

from operator import is_

def init():

    global model

    model_name = 'classifier'

    path = Model.get_model_path(model_name)

    model = joblib.load(path)


def predict_batch(centered_elements):
    predicted_elements = [None] * len(centered_elements)
    for x in range(len(centered_elements)):
        predicted_elements[x] = digit_network.predict(centered_elements[x].reshape(1,32,32,3))[0]
    for x in range(len(predicted_elements)):
        predicted_elements[x] = np.argmax(predicted_elements[x])
    return predicted_elements


def run(data):

    try:
        data = json.load(data)['tensor']

        result = predict_batch(data)

        return {'data' : result.tolist() , 'message' : "Successfully classified digit/operator"}

    except Exception as e:

        error = str(e)

        return {'data' : error , 'message' : 'Failed to classify digit/operator'}