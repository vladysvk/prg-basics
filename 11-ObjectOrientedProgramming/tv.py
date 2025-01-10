def main():
    tv1 = TV()
    tv1.show_status()
    tv1.turn_on()
    tv1.show_status()
    tv1.show_channels()
    tv1.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "TET"])
    tv1.show_channels()
    tv1.set_channel(4)
    tv1.increase_volume()
    tv1.increase_volume()
    tv1.show_status()
    tv1.set_channel(1)
    tv1.reduce_volume()
    tv1.show_status()
    tv1.set_channel(6)
    tv1.increase_volume()
    tv1.increase_volume()
    tv1.increase_volume()
    tv1.show_status()
    tv1.turn_off()
    tv1.show_status()


class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            if 0 <= self.channel_no < len(self.channels):
                print(f"TV is turned on!, channel {self.channel_no} ({self.channels[self.channel_no]}), volume {self.volume}")
        else:
           print("TV is turned off!")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        for channel in self.channels:
            print(channel, end=", ")
        print()
    def increase_volume(self):
        if self.volume+1 in range(0, 11):
            self.volume+=1
    def reduce_volume(self):
        if self.volume-1 in range(0, 11):
            self.volume-=1 
if __name__ == "__main__":
    main() 

