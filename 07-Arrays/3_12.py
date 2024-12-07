def main():
    print_elements(arr)



elements = {}
arr = [2, 3, 2, 5, 8, 1, 9, 8]


def print_elements(arr):
    for i in arr:
        if i in elements:
            elements[i] += 1
        else:
            elements[i] = 1

    for key, value in elements.items():
        if value == 1:
            print(key)


if __name__ == "__main__":
    main()