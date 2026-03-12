def read_config_file(path: str) -> dict:
    try:
        with open(path, "r", "utf-8") as file:
            return file.read()
    except Exception as e:
        raise e


mongo_config = read_config_file("conig.txt")
