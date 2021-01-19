import os
import urllib.request
import json


while True:
    ip = input("What is your target ip : ")
    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print("IP:" + values['query'])
    print("City:" + values["city"])
    print("Country:" + values['country'])
    print("Region:" + values['region'])
    print("Time zone:" + values['timezone'])
    print("Latitude:" + str(values["lat"]))
    print("Longitude:" + str(values["lon"]))
    print("Isp:" + values['isp'])
    print("RegionName:" + values['regionName'])

    break
