dogs_years_human = int(input("Enter dogs years: "))
dogs_years = 0

if dogs_years_human > 0:
    if dogs_years_human == 1:
        dogs_years = 10.5 / 2
    elif dogs_years_human == 2:
        dogs_years == 10.5
    else:
        dogs_years_human -= 2
        dogs_years = 10.5
        dogs_years += dogs_years_human * 4
else:
    print("Dog hasn't been born yet")

print(f"Dog is {dogs_years} years old in dogs years")