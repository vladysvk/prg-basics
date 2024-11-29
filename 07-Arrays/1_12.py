categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

biggest = expenses[0]
biggest_index = 0
for i in range(1, len(expenses)):
    if expenses[i] > biggest:
        biggest = expenses[i]
        biggest_index = i
print(f"The most expesive category is {categories[biggest_index]}")