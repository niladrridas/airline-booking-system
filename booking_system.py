import random

class Airline:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, airline, flight_number, origin, destination, departure_time, arrival_time, price):
        self.airline = airline
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price

class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

class BookingSystem:
    def __init__(self):
        self.airlines = []
        self.flights = []
        self.passengers = []
        self.bookings = {}

    def add_airline(self, airline):
        self.airlines.append(airline)

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def book_flight(self, flight, passenger):
        # Check if the flight exists
        if flight in self.flights:
            # Book the flight for the passenger
            print(f"{passenger.name} booked flight {flight.flight_number} with {flight.airline.name} from {flight.origin} to {flight.destination}, departure: {flight.departure_time}.")
            self.bookings[(passenger.name, passenger.passport_number)] = flight.flight_number
        else:
            print("Flight not found.")

    def generate_passengers(self, count):
        first_names = ["John", "Alice", "Bob", "Emily", "Michael", "Sophia", "David", "Emma", "James", "Olivia"]
        last_names = ["Smith", "Johnson", "Brown", "Lee", "Garcia", "Martinez", "Lopez", "Young", "Wang", "Kim"]

        for _ in range(count):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            name = f"{first_name} {last_name}"
            passport_number = ''.join(random.choices('0123456789', k=10))  # Generate a random 10-digit passport number
            passenger = Passenger(name, passport_number)
            self.add_passenger(passenger)

    def generate_flights(self):
        destinations = ["LHR", "JFK", "FRA", "SFO", "CDG", "HND", "PEK", "DXB", "LAX", "AMS"]
        airlines = [Airline("British Airways"), Airline("American Airlines"), Airline("Lufthansa"), Airline("United Airlines"), Airline("Air France")]

        for _ in range(200):
            airline = random.choice(airlines)
            flight_number = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + ''.join(random.choices('0123456789', k=3))
            origin = random.choice(destinations)
            destination = random.choice(destinations)
            while destination == origin:
                destination = random.choice(destinations)
            departure_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
            arrival_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
            price = random.randint(200, 1000)
            flight = Flight(airline, flight_number, origin, destination, departure_time, arrival_time, price)
            self.add_flight(flight)

    def search_booking_by_passenger(self, passenger_name):
        for passenger, flight_number in self.bookings.items():
            if passenger_name.lower() in passenger[0].lower():
                print(f"Passenger {passenger[0]} with passport number {passenger[1]} booked flight {flight_number}.")
                return
        print("Passenger not found.")

    def search_loop(self):
        while True:
            search_input = input("Enter passenger name to search booking details (type 'exit' to quit): ")
            if search_input.lower() == "exit":
                print("Exiting search loop.")
                break
            self.search_booking_by_passenger(search_input)

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Generate airlines
    for name in ["British Airways", "American Airlines", "Lufthansa", "United Airlines", "Air France"]:
        airline = Airline(name)
        booking_system.add_airline(airline)

    # Generate flights
    booking_system.generate_flights()

    # Generate passengers
    booking_system.generate_passengers(200)

    # Booking flights for random passengers
    for passenger in booking_system.passengers:
        flight = random.choice(booking_system.flights)
        booking_system.book_flight(flight, passenger)

    # Search loop
    booking_system.search_loop()
