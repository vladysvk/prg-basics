def main():
    statistics = Statistics()
    statistics.add_number()
    statistics.add_number()
    statistics.add_number()
    statistics.add_number()
    statistics.add_number()
    statistics.display_set()
    statistics.greatest()
    statistics.smallest()
    statistics.arithmetic_mean()
    statistics.calculate_median()
    statistics.quantities_values()
class Statistics:
    def __init__(self):
        self.numbers = []
        self.greatest_num = None
        self.smallest_num = None
        self.mean = None
        self.median = None
    def add_number(self):
        self.numbers.append(int(input("Enter a number: ")))

    def display_set(self):
        print(self.numbers[0], end="")
        for i in range(1, len(self.numbers)):
            print(f", {self.numbers[i]}", end="")
        print()
    def greatest(self):
       self.greatest_num = sorted(self.numbers)[-1]
    
    def smallest(self):
        self.smallest_num = sorted(self.numbers)[0]
    
    def arithmetic_mean(self):
        sum = 0
        for i in self.numbers:
            sum+=i
        self.mean = sum / len(self.numbers)

    def calculate_median(self):
        self.numbers = sorted(self.numbers) 
        if len(self.numbers) % 2 == 0:
            self.median = (self.numbers[len(self.numbers)/2] + self.numbers[len(self.numbers)+1])/2
        else:
            self.median = self.numbers[len(self.numbers)//2+1]
    
    def quantities_values(self):
        print(f"Minimum: {self.smallest_num}, maximum: {self.greatest_num}, arithmetic mean: {self.mean}, median: {self.median}")

    
if __name__ == "__main__":
    main()