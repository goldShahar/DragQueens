from sqlalchemy import select
from sqlalchemy.orm import Session
from postgres_manager.sql_models.columns.table_column import TableColumn
from postgres_manager.sql_models.columns.type_columns import *
from postgres_manager.sql_models.cud_models import delete_record, get_correct_cond, get_selected_columns
from . import Type, engine


class type_table_singleton:
    instance = None
    columns_dict: dict[str, TableColumn] = {"type_name": TypeNameColumn, "importance": ImportanceColumn, "Min_time": MinTimeColumn, "Min_area": MinAreaColumn}

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

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
    # try:
        # with Session(engine) as session:
        #     stmt = select(*get_selected_columns(selected_columns, Type)).where(*get_where_conditions(filter_values))
        #     return session.execute(stmt).fetchall()
            
    # except Exception as e:
    #     return f"Error reading type: {str(e)}"
        with Session(engine) as session:    
            
            stmt = select(*get_selected_columns(selected_columns, Type)).where(*get_where_conditions(filter_values))
            
            return session.execute(stmt).fetchall()


def get_where_conditions(filter_values: dict[str, str]) -> list:
    conditions = []
    for field_name in filter_values:
        if filter_values[field_name] is not None:
            column_class = type_table_singleton().columns_dict.get(field_name).read_value(cls=type_table_singleton()
                                                                                            .columns_dict.get(field_name), value_to_filter=filter_values[field_name])
            conditions.append(column_class)
    return conditions



    

# print(create_type_in_pg("fire2", 3, 10, 100.0))
# print(read_type_from_pg({"type_name": "fire2"}, [True, True, False, False]))
    