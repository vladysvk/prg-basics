time = input("Enter time (24-hour format): ")
hours, minutes = time.split(":")

if int(hours) <= 12:
    print(f"Time in 12-hour format: {hours}:{minutes}am")
else:
    print(f"Time in 12-hour format: {int(hours) - 12}:{minutes}pm")
