import Pyro4


ns = Pyro4.locateNS()
uri = ns.lookup('Airport')
airport = Pyro4.Proxy(uri)

# Printing our tables in db Airport
print(airport.show_airlines_str())
print(airport.show_flights_str())

# Flights in airline 1
print(airport.show_flights_for_airline_str(1))

# Adding flight and airline
airport.add_flight(6,3, "BERLIN", '2024-04-15 15:25:00', '2024-04-15 18:00:00')
airport.add_airline(4, "BNC")
print(airport.show_airlines_str())
print(airport.show_flights_str())

# Changing flight and airline
airport.change_airline(4, "WWW")
airport.change_flight(6, 1, 'MOSCOW', '2024-04-15 18:00:00', '2024-04-15 18:00:00')
print(airport.show_airlines_str())
print(airport.show_flights_str())

# Deleting flight and airline
airport.delete_flight(6)
airport.delete_airline(4)
print(airport.show_airlines_str())
print(airport.show_flights_str())

# Searching flight and airline by IDs
print(airport.search_airline_str(1))
print(airport.search_flight_str(1))

