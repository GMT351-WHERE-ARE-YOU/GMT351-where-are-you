from pymongo import MongoClient

"""
This script create a person database.
The format of json file includes GSM Tower coordinates.
Every successive coordinate represent one point.
For example, if there are 12 points lat-lon in the json file, person rotation created with 4 points.
Also json file includes range list. This is used for trilateration calculation.
"""

def add_db(person,phone,coord_list):

    client = MongoClient('localhost',27017)

    db = client['position_latlon']

    col = db.positions


    record= {
                "person" : person,
                "phone number" : phone,
                "geometry" : {
                                "type": "Point",
                                "coordinates" : [coord_list]
                            }
                }

    col.insert_many([record])


def db_dynamic(person,phone,Ip,coord_list):

    client = MongoClient('localhost',27017)

    db = client['points_latlon']

    col = db.dynamic_position


    record= {
                "person" : person,
                "ıp": Ip,
                "phone number" : phone,
                "geometry" : {
                                "type": "Line-String",
                                "coordinates" : [coord_list]
                            }
                }

    col.insert_many([record])