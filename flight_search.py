import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv()

token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(url = token_endpoint, headers = header, data = body)
        response.raise_for_status()
        token = response.json()["access_token"]
        print(token)
        return token
    
    def get_iata_code(self, city_name):
        fallback_iata = {
        "Paris": "PAR",
        "Frankfurt": "FRA",
        "Tokyo": "TYO",
        "Hong Kong": "HKG",
        "Istanbul": "IST",
        "Kuala Lumpur": "KUL",
        "New York": "NYC",
        "San Francisco": "SFO",
        "Dublin": "DUB"
    }
        header = {"Authorization": f"Bearer {self._token}"}
        parameters = {
            "keyword": city_name,
            "subType": "CITY",
        }
        try:
            response = requests.get(url = city_search_endpoint, headers = header, params= parameters)
            response.raise_for_status()
            result = response.json()
            if "data" in result and len(result["data"]) > 0:
                return result["data"][0]["iataCode"]
            else:
                return "UNKNOWN"
        except requests.exceptions.RequestException:
                return fallback_iata.get(city_name,"UNKNOWN")

    def search_flights(self, origin, destination):
        return [
        {"price": 450, "date": "2025-01-10"},
        {"price": 380, "date": "2025-02-05"},
        {"price": 299, "date": "2025-04-02"},
        {"price": 410, "date": "2025-05-20"},
    ]