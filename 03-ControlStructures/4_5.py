###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    position = ord(char)
    
    # add one to the character's code
    position += 1
    # replace new character code with its
    # corresponding character (use chr())
    new_character = chr(position)
    # add encrypted character to encrypted text
    encrypted_text += new_character

print(plain_text)
print(encrypted_text)