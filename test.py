from distutils.log import debug
from re import L
from flask import Flask, jsonify
from flask_restful import Api,Resource
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"message":"Hello World"}
    
    def post(self,response):
        return {"message":f"Hello dear {response}"}


api.add_resource(HelloWorld,"/")


app.run(debug=True)