from typing import Any


def welcome_func(reqest: dict[str, Any]):
    if reqest["action"] == "read":
        result = ""
        back_to_reading_funcs(result)
    if reqest["action"] == "write":
        result = ""
        back_to_kafka(reqest["message_id"], result)
    if reqest["action"] == "delete":
        result = ""
        back_to_kafka(reqest["message_id"], result)

    else:
        if "message_id" in reqest.keys:
            back_to_kafka(
                reqest["message_id"], f"Action {reqest["action"]} is invalide"
            )
        else:
            back_to_reading_funcs(f"Action {reqest["action"]} is invalide")


def back_to_kafka(message_id: str, result: str):
    pass


def back_to_reading_funcs(result: str):
    pass
