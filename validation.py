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
        else:
          messages.append("In your json data, the label named 'area' is 'None'! You need a value")
    except:
      messages.append("In your json data, the label named area is suppose to be an integer")
    try:
      if property_type != None:
        validate(instance=property_type, schema={"type":"string"})
      else:
          messages.append("In your json data, the label named 'property typed' is 'None'! You need a value")
    except:
      messages.append("In your json data, the label named 'property typed' is suppose to be an string")
    try:
      if rooms_number != None:
        validate(instance=rooms_number, schema={"type":"integer"})
      else:
          messages.append("In your json data, the label named 'rooms number' is 'None'! You need a value")
    except:
      messages.append("In your json data, the label named 'rooms number' is suppose to be an integer")
    try:
      if zip_code != None:
        validate(instance=zip_code, schema={"type":"integer"})
      else:
          messages.append("In your json data, the label named 'zip code' is 'None'! You need a value")
    except:
      messages.append("In your json data, the label named 'zip code' is suppose to be an integer")
    
    try:
      if land_area != None:
        validate(instance=land_area, schema={"type":"integer"},)
      else:
        mydata["data"]["land-area"] = 0
    except:
      messages.append("In your json data, the label named 'land area' is suppose to be an integer")
    
    try:
      if garden != None:
        validate(instance=garden, schema={"type":"boolean",})
      else:
        mydata["data"]["garden"] = False
    except:
      messages.append("In your json data, the label named 'garden' is suppose to be an boolean")
    try:
      if garden_area != None:
        validate(instance=garden_area, schema={"type":"integer"})
      else:
        mydata["data"]["garden-area"] = 0
    except:
      messages.append("In your json data, the label named 'garden area' is suppose to be an integer")
    try:
      if equipped_kitchen != None:
        validate(instance=equipped_kitchen, schema={"type":"boolean"})
      else:
        mydata["data"]["equipped-kitchen"] = False
    except:
      messages.append("In your json data, the label named 'equipped kitchen' is suppose to be an boolean")
    try:
      if full_address != None:
        validate(instance=full_address, schema={"type":"string"})
      else:
        mydata["data"]["full-address"] = 0
    except:
      messages.append("In your json data, the label '-full address' area is suppose to be an string")
    try:
      if swimming_pool != None:
        validate(instance=swimming_pool, schema={"type":"boolean"})
      else:
        mydata["data"]["swimming-pool"] = False
    except:
      messages.append("In your json data, the label 'swimming pool' area is suppose to be an boolean")
    try:
      if furnished != None:
        validate(instance=furnished, schema={"type":"boolean"})
      else:
        mydata["data"]["furnished"] = False
    except:
      messages.append("In your json data, the label named 'furnished' is suppose to be an boolean")
    try:
      if open_fire != None:
        validate(instance=open_fire, schema={"type":"boolean"})
      else:
        mydata["data"]["open-fire"] = False
    except:
      messages.append("In your json data, the label named 'open fire' is suppose to be an boolean")
    try:
      if terrace != None:
        validate(instance=terrace, schema={"type":"boolean"})
      else:
        mydata["data"]["terrace"] = False
    except:
      messages.append("In your json data, the label named 'terrace' is suppose to be an boolean")
    try:
      if terrace_area != None:
        validate(instance=terrace_area, schema={"type":"integer"})
      else:
        mydata["data"]["terrace-area"] = 0
    except:
      messages.append("In your json data, the label named 'terrace area' is suppose to be an integer")
    try:
      if facades_number != None:
        validate(instance=facades_number, schema={"type":"integer"})
      else:
        mydata["data"]["facades-number"] = 0
    except:
      messages.append("In your json data, the label named 'facades number' is suppose to be an integer")
    try:
      if building_state != None:
        validate(instance=building_state, schema={"type":"string"})
      else:
        mydata["data"]["building-state"] = "Unknown"
    except:
      messages.append("In your json data, the label named 'building state is suppose to be an string")

    return messages,mydata



