def main():
    print(C("Anna","May",17,7))
    print(C("George","Brown",21,4))
class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age<=17:
            return f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"
        else:
            return f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}"

    

if __name__ == "__main__":
    main()