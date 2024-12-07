import random

def main():
    print(rand_elem([1,2,3,4,5,8]))
    print(rand_elem([4,22,43,7,4,5,8]))
    print(rand_elem([6,78,143,76,14,75,8]))



def rand_elem(array):
    return random.choice(array)

if __name__ == "__main__":
    main()