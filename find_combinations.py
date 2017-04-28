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

    def find_connections(self, flights):
        """Find all available flights from self to somewhere (in flights) according to limitations: 1-4 hours between flights.. Keep in mind, that condition for bags is not here. Function separate_according_to_bags is for that"""

        available_flights = []
        for flight in flights:
            if (self.destination == flight.source) and (timedelta(hours=4) >= (flight.departure - self.arrival)) and ((flight.departure - self.arrival) >= timedelta(hours=1)):
                available_flights.append(flight)
        return available_flights


def file_read(file_flights):
    """Reading flights from file"""

    flights = []
    reader = csv.DictReader(file_flights)
    for row in reader:
        flight = Flight(row['source'], row['destination'], row['departure'], row['arrival'], row[
                        'flight_number'], row['price'], row['bags_allowed'], row['bag_price'])
        flights.append(flight)
    return flights


def separate_according_to_bags(flights, bags):
    """Separate the number of available flights according to number of needed bags"""

    nflights = []
    for flight in flights:
        if flight.bags_allowed >= bags:
            nflights.append(flight)
    return nflights


def list_connections(nflight, flights, connections, bags):
    """Find list of all consecutive flights from nflight in flights"""

    connections.append(nflight)
    flight_connections = nflight.find_connections(flights)
    if flight_connections != []:
        for flight in flight_connections:
            list_connections(flight, flights, connections, bags)
            connections.pop(len(connections) - 1)
    else:
        validate_and_print_result(connections, bags)
        connections = []


def validate_and_print_result(connections, bags):
    """Validates consecutive flights to meet conditions: A-B-A is valid, A-B-A-B is not valid"""

    for i in range(0, len(connections), 1):
        for k in range(i + 1, len(connections), 1):
            if (connections[k].source == connections[i].source) and (connections[k].destination == connections[i].destination):
                connections = connections[0:k - 1:1]
                break
    if len(connections) > 1:
        price = 0
        print("%s -> " % (connections[0].source), end="")
        for flight in connections:
            print("%s" % (flight.destination), end=" -> ")
            price += flight.price + bags * flight.bag_price
        print(str(price) + " €")





data = sys.stdin.readlines()

print("///////////////////////////////////// 0 BAGS ///////////////////////////////////////////////////")
bags = 0

flights = file_read(data)
flights = separate_according_to_bags(flights, bags)

for flight in flights:
    list_connections(flight, flights, [], bags)


print("///////////////////////////////////// 1 BAGS ///////////////////////////////////////////////////")
bags = 1

flights = file_read(data)
flights = separate_according_to_bags(flights, bags)

for flight in flights:
    list_connections(flight, flights, [], bags)


print("///////////////////////////////////// 2 BAGS ///////////////////////////////////////////////////")
bags = 2

flights = file_read(data)
flights = separate_according_to_bags(flights, bags)

for flight in flights:
    list_connections(flight, flights, [], bags)
