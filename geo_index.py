import openlay
'''
overlay.json includes points that person destination.
'''

db = MongoClient('localhost',27017).geo_example

db.places.create_index([("loc", GEO2D)])

coord = openlay.coordinates('overlay.json')
for latlon in coord:

    result = db.places.insert_many([{"loc": [latlon]}])


print(result.inserted_ids)