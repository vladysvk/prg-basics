###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = float(input("Enter the temperature in celsius: "))
kelvin = celsius + 273.15
fahrenheit = (9/5 * celsius) + 32
print(f"Temperature in Kelvin: {kelvin}")
print(f"Temperature in Fahrenheit: {fahrenheit}")
