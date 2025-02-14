import json


def get_test_data():
    with open('data/test_data.json', 'r') as test_data:
        data = json.load(test_data)
        return data
