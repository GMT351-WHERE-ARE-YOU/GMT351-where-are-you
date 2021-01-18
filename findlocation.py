#                          Get your current location with IP


#pip install requests


import time
import requests
import schedule

def executeSomething():


    r = requests.get('https://get.geojs.io/')

    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ippAdd = ip_request.json()["ip"]
    print(ippAdd)

    url = 'https://get.geojs.io/v1/ip/geo/' + ippAdd + '.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    # print(geo_data)

    print(geo_data['latitude'])
    print(geo_data['longitude'])

    print(geo_data['city'])
    print(geo_data['region'])
    print(geo_data['country'])
    print(geo_data['timezone'])


schedule.every(10).seconds.do(executeSomething)#This code run every 10 seconds
#schedule.every().hour.do(executeSomething())



while 1:
    schedule.run_pending()
    time.sleep(1)
