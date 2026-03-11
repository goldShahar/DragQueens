from datetime import datetime
import polygon
import pymongo

from config import mongo_config

mongo_client = pymongo.MongoClient(mongo_config["mongo_connection_string"])
mongo_db = mongo_client[mongo_config["mongo_db_name"]]

mongo_building_collection = mongo_db[mongo_config["mongo_building_collection"]]
mongo_people_collection = mongo_db[mongo_config["mongo_people_collection"]]


def find_buildings_in_polygon_erea(geo_polygon: polygon):
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


def find_people_in_polygon_at_time(
    geo_polygon: polygon, start_time: datetime, end_time: datetime
):
    building_in_erea = find_buildings_in_polygon_erea(geo_polygon)
    people_in_erae = []
    for person in mongo_people_collection:
        for residence in person["residences"]:
            if (
                residence["building_id"] in building_in_erea
                and residence["start_date"] >= start_time
                and residence["end_date"] <= end_time
            ):
                people_in_erae.append(person)

    return people_in_erae
