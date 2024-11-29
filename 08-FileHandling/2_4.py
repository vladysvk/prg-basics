###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, "r") as file:
    with open(position_file, "w") as second_file:
        for line in file:
            if job_title in line:
                second_file.write(f"{line.split(',')[1]} {line.split(',')[0]} \n")