# This is a sample Python script.

# Datetime Strftime()
# ver isto para alterar automaticamente a formatacao do tempo



## NUTRITIONIX NATURAL LANGUAGE TO EXERCISE OUTPUT

#  https://developer.nutritionix.com/admin/access_details
# Application ID
# This is the application ID, you should send with each API request.
# 2845263c
#
# Application Keys
# These are application keys used to authenticate requests.
# b3c5e6bed6887eee7c9c29537b091bb3

# criar env var para estas duas ID

# solucao desta API:
# https://gist.github.com/angelabauer/dd71d7072626afd728e1730584c6e4b8




## SHEETY EDIT AND CREATE VISUAL FOR GOOGLESHEETS

# https://dashboard.sheety.co/projects/62dd73c550d0780ff8083f12/sheets/workouts

# Username: M-Elosegui
# Password: passAPISheety947211
# Authorization Header:
# Authorization: Basic TS1FbG9zZWd1aTpwYXNzQVBJU2hlZXR5OTQ3MjEx

# solucao desta API
# https://gist.github.com/angelabauer/164864b78175bb1ecd3d3fd7f4ee39b7


## OPENAI NATURAL LANGUAGE
# https://openai.com/blog/openai-api/



###########################################

# TESTE API NUTRITIONIX


import requests
import os
import datetime

#
# GENDER = "male"
# WEIGHT_KG = 76
# HEIGHT_CM = 169
# AGE = 30
#
# API_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# ENV_NUTRI_APPID = os.environ.get("ENV_NUTRI_APPID")
# ENV_NUTRI_APPKEY = os.environ.get("ENV_NUTRI_APPKEY")
#
#
# # mac/linux: env too see, export ENVKEY=VALUE to add
# headers = {
#  "x-app-id" : ENV_NUTRI_APPID,
#  "x-app-key" : ENV_NUTRI_APPKEY,
# }
#
# parameters = {
# "query": input("What exercise did you do? \n"),
# "gender": GENDER,
# "weight_kg": WEIGHT_KG,
# "height_cm": HEIGHT_CM,
# "age": AGE,
# }
#
# response =  requests.post(API_endpoint, json=parameters, headers=headers)
# result = response.json()
#
#
# exercise = result["exercises"][0]["user_input"]
# duration = result["exercises"][0]["duration_min"]
# calories = result["exercises"][0]["nf_calories"]
#
# print(result)
# print(len(result["exercises"]))
# print(f"\n You did the exercise: {exercise}, for {duration} minutes, burning a total of {calories} calories.")


############# PARTE DAS SHEETS


SHEETY_URL = "https://api.sheety.co/9f1c054950bde5515b838de90c26c506/apiWorkout/workouts"

# sheety_data = requests.get(SHEETY_URL)
# data_test = sheety_data.json()
# print(data_test)

#NOTES about data: "workout" has to be singular even when workouts is the sheet name. name of columns have to be lowercase. both need to be like this to work.
data = {
    "workout": {
    "date": "today lol",
    "time": "...now",
    "exercise": "slacking",
    "duration": "5",
    "calories": "10",
    }

}


add_value = requests.post(url=SHEETY_URL, json=data)
print(add_value)
print(add_value.status_code)


