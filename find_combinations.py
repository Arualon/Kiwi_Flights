import sys
import csv

class Flight(object):
    """Class for one flight"""

    def __init__(self, source, destination, departure, arrival, flight_number, price, bags_allowed, bag_price):
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.flight_number = flight_number
        self.price = price
        self.bags_allowed = bags_allowed
        self.bag_price = bag_price

    def __repr__(self):
        return "{},{},{},{},{},{},{},{}".format(self.source, self.destination, self.departure, self.arrival, self.flight_number, str(self.price), str(self.bags_allowed), str(self.bag_price))


"""test = Flight("USM","HKT","2017-02-11T06:25:00","2017-02-11T07:25:00","PV404",24,1,9)
print (test)"""

def file_read(file_flights):
    flights = []
    reader = csv.DictReader(file_flights)
    for row in reader:
        flight = Flight(row['source'],row['destination'],row['departure'],row['arrival'],row['flight_number'],row['price'],row['bags_allowed'],row['bag_price'])
        flights.append(flight)
    """Testing functionality
    for flight in flights:
        print(flight)"""

file_read(sys.stdin.readlines())
