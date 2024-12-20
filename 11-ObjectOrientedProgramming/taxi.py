class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance: {self.distance}km")
        print(f"Rate per KM: {self.rate_per_km}")
        print(f"Fare: {self.fare}")

def main():
    taxi_ride1 = TaxiRide(2)
    taxi_ride2 = TaxiRide(3)
    taxi_ride1.calculate_fare(100)
    taxi_ride2.calculate_fare(200)
    taxi_ride1.print_receipt()
    taxi_ride2.print_receipt()

if __name__ == "__main__":
    main()
