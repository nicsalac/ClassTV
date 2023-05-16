class TV:
    #Construct a TV object
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        on = False
    #Methods

    def power_off(self):
        if self.on == True:
            self.on += False
        if self.on == False:
            self.on += True

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume
    
    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

tv1 = TV(30, 3, True)
tv2 = TV(3, 2, True)
print("tv1's channel is", int(tv1.channel), "and volume level is", int(tv1.volume) )
print("tv2's channel is", int(tv2.channel), "and volume level is", int(tv2.volume) )
