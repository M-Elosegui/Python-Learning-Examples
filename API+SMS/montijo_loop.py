
import requests
import json
from datetime import datetime
import time
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

############################# WEATHER ON LOCATION ###########################

while True:

    #Montijo Village location
    lat = 38.707415492857805
    lon = -8.96721556203164

    #api key from openwether.org
    api_key = "a371533a46d01d6ccbe7a94d5e1e76a2"

    #currenttime
    current_time = str(datetime.now()).split()[1].split(":")
    current_hour = current_time[0]
    current_minute = current_time[1]

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

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "AC409e4e87e107901e56fda3b50345a385"
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "1122155ae8f33573bde16231762a8de8"

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
                    .create(
                         body=f"Ora boas. Hoje no Montijo são {current_hour}:{current_minute}, estão {current_temp}º, e sente-se como {temp_feel}º. \n A humidade é {humidity}% e no geral, segundo os especialistas, será: <{description}> ",
                         from_='+18576753706',
                         to='+351917146504'
                     )

    print(message.sid)
    time.sleep(21500)

