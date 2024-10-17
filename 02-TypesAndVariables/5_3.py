###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_volume = a*b*c
cuboid_area = 2*(a*b + a*c + b*c)
print(f"The volume of cuboid with sides {a}, {b}, {c} is {cuboid_volume}")
print(f"The surface area of cuboid with sides {a}, {b}, {c} is {cuboid_area}")
