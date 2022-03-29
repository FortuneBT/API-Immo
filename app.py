from flask import Flask, jsonify
from flask_restful import Api,Resource
from typing import Optional,List,Dict


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"message":"Hello World"}


#"building-state": Optional["NEW","GOOD","TO RENOVATE","JUST RENOVATED","TO REBUILD"]
#"property-type": "APARTMENT" | "HOUSE" | "OTHERS"
data = {
  "data": {
    "area": int,
    "property-type": str,
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[str]
  }
}


#output
"""{
  "prediction": Optional[float],
  "error": Optional[str]
}
"""

api.add_resource(HelloWorld,"/")

app.run(debug=True)