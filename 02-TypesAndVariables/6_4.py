###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:-1]}')
print(f'Initials: {employee[0]+employee[4]+employee[9]}')