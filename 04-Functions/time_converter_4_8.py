def main():
    hours = (input("Enter hours: "))
    minutes = (input("Enter minute: "))
    time_format = input("Enter time format: ")
    time = time_string(hours, minutes, time_format)
    print(time)



def time_string(hours, minutes, time_format):
    hours = int(hours)
    minutes = int(minutes)
    if 0 <= hours <= 23 and 0 <= minutes <= 59:  
        if minutes < 10:
            minutes = f"0{minutes}"
        if time_format == "24":
            if hours < 10:
                return f"0{hours}:{minutes}"
            else:
                return f"{hours}:{minutes}"
        elif time_format == "12":
            if hours <= 12:
                if hours == 0:
                    return f"12:{minutes}am"
                else:
                    return f"{hours}:{minutes}am"
            else:
                hours -= 12
                return f"{hours}:{minutes}pm"


if __name__ == "__main__":
    main()