from config import INSERT, DELETE, TYPE
from cud.cud import final_func

from fastapi import APIRouter

router = APIRouter(prefix="/type")


@router.get("/create")
def create_type(type_name: str, importance: int, min_time: float, min_area: float):
    return final_func(
        {
            "type_name": type_name,
            "Importance": importance,
            "Min_time": min_time,
            "Min_area": min_area,
        },
        INSERT,
        TYPE,
    )


@router.get("/delete")
def delete_type(type_name: str):
    return final_func(
        {"type_name": type_name},
        DELETE,
        TYPE,
    )
