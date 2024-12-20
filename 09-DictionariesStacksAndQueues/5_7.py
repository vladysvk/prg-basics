def main():
    print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
    print(f"Average hotel price in Krakow: {avg_price(hotels_in_Krakow)}")
    print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
    print(f"Average hotel price in Sopot: {avg_price(hotels_in_Sopot)}")
    if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
        print("Cheaper hotels in: Krakow")
    else:
        print("Cheaper hotels in: Sopot")

def hotel_list(hotels):
    string = hotels[0]["name"]
    for hotel in range(1, len(hotels)):
        string += f', {hotels[hotel]["name"]}'
    return string

def avg_price(hotels):
    n = 0
    sum = 0
    for hotel in hotels:
        n+=1
        sum+=hotel["price"]

    return sum / n


hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]



if __name__ == "__main__":
    main()