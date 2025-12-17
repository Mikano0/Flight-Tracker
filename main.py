#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
data_manager.get_destination_data()

codes = [code["iataCode"] for code in data_manager.sheet_data["prices"]] # prices is the entire sheet 
print(codes)
for row in data_manager.sheet_data["prices"]:
    if row["iataCode"] == "":
        city_name = row["city"]
        iata_code = flight_search.get_iata_code(city_name)
        row["iataCode"] = iata_code
        data_manager.update_data(row["id"], iata_code)

pprint(data_manager.sheet_data["prices"])  

for row in data_manager.sheet_data["prices"]:
    sheet_price = row["lowestPrice"]
    destination_code = row["iataCode"]

  
    flights = flight_search.search_flights("LON", destination_code)


    flight_data = FlightData(flights)
    cheapest_flight = flight_data.find_cheapest_flight()

  
    if cheapest_flight["price"] < sheet_price:
        message = f" DEAL FOUND! {row['city']}: ${cheapest_flight['price']} on {cheapest_flight['date']}"
        print(message)
        

        notification_manager.send_mail("Flight Deal Alert!", message)
