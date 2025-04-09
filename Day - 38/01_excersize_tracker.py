import requests
from datetime import datetime as dt
import Dummy

headers = {
    'x-app-id' : Dummy.NUTRITIONIX_APP_ID,
    'x-app-key' : Dummy.NUTRITIONIX_API_KEY
}

NUTRITIONIX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

body = {
    'query' : input('Enter your details : ')
}

response = requests.post(url=NUTRITIONIX_URL, headers=headers, json=body)
response.raise_for_status()
if response.text:
    exercises = response.json()['exercises']

    today = dt.now()
    for exercise in exercises:
        workout_req = {
            'workout' : {
                'date' : today.strftime("%d/%m/%Y"),
                'time' : today.strftime("%H:%M:%S"),
                'exercise' : exercise["name"].title(),
                'duration' : exercise["duration_min"],
                'calories' : exercise["nf_calories"],
            }
        }

        workout_headers = {
            'Authorization' : Dummy.SHEETY_AUTH_TOKEN
        }

        response_sheet = requests.post(url='https://api.sheety.co/a347ba7c681b83a5839ac9b0c1311d70/myWorkouts/workouts', json=workout_req, headers=workout_headers)
        response_sheet.raise_for_status()
