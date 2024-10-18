###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = int(input("Enter bonus to the salary in %: ")) / 100 # 15%

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    pass

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')