from pymongo import MongoClient
import openlay

client = MongoClient('localhost',27017)

db = client['nested']

col = db.road

coord = openlay.coordinates('overlay.json')
for latlon in coord:

    record= {
        "geometry" : {
        "coordinates" : [[latlon]]
        }
        }

    col.insert_many([record])
