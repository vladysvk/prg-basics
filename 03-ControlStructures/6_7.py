age = int(input("Enter your age"))

if age >= 65:
    print("You are a senior")
elif 20 <= age <= 64:
    print("You are a adult")
elif 13 <= age <= 19:
    print("You are a teen")
elif 0 < age < 13:
    print("You are a child")
else:
    print("You haven't been born yet")

