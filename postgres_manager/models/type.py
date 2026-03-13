from datetime import datetime
from pydantic import BaseModel

class Type(BaseModel):
    type_name: str
    Importance: int 
    Min_time: datetime 
    Min_area: float

    def create_type(self): 
        if read_type(type_name=self.type_name, selected_columns=[True, False, False, False]):
            return "Type already exists"
        return create_type_in_pg(self.type_name, self.Importance, self.Min_time, self.Min_area)



def delete_type(type_name: str):
    return delete_type_in_pg(type_name)


def read_type(type_name: str | None, Importance: int | None, Min_time: datetime | None, Min_area: float | None, selected_columns: list[bool]):
    return read_type_from_pg({"type_name": type_name, "Importance": Importance, "Min_time": Min_time, "Min_area": Min_area}, selected_columns)