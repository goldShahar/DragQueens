from pydantic import BaseModel

class Type(BaseModel):
    type_name: str
    importance: str
    Min_time: datetime.datetime
    Min_area: float