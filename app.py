import json
from flask import Flask, jsonify, request
from flask_restful import Api,Resource
from typing import Optional,List,Dict
from jsonschema import validate
from validation import validate_json


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
  def get(self):
    return {"message":"Hello World"}

class Predict(Resource):

  def get(self):
    return {"message":"Using machin learning to predict the price of the house"}

  def post(self):
    myjson:json= request.get_json(force=True)
    mydata:Dict = dict(myjson)
    messages:List[str] = []
    messages = validate_json(mydata)
    if len(messages) == 0:
      return {"response":mydata["data"]["price"]}
    else:
      return {"Error message(s)":messages}


  
#output
"""{
  "prediction": Optional[float],
  "error": Optional[str]
}
"""

api.add_resource(HelloWorld,"/")
api.add_resource(Predict,"/predict/")

app.run(debug=True)