from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session
from .__init__ import Type, engine

def create_type_in_pg(type_name: str, Importance: int, Min_time: datetime, Min_area: float):
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
    if filter_values["type_name"]:
        conditions.append(Type.type_name == filter_values["type_name"])
    if filter_values["importance"]:
        conditions.append(get_correct_cond(int, Type.importance, filter_values["importance"]))
    if filter_values["Min_time"]:
        conditions.append(get_correct_cond(int, Type.Min_time, filter_values["Min_time"]))
    if filter_values["Min_area"]:
        conditions.append(get_correct_cond(int, Type.Min_area, filter_values["Min_area"]))   
    return conditions 




    
def delete_record(pk, table, pk_column):
    try:
        with Session(engine) as session:
            record_to_delete = session.query(table).filter(pk_column == pk).first()
            if record_to_delete:
                session.delete(record_to_delete)
                session.commit()
                return "Deleted successfully"
            else:
                return "Record not found"
    except Exception as e:
        return f"Error deleting record: {str(e)}"
    
    


def get_selected_columns(selected_columns: list[bool], table) -> list[str]:
    table_columns = table.__table__.columns.keys()
    return [getattr(table, table_columns[i]) for i in range(len(table_columns)) if selected_columns[i]]


def get_correct_cond(obj_type, field, cond: str):
    if cond.startswith(">="):
        return field >= obj_type(cond[2:])
    if cond.startswith("<="):
        return field <= obj_type(cond[2:])
    if cond.startswith(">"):
        return field > obj_type(cond[1:])
    if cond.startswith("<"):
        return field < obj_type(cond[1:])
    return field == obj_type(cond)

    


