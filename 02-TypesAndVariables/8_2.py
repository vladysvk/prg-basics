###
# Calculation of circle area and circumference 
#
import math 
# determine radius and PI values
radius = int(input("Enter radius: "))
pi = 3.14
# calculate area 
area = pi*radius**2
# calculate circumference 
circumference = 2*pi*radius
# print results
print(f"Area: {area}")
print(f"Circumference:{circumference}")