from datetime import datetime
from shapely import Polygon
from shapely.wkt import loads
from pydantic import BaseModel, field_validator


class Hazard_Model(BaseModel):
    type_name: str
    id: str
    geo_polygon: str
    start_time: datetime
    end_time: datetime
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

class Type_Model(BaseModel):
    type_name: str
    Importance: int 
    Min_time: datetime 
    Min_area: float