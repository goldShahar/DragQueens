from config import INSERT, DELETE, TYPE
from cud.cud import final_func

from fastapi import APIRouter

router = APIRouter(prefix="/type")


@router.get("/create")
def create_type(hazerd_type: str, importance: int, min_time: float, min_area: float):
    final_func(
        {
            "type": hazerd_type,
            "importance": importance,
            "min_time": min_time,
            "min_area": min_area,
        },
        INSERT,
        TYPE,
    )


@router.get("/delete")
def delete_type(hazerd_type: str):
    final_func(
        {"type": hazerd_type},
        DELETE,
        TYPE,
    )
