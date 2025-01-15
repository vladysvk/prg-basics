temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

arr = list(filter(lambda x: temp[x] > 0, temp))
print(arr)