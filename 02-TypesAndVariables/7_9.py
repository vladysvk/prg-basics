import random

dice_number = random.randint(1, 6)
dice_number_binary = dice_number == 1 or dice_number == 6
print(f"Special number (1 or 6): {dice_number_binary}")