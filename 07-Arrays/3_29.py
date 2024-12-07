def main():
    arr = create_2d_arr(5, 5)
    print(arr)



def create_2d_arr(x, y):
    return [[0 for i in range(x)] for i in range(y)]
            


if __name__ == "__main__":
    main()