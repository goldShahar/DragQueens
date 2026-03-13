from datetime import datetime
from typing import Any

import pymongo

from read_config_file import mongo_config

mongo_client = pymongo.MongoClient(mongo_config["mongo_connection_string"])
mongo_db = mongo_client[mongo_config["mongo_db_name"]]

mongo_building_collection = mongo_db[mongo_config["mongo_building_collection"]]
mongo_people_collection = mongo_db[mongo_config["mongo_people_collection"]]


def find_buildings_in_polygon_area(geo_polygon):
    return mongo_building_collection.find(
        {
            "geometry": {
                "$geoIntersects": {
                    "$geometry": {"type": "Polygon", "coordinates": geo_polygon}
                }
            }
        },
        {"_id": 1},
    )


def find_people_in_polygon_at_time(geo_polygon: list, start_time: datetime, end_time: datetime):
    building_in_area = find_buildings_in_polygon_area(geo_polygon)
    people_in_area = []

    for person in mongo_people_collection.find():
        print(person)
        for residence in person["residences"]:
            if (residence["building_id"] in building_in_area
                and residence["start_date"] >= start_time
                and (residence["end_date"] <= end_time or residence["end_date"] is None)
            ):
                people_in_area.append(person)

    return people_in_area


def switch_building_id_to_polygon(person: dict[str, Any]):
    person["polygon_residences"] = []
    for residence in person["residences"]:
        building_info = mongo_building_collection.find_one(residence["building_id"])
        person["polygon_residences"].append({
            "geometry": building_info["geometry"],
            "latitude": building_info["latitude"],
            "longitude": building_info["longitude"],
            "start_date": residence["start_date"],
            "end_date": residence["end_date"]})
    person.pop("residences")
    return person

def find_updated_people_after_time(time: datetime):
    updated_people = []
    for person in mongo_people_collection.find():
        if person["last_update_time"] >= time:
            updated_people.append(switch_building_id_to_polygon(person))
    return updated_people


