from postgres_manager.sql_models.columns.table_column import TableColumn
from postgres_manager.sql_models import Type
from postgres_manager.sql_models.cud_models import get_correct_cond

class TypeNameColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return Type.type_name.in_(value_to_filter)
    

class ImportanceColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(int, Type.importance, value_to_filter)
    

class MinTimeColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(int, Type.Min_time, value_to_filter)
    

class MinAreaColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(float, Type.Min_area, value_to_filter)
    


        