from jsonschema import validate
from typing import List,Dict,Optional

def validate_json(mydata):

    area = mydata["data"]["area"]
    property_type = mydata["data"]["property-type"]
    rooms_number = mydata["data"]["rooms-number"]
    zip_code= mydata["data"]["zip-code"]
    land_area= mydata["data"]["land-area"]
    garden = mydata["data"]["garden"]
    garden_area = mydata["data"]["garden-area"]
    equipped_kitchen = mydata["data"]["equipped-kitchen"]
    full_address = mydata["data"]["full-address" ]
    swimming_pool= mydata["data"]["swimming-pool"] 
    furnished = mydata["data"]["furnished"] 
    open_fire = mydata["data"]["open-fire" ]
    terrace = mydata["data"]["terrace"] 
    terrace_area = mydata["data"]["terrace-area"] 
    facades_number = mydata["data"]["facades-number"] 
    building_state = mydata["data"]["building-state" ]    
   
    messages:List = []
    
    try:
        if area != None:
            validate(instance=area, schema={"type":"integer"})

    except:
      messages.append("In your json data, the label named area is suppose to be an integer")
    try:
      validate(instance=property_type, schema={"type":"string"})
    except:
      messages.append("In your json data, the label named 'property typed' is suppose to be an string")
    try:
      validate(instance=rooms_number, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'rooms number' is suppose to be an integer")
    try:
      validate(instance=zip_code, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'zip code' is suppose to be an integer")
    
    try:
      validate(instance=land_area, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'land area' is suppose to be an integer")
    
    try:
      validate(instance=garden, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label named 'garden' is suppose to be an boolean")
    
    try:
      validate(instance=garden_area, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'garden area' is suppose to be an integer")
    
    try:
      validate(instance=equipped_kitchen, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label named 'equipped kitchen' is suppose to be an boolean")
    
    try:
      validate(instance=full_address, schema={"type":"string"})
    except:
      messages.append("In your json data, the label '-full address' area is suppose to be an string")
    try:
      validate(instance=swimming_pool, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label 'swimming pool' area is suppose to be an boolean")

    try:
      validate(instance=furnished, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label named 'furnished' is suppose to be an boolean")
    
    try:
      validate(instance=open_fire, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label named 'open fire' is suppose to be an boolean")
    try:
      validate(instance=terrace, schema={"type":"boolean"})
    except:
      messages.append("In your json data, the label named 'terrace' is suppose to be an boolean")
    try:
      validate(instance=terrace_area, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'terrace area' is suppose to be an integer")
    try:
      validate(instance=facades_number, schema={"type":"integer"})
    except:
      messages.append("In your json data, the label named 'facades number' is suppose to be an integer")
    try:
      validate(instance=building_state, schema={"type":"string"})
    except:
      messages.append("In your json data, the label named 'building state is suppose to be an string")

    return messages

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

