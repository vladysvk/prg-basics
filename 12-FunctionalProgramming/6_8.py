arr = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit

min_70 = min_pts(70)
min_40 = min_pts(40)
min_30 = min_pts(30)

arr_70 = list(filter(min_70, arr))
arr_40 = list(filter(min_40, arr))
arr_30 = list(filter(min_30, arr))

print(arr_70)
print(arr_40)
print(arr_30)