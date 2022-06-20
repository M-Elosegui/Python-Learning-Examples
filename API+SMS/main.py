#  + lecture 35 api & sms

# pull from API: coinbase, weather, iss, sporting/ligapt, own position
# http://jsonviewer.stack.hu/#http:// - visualize json

import requests


######################   ISS LOCATION
def iss_location():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()    #this function raises an execpcion to know which error
    #print(response)

    data1 = response.json()
    lon = response.json()["iss_position"]["longitude"]
    lat = response.json()["iss_position"]["latitude"]
    data = (lat, lon)

    #this is the actual value we needed
    # print(f"Original json file data: \n {data1} \n\n")
    # print(data)
    return data


print(iss_location())

##################   OWN POSITION

own_position=[38.77663006326763, -9.10232654925077]

print(own_position)


##################   WEATHER
# sunrise/sunset on own position. this api requires parameters
def sunrise_on_input(a,b):

    parameters={
        "lat":f"{a}",
        "lon":f"{b}"
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    sunrisesunset_info = response.json()
    # print(parameters)
    print(f"\n\nYour sunrise time is: " + sunrisesunset_info["results"]["sunrise"])

    return sunrisesunset_info


lat = own_position[0]
lon = own_position[1]
sunrise_on_input(lat,lon)

