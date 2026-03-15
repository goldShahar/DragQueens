from config import  SUCCESS, FAILURE
from redili_manager.my_redis import delete_key, read

def insert_type_validation(hazard_type: dict):
    if 1 < hazard_type["importance"] < 100 and hazard_type['min_area'] > 0 and hazard_type['min_time'] > 0:
        return SUCCESS
    return FAILURE

def delete_type_validation(type_name: str):
    if delete_key(type_name):
        return SUCCESS
    return FAILURE

def existing_type_validator(hazard: dict):
    hazard_type = read(hazard['type_name'])
    if hazard_type:
        return check_valid_hazrad(hazard_type[1], hazard)
    
    # check if the type exists in postgres
    return FAILURE

def check_valid_hazrad(conditions: dict, hazard: dict):
    if conditions['min_time'] <= hazard['min_time']:
        return FAILURE
    if conditions['min_area'] <= hazard['min_area']:
        return FAILURE
    return SUCCESS
