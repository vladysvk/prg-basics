def main():
    avg_speed = lambda distance, hours, minutes: distance/(hours*60+minutes)*60
    print(round(avg_speed(70, 1, 23),1),"km/h")


if __name__ == "__main__":
    main()