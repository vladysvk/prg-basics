###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import input_types # your own defined module

# Reads employee's data from keyboard
first_name = input_types.input_string('Enter name: ')
last_name = input_types.input_string("Enter last name: ")
age = input_types.input_integer("Enter age: ")
salary = input_types.input_real("Enter salary")
is_salary_hidden = input_types.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print("Last name:", last_name)
print("Age:", age)

if is_salary_hidden:
    print(f'Salary: {salary: .2f}')