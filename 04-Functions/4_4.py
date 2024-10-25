###
# Calculates the sum of the digits in a number
#
def main():
    any_number = int(input('Enter integer number: '))
    result = sum_digits(any_number)
    print(f'The sum of the digits in the number {any_number} is {result}')


def sum_digits(number):
    sum = 0
    if number < 0:
        number = abs(number)
    elif number == 0:
        return 0
    
    
    for i in str(number):
        sum += int(i)
    return sum

if __name__ == "__main__":
    main()