def main():
    phone = Phone("black", 1000, 512)
    print(f"Color: {phone.color}\nPrice: {phone.price}\nMemory: {phone.memory}")
    phone.turn_on()
    phone.make_photo()
    phone.turn_off()    




class Phone():
    def __init__(self, color, price, memory):
        self.color = color
        self.price = price
        self.memory = memory

    def make_photo(self):
        print("Photo has been made")
    
    def turn_on(self):
        print("Smartphone has been turned on!")

    def turn_off(self):
        print("Smartphone has been turned off!")
        

if __name__ == "__main__":
    main()