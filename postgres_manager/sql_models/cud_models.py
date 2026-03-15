from datetime import datetime

from sqlalchemy.orm import Session
from .__init__ import engine

def delete_record(pk, table, pk_column):
    try:
        with Session(engine) as session:
            records_to_delete = session.query(table).filter(pk_column == pk).all()
            if records_to_delete:
                for record in records_to_delete:
                    session.delete(record)
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
        return field >= convert_to_correct_type(cond[2:], obj_type)
    if cond.startswith("<="):
        return field <= convert_to_correct_type(cond[2:], obj_type)
    if cond.startswith(">"):
        return field > convert_to_correct_type(cond[1:], obj_type)
    if cond.startswith("<"):
        return field < convert_to_correct_type(cond[1:], obj_type)
    return field == convert_to_correct_type(cond, obj_type)

def convert_to_correct_type(value: str, obj_Type):
    if obj_Type == datetime:
        return datetime.strptime(value, f"%Y-%m-%dT%H:%M:%S")
    else:
        return obj_Type(value)