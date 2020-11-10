import json
odics = '{"K1": "VAL1", "K2": "VAL2"}'
json_result = json.loads(odics)
print(json_result)

dict_format = json.dumps(json_result)
print(dict_format)


