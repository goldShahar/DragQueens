from sqlalchemy.orm import Session
from .__init__ import engine



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