def main():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minute: "))
    time_format = int(input("Enter time format: "))
    time_string(hours, minutes, time_format)

def time_string(hours, minutes, time_format):
    if time_format == 24:
        print(f"{hours}:{minutes}")
    elif time_format == 12:
        if hours <= 12:
            print(f"{hours}:{minutes}am")
        else:
            hours -= 12
            print(f"{hours}:{minutes}pm")


if __name__ == "__main__":
    main()