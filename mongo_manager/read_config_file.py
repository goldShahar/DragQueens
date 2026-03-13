import json


def read_config_file(path: str) -> dict:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except Exception as e:
        raise e


mongo_config = read_config_file("mongo_manager/config.json")
