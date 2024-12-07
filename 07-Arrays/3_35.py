def main():
    print_matrix(transpose([[1,2,3,4,5], [6,7,8,9,0]]))
    print_matrix(transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print_matrix(transpose([[5,6,7,8]]))


def transpose(matrix):
    transposed = [[0]*len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()
    print()


if __name__ == "__main__":
    main()