import pymongo
import config, read

mongo_client = pymongo.MongoClient(config.mongo_connection_string)
mongo_db = mongo_client[config.mongo_db_name]


poly = mongo_db[config.mongo_buildings_collection].find_one(
    {"_id": "6MR368G6+J545"}, {"geometry": {"coordinates": 1}}
)["geometry"]["coordinates"]

man = mongo_db[config.mongo_people_collection].find_one(
    {"_id": "7300000001", "building_id": "6MR368G6+J545"},
    {"start_date": 1, "end_date": 1, "_id": 0},
)
print("------------------------------------start------------------------------------")

for polygon in read.find_buildings_in_polygon_erea(poly):
    print(polygon)


for person in read.find_people_in_polygon_at_time(
    poly, man["start_date"], man["end_date"]
):
    print(person)
