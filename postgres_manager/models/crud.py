from datetime import datetime

from postgres_manager.models.basemodels import Hazard_Model
from postgres_manager.models.basemodels import Type_Model
from postgres_manager.sql_models.hazard_db import create_hazard_in_pg, delete_hazard_in_pg_by_type_name
from postgres_manager.sql_models.type_db import create_type_in_pg, delete_type_in_pg, read_type_from_pg


def create_hazard(hazard_dict: dict):
    hazard = Hazard_Model(**hazard_dict)
    return create_hazard_in_pg(hazard)

def delete_hazard(id: str, type_name: str):
    return delete_hazard_in_pg_by_type_name(id, type_name)

def read_hazard(): # TODO match it with type.py read
    pass
    
def create_type(type_dict: dict): 
    type = Type_Model(**type_dict)
    if read_type(type_name=type.type_name, selected_columns=[True, False, False, False]):
        return "Type already exists"
    return create_type_in_pg(type.type_name, type.Importance, type.Min_time, type.Min_area)


def delete_type(type_name: str):
    return delete_type_in_pg(type_name)


def read_type(type_name: str | None, Importance: int | None, Min_time: datetime | None, Min_area: float | None, selected_columns: list[bool]):
    return read_type_from_pg({"type_name": type_name, "Importance": Importance, "Min_time": Min_time, "Min_area": Min_area}, selected_columns)