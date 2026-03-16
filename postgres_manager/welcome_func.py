from typing import Any

from postgres_manager.models.crud import *


class ActionToTableSingleton:
    instance = None
    actions_dict: dict[str, callable] = {"read + type": read_type, "insert + type": create_type, "delete + type": delete_type,
                                        "read + hazard": read_hazard, "insert + hazard": create_hazard, "delete + hazard": delete_hazard}

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    

def welcome_func(action: str, table: str, values: dict[str, Any]):
    try:
        return ActionToTableSingleton().actions_dict.get(f"{action.lower()} + {table.lower()}")(values)
    except Exception as e:
        return f"Action {action} is invalide: {str(e)}" 



