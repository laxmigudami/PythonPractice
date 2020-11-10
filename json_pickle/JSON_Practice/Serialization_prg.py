import json
data = {
    "details" : { "name" : "lakshmi", "place" : "Belgaum"}
    }
with open("data.json", 'w') as f:
    json.dump(data, f, indent=4) #Running above code creates a file named data.json, with python Dictionary converted into JSON format.

#
# # dumps
# json_data = json.dumps(data) # to serialize the data in the above format into string
# print(json_data)