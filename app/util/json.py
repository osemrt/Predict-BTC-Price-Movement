import json


def save(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data))


def load(filename):
    with open(filename) as f:
        data = json.loads(f.read())
    return data
