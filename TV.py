class TV:
    #Construct a TV object
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume
    #Methods
    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume
    
    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

tv1 = TV(30, 3)
tv2 = TV(3, 2)
print("tv1's channel is", int(tv1.channel), "and volume level is", int(tv1.volume) )
print("tv2's channel is", int(tv2.channel), "and volume level is", int(tv2.volume) )
