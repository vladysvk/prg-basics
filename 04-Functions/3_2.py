###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

def main():
    random_num = dice()
    print(random_num)

def dice():
    rand = random.randint(1, 6)
    return rand

if __name__ == "__main__":
    main()
