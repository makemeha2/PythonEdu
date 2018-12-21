import json
param = [1,2,3,{'4':5, '6':7}]
result = json.dumps(param, separators=(',', ':'))
print(result)

print("param's Type is ", type(param))
print("result's Type is ", type(result))
