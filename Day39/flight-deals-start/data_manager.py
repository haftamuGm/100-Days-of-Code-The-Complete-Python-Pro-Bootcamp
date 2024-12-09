import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
MY_SHEET_ENDPOINT="https://api.sheety.co/d51a600a5ea8623d17e0b4062b07f9c0/capstone/prices"
load_dotenv()
class Datamanager:
    def __init__(self):
        self.user_name=os.environ.get("USER_NAME")
        self.password=os.environ.get("PASSWORD")
        self.destination_data={}
    def get_destination_data(self):
        data=requests.get(MY_SHEET_ENDPOINT)
        self.destination_data=data.json()["prices"]
        return self.destination_data
    def update_destination(self):
        for city in self.destination_data:
            parameter={
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            updated=requests.put(f"{MY_SHEET_ENDPOINT}/{city['id']}",json=parameter)
            print(updated.text)


