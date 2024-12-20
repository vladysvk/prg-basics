# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.studying = False

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.studying = True
    student2.name = "Olivia"
    student2.age = 21
    student2.studying = True
    student3.name = "Vlad"
    student3.age = 17
    student3.studying = True

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, studying {student1.studying}')
    print(f'{student2.name}, {student2.age} years old, studying {student2.studying}')
    print(f'{student3.name}, {student3.age} years old, studying {student3.studying}')

if __name__ == "__main__":
    main()