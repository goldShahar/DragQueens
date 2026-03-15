from postgres_manager.sql_models.columns.table_column import TableColumn
from postgres_manager.sql_models import Hazard
from postgres_manager.models.funcs import read_type
from sqlalchemy import Sequence, func

from postgres_manager.sql_models.cud_models import get_correct_cond

class HazardTypeNameColumn(TableColumn):
    field_in_table = Hazard.type_name

    def read_value(cls, value_to_filter: list[str]):
        return cls.field_in_table in value_to_filter
    

class IdColumn(TableColumn):
    field_in_table = Hazard.id

    def read_value(cls, value_to_filter: list[str]):
        return "-".join(cls.field_in_table.split("-")[1:]) in value_to_filter
        

class GeoPolygonColumn(TableColumn):
    field_in_table = Hazard.geo_polygon

    def read_value(cls, value_to_filter):
        return func.ST_Intersects(cls.field_in_table, func.ST_GeomFromText(value_to_filter, 4326))


class StartTimeColumn(TableColumn):
    field_in_table = Hazard.start_time

    def read_value(cls, value_to_filter):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)
    

class EndTimeColumn(TableColumn):
    field_in_table = Hazard.end_time

    def read_value(cls, value_to_filter):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)


class PeopleIdsColumn(TableColumn):
    field_in_table = Hazard.people_ids

    def read_value(cls, value_to_filter):
        if isinstance(value_to_filter, list):
            return any(cls.field_in_table.contains(value) for value in value_to_filter)
        elif isinstance(value_to_filter, str):
            return get_correct_cond(type(cls.field_in_table), len(cls.field_in_table), value_to_filter)


class BuildingsIdsColumn(TableColumn):
    field_in_table = Hazard.buildings_ids

    def read_value(cls, value_to_filter):
        if isinstance(value_to_filter, list):
            return any(cls.field_in_table.contains(value) for value in value_to_filter)
        elif isinstance(value_to_filter, str):
            return get_correct_cond(type(cls.field_in_table), len(cls.field_in_table), value_to_filter)
        

class Duration(TableColumn):
    field_in_table = func.extract('epoch', Hazard.end_time - Hazard.start_time)

    def read_value(cls, value_to_filter):
        return get_correct_cond(type(cls.field_in_table), cls.field_in_table, value_to_filter)
    

class Importance(TableColumn):
    field_in_table = Hazard.type_name

    def read_value(cls, value_to_filter):
        seq: Sequence = HazardTypeNameColumn.read_value(read_type(Importance=value_to_filter, selected_columns=[True, False, False, False]))
        return HazardTypeNameColumn.read_value(seq)




