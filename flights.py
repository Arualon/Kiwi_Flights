from datetime import datetime,timedelta

class Flight(object):
    """Class for flight"""

    def __init__(self, source, destination, departure, arrival, flight_number, price, bags_allowed, bag_price):
        self.source = source
        self.destination = destination
        self.departure = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S")
        self.arrival = datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S")
        self.flight_number = flight_number
        self.price = int(price)
        self.bags_allowed = int(bags_allowed)
        self.bag_price = int(bag_price)

    def __repr__(self):
        return "{},{},{},{},{},{},{},{}".format(self.source, self.destination, self.departure, self.arrival, self.flight_number, str(self.price), str(self.bags_allowed), str(self.bag_price))

    def find_connections(self, flights):
        """Find all available flights from self to somewhere (in flights) according to limitations: 1-4 hours between flights.. Keep in mind, that condition for bags is not here. Function separate_according_to_bags is for that"""

        available_flights = []
        for flight in flights:
            if (self.destination == flight.source) and (timedelta(hours=4) >= (flight.departure - self.arrival)) and ((flight.departure - self.arrival) >= timedelta(hours=1)):
                available_flights.append(flight)
        return available_flights
