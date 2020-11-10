import json
def writeFunc():
    fileObj = open("pythonJsonData.json", 'w')
    data = { "name": "laxmi", "address": "belgaum", "phone": None, "mock": True}
    print(type(data))
    # dump and dumps
    c_data = json.dumps(data)
    fileObj.write(c_data)
    # json.dump(data, fileObj)
    print(type(c_data))
writeFunc()