from postgres_manager.sql_models.columns.table_column import TableColumn
from postgres_manager.sql_models import Type
from postgres_manager.sql_models.cud_models import get_correct_cond

class TypeNameColumn(TableColumn):
    field_in_table = Type.type_name

    def read_value(cls, value_to_filter: list[str]):
        return cls.field_in_table in value_to_filter
    

class ImportanceColumn(TableColumn):
    field_in_table = Type.importance

    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)
    

class MinTimeColumn(TableColumn):
    field_in_table = Type.Min_time

    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)
    

class MinAreaColumn(TableColumn):
    field_in_table = Type.Min_area

    def read_value(cls, value_to_filter: list[str]):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)
    


        