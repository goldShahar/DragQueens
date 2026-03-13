import datetime
from shapely import Polygon
from shapely.wkt import loads
from pydantic import BaseModel, field_validator


class Hazard_Model(BaseModel):
    type_name: str
    id: str
    geo_polygon: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    people_ids: list[str]
    buildings_ids: list[str]

    @field_validator('geo_polygon')
    def validate_wkt(cls, polygon):
        try:
            value_as_geometry = loads(polygon)
            if not isinstance(value_as_geometry, Polygon):
                raise ValueError('Not a polygon')
            return polygon
        except Exception as e:
            raise ValueError(f'Invalid WKT: {e}')


def create_hazard(hazard: Hazard_Model):
    return create_hazard_in_pg(hazard)

def delete_hazard(id: str):
    return delete_hazard_in_pg(id: )
    
