from fastapi import APIRouter
from postgres_manager.welcome_func import welcome_func

router = APIRouter(prefix="/read_postgres")


@router.get("/query_hazards_table")
def get_query_in_hazards_table(filter_tables_fields: list[bool]):
    welcome_func("READ", "hazard", filter_tables_fields)


@router.get("/query_types_table")
def get_query_in_types_table(filter_tables_fields: list[bool]):
    welcome_func("READ", "type", filter_tables_fields)
