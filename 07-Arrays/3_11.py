def main():
    print(bubblesort([2,5,1,2,4,5,7,1,12,6,1,46,685,857]))
    print(bubblesort([2,61,47,1,735,7,1,5,8,3,2,893,457,2]))
    print(bubblesort([3,7,53,34173,352,12,62,4,8,31,568,3,15]))


def bubblesort(array):
    n = len(array) - 1
    sorted = True 

    while sorted:
        sorted = False

        for i in range(n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = True
    return array
if __name__ == "__main__":
    main()