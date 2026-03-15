from typing import Any


def welcome_func(action: str, table: str, valuses: dict[str, Any]):
    if action == "read":
        return ""
    if action == "write":
        return ""
    if action == "delete":
        return ""

    else:
        return f"Action {action} is invalide"
