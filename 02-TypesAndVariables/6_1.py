###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Vladyslav'   # replace Anna with your name
surname = 'Kuzil' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_name+characters_in_surname+1} characters') # with a space between name and surname