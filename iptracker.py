import os
import urllib.request
import json
import time
import schedule

def executeSomething():

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


schedule.every(1).seconds.do(executeSomething)#This code run every 10 seconds
#schedule.every().hour.do(executeSomething())


while 1:
    schedule.run_pending()
    time.sleep(1)
