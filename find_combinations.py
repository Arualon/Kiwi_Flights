import sys
import csv
from datetime import datetime
from datetime import timedelta

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

    def find_connections(self,flights):
        available_flights = []
        for flight in flights:
            if (self.destination == flight.source) and (timedelta(hours=4) >= (flight.departure - self.arrival)) and ((flight.departure - self.arrival) >= timedelta(hours=1)):
                available_flights.append(flight)
        return available_flights


def file_read(file_flights):
    """Reading flights  from file"""

    flights = []
    reader = csv.DictReader(file_flights)
    for row in reader:
        flight = Flight(row['source'], row['destination'], row['departure'], row['arrival'], row[
                        'flight_number'], row['price'], row['bags_allowed'], row['bag_price'])
        flights.append(flight)
    return flights


def separate_according_to_bags(flights, bags):
    """Seperate the number of available flights according to number of needed bags"""

    nflights = []
    for flight in flights:
        if int(flight.bags_allowed) >= bags:
            nflights.append(flight)
    return nflights


bags = 0

flights = file_read(sys.stdin)
flights = separate_according_to_bags(flights, bags)

# available_flights=flights[1].find_connections(flights)
# for flight in available_flights:
#     print(flight)
