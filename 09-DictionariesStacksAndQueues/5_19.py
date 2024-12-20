import json

def main():
    data = get_data()
    print(f"Number of rooms: {number_of_rooms(data)}")
    print(f"Number of paid reservations: {number_of_paid_reservations(data)}")
    print(f"Number of inpaid reservations: {number_of_unpaid_reservations(data)}")
    print(f"Total value of paid reservations: {value_of_paid_reservations(data)}")
    print(f"Total value of unpaid reservations: {value_of_unpaid_reservations(data)}")


def get_data():
    with open("reservations.json") as file:
        return json.load(file)["reservations"]

def number_of_rooms(data):
    return len(data)

def number_of_paid_reservations(data):
    count = 0
    for cell in data:
        if cell["paid"]:
            count+=1
    return count

def value_of_unpaid_reservations(data):
    count = 0
    for cell in data:
        if cell["paid"] == False:
            count+=1
    return count

def value_of_paid_reservations(data):
    sum = 0
    for cell in data:
        if cell["paid"]:
            sum+=cell["price_per_night"]
    return sum

def number_of_unpaid_reservations(data):
    sum = 0
    for cell in data:
        if cell["paid"] == False:
            sum+=cell["price_per_night"]
    return sum

if __name__ == "__main__":
    main()