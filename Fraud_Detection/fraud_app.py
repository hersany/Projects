from flask import Flask, request
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle

app = Flask(__name__)

#with open('features.pkl', 'rb') as m:
#   features = pickle.load(m)

with open('model', 'rb') as m:
    model = pickle.load(m)

@app.route('/fraud')
def index():
    return 'server is up and running'

@app.route('/predict', methods = ['GET', 'POST'])
def predict():

    json_data = request.get_json()         # json_Data = request.data     get_json() is better

    if not all(k in json_data for k in ['V1', 'V2', 'V3', 'V4', 'Amount']):
        return "Not enough data to make a prediction!"

    df = pd.DataFrame.from_dict([json_data])

    df = MinMaxScaler().fit_transform(df)

    prediction = model.predict(df)

    return str(prediction[0])

app.run()