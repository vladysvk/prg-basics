price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

total = 0
for key,value in price_list.items():
    total+=value
    print(f"{key} : {value}")
print(f"{total: .2f}")


for key,value in price_list.items():
    price_list[key] = value - value/10
total_disc = 0
for key,value in price_list.items():
    total_disc+=value
    print(f"{key} : {value: .2f}")
print(f"{total_disc: .2f}")