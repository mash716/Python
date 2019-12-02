import json

f = open('json01.json','r')
json_dict = json.load(f)
print(format(json_dict['yamada']))