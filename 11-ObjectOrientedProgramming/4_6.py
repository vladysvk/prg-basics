def main():
    account = Account("12 3456 5555 9090 1111 0000 7722")
    account.display_balance()
    account.deposit()
    account.display_balance()
    account.withdraw()
    account.display_balance()
    account.withdraw()
    account.display_balance()

class Account:
    def __init__(self, number):
        self.bank_number = number
        self.balance = 0

    def deposit(self,):
        deposite_amount = float(input("Enter amount: "))
        if deposite_amount > 0:
            self.balance+=deposite_amount
    
    def withdraw(self):
        withdraw = float(input("Enter amounth of withdrawal"))
        if withdraw < self.balance:
            self.balance-=withdraw

    def display_balance(self):
        print(f"Balance: {self.balance}")
if __name__ == "__main__":
    main()