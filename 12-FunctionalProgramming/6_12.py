ol = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

arr = list(filter(lambda x: x["gold"]+x["silver"]+x["bronze"]>=10, ol))
print(arr)
for i in arr:
    print(f"{i['country']}: {i['gold']},{i['silver']},{i['bronze']}")