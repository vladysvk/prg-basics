###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#

day_number = int(input("Enter the number of the day of the week from 1 to 7: "))

def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n]


print(weekday(day_number - 1))
print(weekday(0))
print(weekday(3))
print(weekday(6))
