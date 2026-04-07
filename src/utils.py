import json


def load_json(path: str) -> dict:
    """
    Load JSON file and return its contents as a dictionary.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
