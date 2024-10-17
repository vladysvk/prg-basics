###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
# Calculate feet and remaining inches
feet = cm // 30.48
inches = cm / 30.48 % 1

# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches: .1f} inches')