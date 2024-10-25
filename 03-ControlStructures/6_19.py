first_question = input("SURVEY Are you interested in computer science (y/n): ")
second_question = input("Do you like playing computer gmaes (y/n): ")
third_question = input("Do you have an Instargam account (y/n): ")

if first_question == "y":
    first_question = True
else:
    first_question = False

if second_question == "y":
    second_question = True
else:
    second_question = False

if third_question == "y":
    third_question = True
else:
    third_question = False


if first_question == True:
    print("SURVEY RESULTS Intererested in computer science: Yes")
else:
    print("SURVEY RESULTS Interested in computer science: No")

if second_question == True:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if second_question == True:
    print("Has an instagram account: Yes")
else:
    print("Has an instagram account: No")