###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
questions_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer:
      correct_answers += 1 

# calculates the number of incorrect answers
incorrect_answers = 0
for answer in test_results:
   if answer == False:
      incorrect_answers += 1 

# calculates the percentage of correct answers
percentage = 100/questions_number * correct_answers

print('TEST STATISTICS')
print('===============')
print('Number of questions:', questions_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', percentage)
