#  + lecture 35 api & sms

# pull from API: coinbase, weather, iss, sporting/ligapt, own position
# http://jsonviewer.stack.hu/#http:// - visualize json

import requests
import json
from datetime import datetime

def print_test(*args):
    for n in args:
        print(n)


######################   ISS LOCATION    ######################

# def iss_location():
#
#     response = requests.get(url="http://api.open-notify.org/iss-now.json")
#     response.raise_for_status()    #this function raises an execpcion to know which error
#     #print(response)
#
#     data1 = response.json()
#     lon = response.json()["iss_position"]["longitude"]
#     lat = response.json()["iss_position"]["latitude"]
#     data = (lat, lon)
#
#     #this is the actual value we needed
#     # print(f"Original json file data: \n {data1} \n\n")
#     # print(data)
#     return data
#
# print(iss_location())

##################   OWN POSITION & WEATHER    ######################


# own_position=[38.77663006326763, -9.10232654925077]
#
# def sunrise_on_input(a, b):
# # sunrise/sunset on own position. this api requires parameters
#
#     parameters={
#         "lat": f"{a}",
#         "lon": f"{b}"
#     }
#
#     response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     sunrisesunset_info = response.json()
#     # print(parameters)
#     print(f"\n\nYour sunrise time is: " + sunrisesunset_info["results"]["sunrise"])
#
#     return sunrisesunset_info
#
#
# lat = own_position[0]
# lon = own_position[1]
# sunrise_on_input(lat, lon)



############################# WEATHER ON LOCATION ###########################
# weather on location:


#Montijo Village location
lat = 38.707415492857805
lon = -8.96721556203164
#api key from openwether.org
api_key = "a371533a46d01d6ccbe7a94d5e1e76a2"
#currenttime
current_time = str(datetime.now()).split()[1].split(":")
current_hour = current_time[0]
current_minute = [1]

#API request
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
response.raise_for_status()
data = response.json()

#json file creating
json_object = json.dumps(data)
# Writing to json file
with open("current_montijo.json", "w") as weather_data:
    weather_data.write(json_object)

current_temp = data["main"]["temp"]
temp_feel = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]


###############################    SMS   ( with twilio )   ###############################

import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "AC409e4e87e107901e56fda3b50345a385"
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "1122155ae8f33573bde16231762a8de8"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"Ora boas. Hoje no Montijo são {current_hour}:{current_minute}, estão {current_temp}º, e sente-se como {temp_feel}º. \n A humidade é {humidity}% e no geral, segundo os especialistas, será: <{description}> ",
                     from_='+18576753706',
                     to='+351917146504'
                 )

print(message.sid)


