import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from typing import Optional, List, Dict
from jsonschema import validate
from predict.prediction import predict_linear_regression
from validation import validate_json
import os
from preprocessing.cleaning_data import preprocess, raw_data
import pandas as pd


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self) -> str:

        return "The server is alive."


class Predict(Resource):
    "This class is a new ressource for this API. It will manage the prediction part"

    def get(self) -> Dict:
        """
        This function return a dictionary to help the user to know what should be assign
        """
        return {
            "0": {
                "area": "int",
                "property-type": "str",
                "rooms-number": "int",
                "zip-code": "int",
                "land-area":"Optional[int]",
                "garden": "Optional[bool]",
                "garden-area":" Optional[int]",
                "equipped-kitchen": "Optional[bool]",
                "full-address": "Optional[str]",
                "swimming-pool": "Optional[bool]",
                "furnished": "Optional[bool]",
                "open-fire": "Optional[bool]",
                "terrace": "Optional[bool]",
                "terrace-area":" Optional[int]",
                "facades-number":" Optional[int]",
                "building-state": "Optional[str]",
            }
        }

    def post(self) -> Dict:
        """
        This function will manage the post request in the predict ressource.
        it wiil give the prediction if the format is correct else an error message
        """
        myjson: json = request.get_json(force=True)
        # convert the json format in a dictionary
        mydata: Dict = dict(myjson)
        # create a list to save all the messages
        messages: List[str] = []
        messages, mydata = validate_json(mydata)
        if len(messages) == 0:
            df = convert_input(mydata)
            X = preprocess(df)[1]
            price = predict_linear_regression(X)
            return {"prediction": price}
        else:
            return {"error": messages}


def convert_input(mydata: Dict) -> pd.Series:
    """
    This function will convert the input of the user and create new label in
    the dictionary if it doesn't exist
    """
    living_area: str = "Living area"  # "area":int
    property_type: str = "Property type"  # "property-type": str
    bedrooms: int = "Bedrooms"  # "rooms-number": int
    post_code: int = "Post code"  # "zip-code": int

    data_encoded = {0: {}}

    columns = raw_data.columns
    # list of label that exist in the dataset
    my_list = [
        "Immoweb ID",
        "Property type",
        "property sub-type",
        "Price",
        "Post code",
        "Building condition",
        "Kitchen type",
        "Bedrooms",
        "Furnished",
        "Terrace surface",
        "Tenement building",
        "Number of frontages",
        "Swimming pool",
        "How many fireplaces?",
        "Garden",
        "Terrace",
        "Surface of the plot",
        "Living area",
        "Garden surface",
        "Garden orientation",
    ]

    for elem in columns:
        for label in my_list:
            if (
                label != living_area
                or label != property_type
                or label != bedrooms
                or label != post_code
            ):
                if elem == "Immoweb ID":
                    data_encoded[0][elem] = 7921700
                if elem == property_type:
                    data_encoded[0][property_type] = mydata["0"]["property-type"]
                if elem == "property sub-type":
                    data_encoded[0][elem] = "unknown"
                if elem == "Price":
                    data_encoded[0][elem] = 0
                if elem == post_code:
                    data_encoded[0][post_code] = str(mydata["0"]["zip-code"])
                if elem == "Building condition":
                    data_encoded[0][elem] = "bad"
                if elem == "Kitchen type":
                    data_encoded[0][elem] = "super equiped"
                if elem == bedrooms:
                    data_encoded[0][bedrooms] = mydata["0"]["rooms-number"]
                if elem == "Furnished":
                    data_encoded[0][elem] = False
                if elem == "Terrace surface":
                    data_encoded[0][elem] = 20
                if elem == "Tenement building":
                    data_encoded[0][elem] = False
                if elem == "Number of frontages":
                    data_encoded[0][elem] = 0
                if elem == "Swimming pool":
                    data_encoded[0][elem] = True
                if elem == "How many fireplaces?":
                    data_encoded[0][elem] = 0
                if elem == "Garden":
                    data_encoded[0][elem] = 0
                if elem == "Terrace":
                    data_encoded[0][elem] = 0
                if elem == "Surface of the plot":
                    data_encoded[0][elem] = 350
                if elem == living_area:
                    data_encoded[0][living_area] = mydata["0"]["area"]
                if elem == "Garden surface":
                    data_encoded[0][elem] = 0
                if elem == "Garden orientation":
                    data_encoded[0][elem] = 0

    # assign every data in a new dataframe
    df = pd.DataFrame.from_dict(data_encoded, orient="index")

    return df


# add ressource to the api
api.add_resource(HelloWorld, "/")
api.add_resource(Predict, "/predict/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)
