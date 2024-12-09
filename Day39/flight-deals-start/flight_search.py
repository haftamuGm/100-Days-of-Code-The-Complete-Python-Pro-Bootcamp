import requests
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN_ENDPOINT="https://test.api.amadeus.com/v1/security/oauth2/token"
AITA_ENDPOINT= "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFER_ENDPOINT="https://test.api.amadeus.com/v2/shopping/flight-offers"
import datetime
today=datetime.datetime(year=2024,month=12,day=8).strftime("%Y-%m-%d")
class Flight_search:
    def __init__(self):
        self.api_key=os.environ.get("AMADEUS_API_KEY")
        self.secret_key=os.environ.get("AMADEUS_SECRET")
        self.token=self.get_token()
    def get_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'client_id': self.api_key,
            'client_secret': self.secret_key,
            'grant_type': 'client_credentials',
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()["access_token"]
    def get_destination(self,city):
        headers={"Authorization": f"Bearer {self.token}"}
        query={
            "keyword":city,
            "max":2,
            "include":"AIRPORTS"
        }
        responce=requests.get(AITA_ENDPOINT, params=query, headers=headers)
        return responce.json()['data'][0]['iataCode']

    def get_city(self,originLocationCode,destinationLocationCode,departureDate,return_date):
        para = {
            "originLocationCode": originLocationCode,
            "destinationLocationCode":destinationLocationCode,
            "departureDate": departureDate.strftime("%Y-%m-%d"),
            "currencyCode": "EUR",
            "returnDate":return_date.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop": "true"
        }
        headers = {
            'Authorization': f"Bearer {self.get_token()}"
        }
        response = requests.get(FLIGHT_OFFER_ENDPOINT, params=para, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"



