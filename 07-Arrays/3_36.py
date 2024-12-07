def main():
    print_1d(convert_to_1D([[2,3],[1,5]]))
    print_1d(convert_to_1D([[5,0,3,7,5],[9,0,9,1,2]]))
    print_1d(convert_to_1D([[2,1],[3,5],[7,4],[2,6]]))



def convert_to_1D(array):
    new_arr = []
    for i in array:
        for j in i:
            new_arr.append(j)
    return new_arr


def print_1d(array):
    for i in array:
        print(i, end=" ")
    print()
    


if __name__ == "__main__":
    main()