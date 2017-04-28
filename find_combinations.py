import sys
import csv
from flights import Flight


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


flights = file_read(sys.stdin)

for bags in range(0,3,1):
    print("///////////////////////////////////// %s BAGS ///////////////////////////////////////////////////" % (bags))

    bag_available_flights = separate_according_to_bags(flights, bags)

    for flight in bag_available_flights:
        list_connections(flight, bag_available_flights, [], bags)
