import json
from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from typing import Optional,List,Dict
from jsonschema import validate
from predict.prediction import predict_linear_regression
from validation import validate_json
import os
from preprocessing.cleaning_data import preprocess, raw_data
import pandas as pd


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
  def get(self):
    #return {"message":"Hello World"}
    return "Welcome to our API - house predict"

class Predict(Resource):

  def get(self):
    return {"message":"Using machin learning to predict the price of the house"}
    

  def post(self):
    myjson:json= request.get_json(force=True)
    mydata:Dict = dict(myjson)
    messages:List[str] = []
    messages,mydata = validate_json(mydata)
    if len(messages) == 0:
      df = convert_input(mydata)
      X = preprocess(df)[1]
      price = predict_linear_regression(X)
      return {"prediction":price}
    else:
      return {"error":messages}




def convert_input(mydata:Dict) -> pd.Series:

  living_area:str = "Living area" # "area":int
  property_type:str = "Property type" #"property-type": str
  bedrooms:int = "Bedrooms" #"rooms-number": int
  post_code:int = "Post code" #"zip-code": int

  data_encoded = {
    0:{}
  }

  columns = raw_data.columns
  my_list = ['Immoweb ID', 'Property type', 'property sub-type', 'Price',
        'Post code', 'Building condition', 'Kitchen type', 'Bedrooms',
        'Furnished', 'Terrace surface', 'Tenement building',
        'Number of frontages', 'Swimming pool', 'How many fireplaces?',
        'Garden', 'Terrace', 'Surface of the plot', 'Living area',
        'Garden surface', 'Garden orientation']

  for elem in columns:
      for label in my_list:
          if label != living_area or label != property_type or label != bedrooms or label != post_code:
              if elem == 'Immoweb ID':
                  data_encoded[0][elem] = 7921700
              if elem == property_type:
                  data_encoded[0][property_type] = mydata["0"]['property-type']
              if elem == 'property sub-type':
                  data_encoded[0][elem] = "unknown"
              if elem == 'Price':
                  data_encoded[0][elem] = 0
              if elem == post_code:
                  data_encoded[0][post_code] = str(mydata["0"]['zip-code'])
              if elem == 'Building condition':
                  data_encoded[0][elem] = "bad"                 
              if elem == 'Kitchen type':
                  data_encoded[0][elem] = "super equiped"
              if elem == bedrooms:
                  data_encoded[0][bedrooms] = mydata["0"]['rooms-number']
              if elem == 'Furnished':
                  data_encoded[0][elem] = False
              if elem == 'Terrace surface':
                  data_encoded[0][elem] = 20
              if elem == 'Tenement building':
                  data_encoded[0][elem] = False
              if elem == 'Number of frontages':
                  data_encoded[0][elem] = 0
              if elem == 'Swimming pool':
                  data_encoded[0][elem] = True
              if elem == 'How many fireplaces?':
                  data_encoded[0][elem] = 0
              if elem == 'Garden':
                  data_encoded[0][elem] = 0
              if elem == 'Terrace':
                  data_encoded[0][elem] = 0
              if elem == 'Surface of the plot':
                  data_encoded[0][elem] = 350
              if elem == living_area:
                  data_encoded[0][living_area] = mydata["0"]['area']
              if elem == 'Garden surface':
                  data_encoded[0][elem] = 0
              if elem == 'Garden orientation':
                  data_encoded[0][elem] = 0

  df = pd.DataFrame.from_dict(data_encoded,orient="index")

  return df


api.add_resource(HelloWorld,"/")
api.add_resource(Predict,"/predict/")

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host="0.0.0.0", threaded=True, port=port)