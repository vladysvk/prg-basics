def main():
    print(total())

def total():
    total_hours = 0
    winter_semester = {"math":60,"programming":30, "history":15}
    for subject in winter_semester.values():
        total_hours += subject

    return total_hours

if __name__ == "__main__":
    main()