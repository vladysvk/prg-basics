import random

def main():
    thermometer = Thermometer()
    thermometer.turn_on()
    thermometer.measure_temperature()
    thermometer.display_temperature()
    thermometer.turn_off()
class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0
    
    def measure_temperature(self):
        self.temperature = round(random.uniform(36.0, 42.1), 1)
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False   
    def display_temperature(self):
        if self.temperature >= 41:
            print("CRITICAL TEMPERATURE!")
        elif self.temperature >= 37:
            print(f"Temperature: {self.temperature}C (fever)")
        else:
            print(f"Temperature {self.temperature}")
            
if __name__ == "__main__":
    main() 