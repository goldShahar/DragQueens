from datetime import datetime

from postgres_manager.sql_models.columns.table_column import TableColumn
from postgres_manager.sql_models import Hazard
import postgres_manager.models.crud as crud
from sqlalchemy import Row, Sequence, func
from geoalchemy2.shape import to_shape
from geoalchemy2.elements import WKTElement
from postgres_manager.sql_models.columns.type_columns import TypeNameColumn
from postgres_manager.sql_models.cud_models import get_correct_cond
from shapely import to_wkt
from geoalchemy2.functions import ST_AsText



class HazardTypeNameColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return lambda: Hazard.type_name.in_(value_to_filter)
    
    def read_by_schema(hazard: dict):
        return hazard.get("type_name")


class IdColumn(TableColumn):
    def read_value(cls, value_to_filter: list[str]):
        return lambda: "-".join(Hazard.id.split("-")[1:]).in_(value_to_filter)
    
    def read_by_schema(hazard: dict):
        return "-".join(hazard.get("id").split("-")[1:])
        

class GeoPolygonColumn(TableColumn):
    def read_value(cls, value_to_filter):
        wkt = WKTElement(value_to_filter, 4326)
        return lambda: func.ST_Intersects(Hazard.geo_polygon, wkt)
    
    def read_by_schema(hazard: dict):
        return to_wkt(hazard.get("geo_polygon"))


class StartTimeColumn(TableColumn):
    def read_value(cls, value_to_filter):
        return get_correct_cond(datetime, Hazard.start_time, value_to_filter)
    
    def read_by_schema(hazard: dict):
        return hazard.get("start_time")
    

class EndTimeColumn(TableColumn):
    def read_value(cls, value_to_filter):
        return get_correct_cond(datetime, Hazard.end_time, value_to_filter)
    
    def read_by_schema(hazard: dict):
        return hazard.get("end_time")


class PeopleIdsColumn(TableColumn):
    def read_value(cls, value_to_filter):
        if isinstance(value_to_filter, list):
            return any(Hazard.people_ids.contains(value) for value in value_to_filter)
        elif isinstance(value_to_filter, str):
            return get_correct_cond(list, len(Hazard.people_ids), value_to_filter)
    
    def read_by_schema(hazard: dict):
        return len(hazard.get("people_ids"))


class BuildingsIdsColumn(TableColumn):
    def read_value(cls, value_to_filter):
        if isinstance(value_to_filter, list):
            return any(Hazard.buildings_ids.contains(value) for value in value_to_filter)
        elif isinstance(value_to_filter, str):
            return get_correct_cond(list, len(Hazard.buildings_ids), value_to_filter)
    
    def read_by_schema(hazard: dict):
        return len(hazard.get("buildings_ids"))



class Duration(TableColumn):
    def read_value(cls, value_to_filter):
        return get_correct_cond(type(func.extract('epoch', Hazard.end_time - Hazard.start_time)), func.extract('epoch', Hazard.end_time - Hazard.start_time), value_to_filter)
    

class Importance(TableColumn):
    def read_value(cls, value_to_filter):
        seq: Sequence = TypeNameColumn.read_value(crud.read_type(Importance=value_to_filter, selected_columns=[True, False, False, False]))
        return HazardTypeNameColumn.read_value(seq)