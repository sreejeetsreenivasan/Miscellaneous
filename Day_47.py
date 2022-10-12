# From 50 days of Python Challenge book
import json


def save_json(input_dict):
    json_object = json.dumps(input_dict, indent=4)
    file = open("json.file", "w")
    file.write(json_object)
    file.close()


def read_json():
    file = open("json.file", "r")
    json_object = json.load(file)
    print(json_object)


# save_json({'name': 'Carol','sex': 'female','age': 55})
# read_json()
