import json

FILE_NAME = "data/volunteers.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

def save_data(volunteers):
    with open(FILE_NAME, "w") as file:
        json.dump(volunteers, file, indent=4)