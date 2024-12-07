def main():
    print_matrix(identity_matrix(3))
    print_matrix(identity_matrix(5))
    print_matrix(identity_matrix(8))
    


def identity_matrix(n):
    identity = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        identity[i][i] = 1
    return identity

def print_matrix(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print("")
    print()


if __name__ == "__main__":
    main()