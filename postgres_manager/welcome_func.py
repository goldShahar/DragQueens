from typing import Any


def welcome_func(action: str, table: str, valuses: dict[str, Any]):
    if action == "READ":
        return ""
    if action == "WRITE":
        return ""
    if action == "DELETE":
        return ""

    else:
        return f"Action {action} is invalide"
