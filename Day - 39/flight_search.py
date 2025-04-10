import requests
import constants as const
import Dummy
from datetime import datetime as dt
from dateutil.relativedelta import *

class FlightSearch:

    def __init__(self):
        self.bearer_token = ""
        self.login_token()
        self.origin_code = self.fetch_iata(const.CURRENT_PLACE)


    def login_token(self):
        login_data = {
            'grant_type' : 'client_credentials',
            'client_id' : Dummy.AMADEUS_API_KEY,
            'client_secret' : Dummy.AMADEUS_API_SECRET
        }

        try:
            token_response = requests.post(url=const.AMADEUS_LOGIN_API, data=login_data)
            token_response.raise_for_status()
            token_data = token_response.json()
            self.bearer_token = f"{token_data['token_type']} {token_data['access_token']}"
        except requests.exceptions.RequestException as err:
            print("Login Token Function error as ", err)

    def search_flights(self, destination_code: str):
        flight_headers = {
            'Authorization': self.bearer_token,
        }

        date = dt.now() + relativedelta(months=+6)
        journey_date = date.strftime("%Y-%m-%d")

        flight_data = {
            'originLocationCode': self.origin_code,
            'destinationLocationCode': destination_code,
            'departureDate': journey_date,
            'adults': 2,
            'max': 5
        }

        print(flight_data)
        try:
            response = requests.get(url=const.AMADEUS_FLIGHT_OFFERS_API, headers=flight_headers,
                                    params=flight_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            self.login_token()
            self.search_flights(destination_code)

    def fetch_iata(self, city_name):
        city_headers = {
            'Authorization': self.bearer_token,
        }

        city_data = {
            'subType': 'CITY',
            'keyword': city_name
        }

        try:
            response = requests.get(url=const.AMADEUS_FETCH_IATA_API, headers=city_headers,
                                    params=city_data)
            response.raise_for_status()
            fetched_data = response.json()['data']
            for n_dict in fetched_data:
                if n_dict['name'].lower() == city_name.lower():
                    return n_dict['iataCode']

            return None
        except requests.exceptions.RequestException:
            self.login_token()
            self.fetch_iata(city_name)

