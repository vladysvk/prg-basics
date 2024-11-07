def main():
    print(f(1))


def f(n):
    asterix_string = ""
    while n > 0:
        asterix_string+="*"
        if (n - 1) > 0:
            asterix_string += "/"
        n -= 1
    return asterix_string
        


if __name__ == "__main__":
    main()