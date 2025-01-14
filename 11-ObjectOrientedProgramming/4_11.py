def main():
    c = C({"A":120,"D":150,"G":90,"K":110})
    c.m1("G",130)
    print(c.m2("GD"))
    print(c.m2("KEJ"))
class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self,s,n):
        self.sectors[s] = n
    
    def m2(self,s):
        sum = 0
        for i in s:
            if i in self.sectors:
                sum+=self.sectors[i]
        return sum
    
if __name__ == "__main__":
    main()