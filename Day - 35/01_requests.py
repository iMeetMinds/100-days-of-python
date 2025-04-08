import requests
import Dummy

API_KEY = Dummy.OWF_API_KEY
MY_LAT = -5.525830
MY_LNG = -47.477032

parameters = {
    'lat' : MY_LAT,
    'lon' : MY_LNG,
    'appid' : API_KEY
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather_data = response.json()

is_rain = [n for n in weather_data['list'][0:6] if n['weather'][0]['id'] < 700]

if len(is_rain) > 0:
    print('Bring Umbrella. There will be rain.')
