def main(): 
    c = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(c.m(2))
    print(c.m(3))

class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        counter = 0
        for coordinate in self.coordinates:
            if coordinate[0]>0 and coordinate[1]>0:
                counter+=1
        if n <= counter:
            return True
        else:
            return False


if __name__ == "__main__":
    main()