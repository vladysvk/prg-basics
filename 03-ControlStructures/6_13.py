car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140

if 40 <= car_speed <= 140:
    print("Car speed is ok")
else:
    print("Invalid car speed")