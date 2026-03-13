from pydantic import BaseModel


class Hazard(BaseModel):
    type_name: str
    id: str
    geo_polygon: WKBElement
    start_time: datetime.datetime
    end_time: datetime.datetime
    people_ids: list[str]
    buildings_ids: list[str]
    
