import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()
sheet_endpoint = "https://api.sheety.co/1d05cf9c637366d15a4f2bed547f8db4/flightDeals/prices"

class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.sheet_data = {}

    def get_destination_data(self):
        response = requests.get(url = sheet_endpoint, auth = self._authorization)
        response.raise_for_status()
        print(response.status_code)
        self.sheet_data = response.json()
        return self.sheet_data

    def update_data(self, row_id, iata_code):
        data = {"price": {"iataCode": iata_code}}
        response = requests.put(url=f"{sheet_endpoint}/{row_id}", json=data, auth=self._authorization)
        response.raise_for_status()