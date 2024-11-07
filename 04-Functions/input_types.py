###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    integer = input(message)
    return int(integer)

def input_real(message):
    real = input(message)
    return float(real)

def input_boolean(message):
    boolean = input(message)
    if boolean == "y":
        return False
    elif boolean == "n":
        return True
    