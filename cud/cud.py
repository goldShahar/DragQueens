import uuid
from kafkush.producers.producer import send_to_kafka
from redili_manager.my_redis import write, delete_key
from config import TOPIC1, INSERT, FAILURE, TYPE, DELETE
from cud.validator import (
    insert_type_validation,
    delete_type_validation,
    existing_type_validator,
)


def insert_type(hazard_type: dict):
    if insert_type_validation(hazard_type):
        write(
            hazard_type["type_name"],
            {"id_msg": hazard_type["id_msg"], "conditions": hazard_type["conditions"]},
        )
        send_to_kafka(hazard_type, TOPIC1)
        return hazard_type["id_msg"]
    return FAILURE


def delete_type(hazard_type: dict):
    if delete_type_validation(hazard_type["type_name"]):
        delete_key(hazard_type["type_name"])
        send_to_kafka(hazard_type, TOPIC1)
        return hazard_type["id_msg"]
    return FAILURE


def insert_hazard(hazard: dict):
    if existing_type_validator(hazard["type_name"]):
        send_to_kafka(hazard, TOPIC1)
        return hazard["id_msg"]
    return FAILURE


def delete_hazard(hazard: dict):
    send_to_kafka(hazard, TOPIC1)
    return hazard["id_msg"]


def final_func(values: dict, action: str, class_type: str):
    values["id_msg"] = str(uuid.uuid4())
    values["TABLE"] = class_type
    if class_type == TYPE:
        if action == INSERT:
            values["ACTION"] = INSERT
            return insert_type(values)
        else:
            values["ACTION"] = DELETE
            return delete_type(values)
    else:
        if action == INSERT:
            values["ACTION"] = INSERT
            return insert_hazard(values)
        else:
            values["ACTION"] = DELETE
            return delete_hazard(values)
