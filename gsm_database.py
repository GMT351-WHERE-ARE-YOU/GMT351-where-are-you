from pymongo import MongoClient
import openlay

"""
This script create a person database.
The format of json file includes GSM Tower coordinates.
Every successive coordinate represent one point.
For example, if there are 12 points lat-lon in the json file, person rotation created with 4 points.
Also json file includes range list. This is used for trilateration calculation.
"""

client = MongoClient('localhost',27017)

db = client['gsm_towers']

col = db.towers

coord  = openlay.coordinates('1.json')
coord2 = openlay.coordinates('2.json')
coord3 = openlay.coordinates('3.json')
coord4 = openlay.coordinates('4.json')
coord5 = openlay.coordinates('5.json')
coord6 = openlay.coordinates('6.json')
coord7 = openlay.coordinates('7.json')
coord8 = openlay.coordinates('8.json')
coord9 = openlay.coordinates('9.json')
coord10 = openlay.coordinates('10.json')
coord11 = openlay.coordinates('11.json')


range1 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range2 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range3 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range4 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range5 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range6 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range7 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range8 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range9 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range10 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
range11 = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

coordin = [coord, coord2, coord3, coord4, coord5, coord6, coord7, coord8, coord9, coord10, coord11]
person = ["Pınar Hazan", "Aytaç Eskici", "Melih Altay", "Berk Anbaroğlu", "Ali Özgün Ok", "Sultan Kocaman", "Mustafa Türker", "Metin Nohutcu", "Ali Osman Demirer", "Murat Durmaz", "Kamil Teke"]
phone = [1111111, 222222, 333333, 1234567890, 234567810, 3456789120, 4567891230, 567891234, 7891234560, 1478523690, 3214569870 ]
ranges = [range1, range2, range3, range4, range5, range6, range7, range8, range9, range10, range11]

for rota in range(len(coordin)):

    record= {
            "person" : person[rota],
            "phone number" : phone[rota],
            "geometry" : {
                            "type": "Polygon",
                            "coordinates" : [coordin[rota]]
                        },

                            "range": [ranges[rota]]
            }

    col.insert_many([record])
