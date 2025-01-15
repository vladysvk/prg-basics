import statistics

grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
grades_without_two = list(filter(lambda x: x > 2.0, grades))
avg = statistics.mean(grades_without_two)
print(f"Arithmetic mean for grades <> 2.0 is {round(avg, 2)}")