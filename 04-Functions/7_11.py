def main():
    print(f(1, 8, 12))


def f(n1, n2, n3):
    is_negative = False
    if n1 < 0 or n2 < 0 or n3 < 0:
        is_negative = True
    return is_negative

if __name__ == "__main__":
    main()