from config import INSERT, DELETE, HAZARD
from cud.cud import final_func

from datetime import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/hazard")


@router.get("/create")
def create_hazard(
    hazerd_type: str,
    hazerd_id: str,
    goe_polygon,
    start_time: datetime,
    end_time: datetime,
):
    return final_func(
        {
            "type_name": hazerd_type,
            "id": hazerd_id,
            "goe_polygon": goe_polygon,
            "start_time": start_time,
            "end_time": end_time,
        },
        INSERT,
        HAZARD,
    )


@router.get("/delete")
def delete_hazard(hazerd_id: str, hazerd_type: str | None):
    return final_func(
        {"type": hazerd_type, "id": hazerd_id},
        DELETE,
        HAZARD,
    )
