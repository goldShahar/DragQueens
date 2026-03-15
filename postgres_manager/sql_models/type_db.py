from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from postgres_manager.sql_models.cud_models import delete_record, get_correct_cond, get_selected_columns
from . import Type, engine



def create_type_in_pg(type_name: str, Importance: int, Min_time: int, Min_area: float):
    try:
        with Session(engine) as session:
            inserted_type = Type(type_name=type_name, importance=Importance, Min_time=Min_time, Min_area=Min_area)
            session.add(inserted_type)
            session.commit()
            return "Type created successfully"
    except Exception as e:
        return f"Error creating type: {str(e)}"
    

def delete_type_in_pg(type_name1: str):
    delete_record(type_name1, Type, Type.type_name)



def read_type_from_pg(filter_values: dict[str, str], selected_columns: list[bool]):
    try:
        with Session(engine) as session:
            stmt = select(*get_selected_columns(selected_columns, Type)).where(*get_where_conditions(filter_values))
            return session.execute(stmt).fetchall()
            
    except Exception as e:
        return f"Error reading type: {str(e)}"


def get_where_conditions(filter_values: dict[str, str]) -> list:
    conditions = []
    if filter_values.get("type_name"):
        conditions.append(Type.type_name == filter_values["type_name"])
    if filter_values.get("importance"):
        conditions.append(get_correct_cond(int, Type.importance, filter_values["importance"]))
    if filter_values.get("Min_time"):
        conditions.append(get_correct_cond(int, Type.Min_time, filter_values["Min_time"]))
    if filter_values.get("Min_area"):
        conditions.append(get_correct_cond(int, Type.Min_area, filter_values["Min_area"]))   
    return conditions 




    


print(create_type_in_pg("fire", "8", "2025-09-20T02:33:12", 12.5))
    