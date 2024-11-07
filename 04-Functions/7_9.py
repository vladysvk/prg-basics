def main():
    print(f(3124, False))


def f(number, even):
    sum = 0
    for integer in str(number):
        integer = int(integer)
        if even:
            if integer % 2 == 0:
                sum+=integer
        elif even == False:
            if integer % 2 != 0:
                sum+=integer
    return sum


if __name__ == "__main__":
    main()