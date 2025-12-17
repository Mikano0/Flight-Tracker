class FlightData:
    def __init__(self, flights):
        self.flights = flights

    def find_cheapest_flight(self):
        cheapest = self.flights[0]
        for flight in self.flights:
            if flight["price"] < cheapest["price"]:
                cheapest = flight
        return cheapest