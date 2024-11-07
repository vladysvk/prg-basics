def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n * 0.3937

def feet_and_inches_to_cm(n):
    n = str(n)
    feet, inches = n.split(".")
    inches = int(inches)
    feet = int(feet)
    inches += feet * 12
    cm = inches * 2.54
    return cm
    

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"48cm = {cm_to_inch(48): .1f}inches")
    print(f"6.12 feet = {feet_and_inches_to_cm(6.12): .0f}")

