def main():
    print(round(avg_speed(70, 1, 23),1),"km/h")
def avg_speed(distance, hours, minutes):
    return distance/(hours*60+minutes)*60

if __name__ == "__main__":
    main()