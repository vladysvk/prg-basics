arr =[508,500,512,499,492,511,503,476,501,509]
length = len(arr)
tollerance = 500/100*2

arr1 = list(filter(lambda x: not (500-tollerance <= x <= 500+tollerance),arr))

length1 = len(arr1)

per = int(length1/length*100)
print(f"Bottle capacity:    500ml\nFilling tolerance   2%\nFilled bottles:     ",end="")
print(*arr, sep=",", end="")
print(f"\nIncorrectly filled: {per}%")
