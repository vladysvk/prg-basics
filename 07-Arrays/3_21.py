def main():
    arr = [1,2,34,4,6,7,8]
    arr2 = [1,2,34,4]
    if is_subset(arr, arr2):
        print(f"Array {arr2} is a subset of {arr}")
    else:
        print(f"Array {arr2} isn't a subset of {arr}")

def is_subset(arr, arr2):
    lenght = len(arr2)
    subset = arr[:lenght]

    for i in range(lenght):
        if subset[i] != arr2[i]:
            return False
    return True


if __name__ == "__main__":
    main()