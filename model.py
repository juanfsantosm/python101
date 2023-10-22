import json

def load_db():
    with open("employees.json") as e:
        return json.load(e)

db = load_db()