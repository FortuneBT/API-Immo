from jsonschema import validate
from typing import List, Dict, Optional


def validate_json(mydata: Dict) -> List[list, dict]:
    """
    This function validate the json format that is send by the user

    """
    area = mydata["0"]["area"]
    property_type = mydata["0"]["property-type"]
    rooms_number = mydata["0"]["rooms-number"]
    zip_code = mydata["0"]["zip-code"]
    land_area = mydata["0"]["land-area"]
    garden = mydata["0"]["garden"]
    garden_area = mydata["0"]["garden-area"]
    equipped_kitchen = mydata["0"]["equipped-kitchen"]
    full_address = mydata["0"]["full-address"]
    swimming_pool = mydata["0"]["swimming-pool"]
    furnished = mydata["0"]["furnished"]
    open_fire = mydata["0"]["open-fire"]
    terrace = mydata["0"]["terrace"]
    terrace_area = mydata["0"]["terrace-area"]
    facades_number = mydata["0"]["facades-number"]
    building_state = mydata["0"]["building-state"]

    messages: List = []

    try:
        if area != None:
            validate(instance=area, schema={"type": "integer"})
        else:
            messages.append(
                "In your json data, the label named 'area' is 'None'! You need a value"
            )
    except:
        messages.append(
            "In your json data, the label named area is suppose to be an integer"
        )
    try:
        if property_type != None:
            validate(instance=property_type, schema={"type": "string"})
        else:
            messages.append(
                "In your json data, the label named 'property typed' is 'None'! You need a value"
            )
    except:
        messages.append(
            "In your json data, the label named 'property typed' is suppose to be an string"
        )
    try:
        if rooms_number != None:
            validate(instance=rooms_number, schema={"type": "integer"})
        else:
            messages.append(
                "In your json data, the label named 'rooms number' is 'None'! You need a value"
            )
    except:
        messages.append(
            "In your json data, the label named 'rooms number' is suppose to be an integer"
        )
    try:
        if zip_code != None:
            validate(instance=zip_code, schema={"type": "integer"})
        else:
            messages.append(
                "In your json data, the label named 'zip code' is 'None'! You need a value"
            )
    except:
        messages.append(
            "In your json data, the label named 'zip code' is suppose to be an integer"
        )

    try:
        if land_area != None:
            validate(
                instance=land_area,
                schema={"type": "integer"},
            )
        else:
            mydata["0"]["land-area"] = 0
    except:
        messages.append(
            "In your json data, the label named 'land area' is suppose to be an integer"
        )

    try:
        if garden != None:
            validate(
                instance=garden,
                schema={
                    "type": "boolean",
                },
            )
        else:
            mydata["0"]["garden"] = False
    except:
        messages.append(
            "In your json data, the label named 'garden' is suppose to be an boolean"
        )
    try:
        if garden_area != None:
            validate(instance=garden_area, schema={"type": "integer"})
        else:
            mydata["0"]["garden-area"] = 0
    except:
        messages.append(
            "In your json data, the label named 'garden area' is suppose to be an integer"
        )
    try:
        if equipped_kitchen != None:
            validate(instance=equipped_kitchen, schema={"type": "boolean"})
        else:
            mydata["0"]["equipped-kitchen"] = False
    except:
        messages.append(
            "In your json data, the label named 'equipped kitchen' is suppose to be an boolean"
        )
    try:
        if full_address != None:
            validate(instance=full_address, schema={"type": "string"})
        else:
            mydata["0"]["full-address"] = 0
    except:
        messages.append(
            "In your json data, the label '-full address' area is suppose to be an string"
        )
    try:
        if swimming_pool != None:
            validate(instance=swimming_pool, schema={"type": "boolean"})
        else:
            mydata["0"]["swimming-pool"] = False
    except:
        messages.append(
            "In your json data, the label 'swimming pool' area is suppose to be an boolean"
        )
    try:
        if furnished != None:
            validate(instance=furnished, schema={"type": "boolean"})
        else:
            mydata["0"]["furnished"] = False
    except:
        messages.append(
            "In your json data, the label named 'furnished' is suppose to be an boolean"
        )
    try:
        if open_fire != None:
            validate(instance=open_fire, schema={"type": "boolean"})
        else:
            mydata["0"]["open-fire"] = False
    except:
        messages.append(
            "In your json data, the label named 'open fire' is suppose to be an boolean"
        )
    try:
        if terrace != None:
            validate(instance=terrace, schema={"type": "boolean"})
        else:
            mydata["0"]["terrace"] = False
    except:
        messages.append(
            "In your json data, the label named 'terrace' is suppose to be an boolean"
        )
    try:
        if terrace_area != None:
            validate(instance=terrace_area, schema={"type": "integer"})
        else:
            mydata["0"]["terrace-area"] = 0
    except:
        messages.append(
            "In your json data, the label named 'terrace area' is suppose to be an integer"
        )
    try:
        if facades_number != None:
            validate(instance=facades_number, schema={"type": "integer"})
        else:
            mydata["0"]["facades-number"] = 0
    except:
        messages.append(
            "In your json data, the label named 'facades number' is suppose to be an integer"
        )
    try:
        if building_state != None:
            validate(instance=building_state, schema={"type": "string"})
        else:
            mydata["0"]["building-state"] = "Unknown"
    except:
        messages.append(
            "In your json data, the label named 'building state is suppose to be an string"
        )

    return messages, mydata
