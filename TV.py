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
    #Sets channel
    def set_channel(self, channel):
        self.channel = channel
    #Sets volume level 
    def set_volume(self):
        self.volume = volume
    #Increases channel number by 1 
    def channel_up(self):
        self.channel = channel
        return self.channel + 1
    #Decreases channel number by 1
    def channel_down(self):
        self.channel = channel
        return self.channel - 1
    #Increases the volume level by 1
    def volume_up(self):
        self.volume = volume
        return self.volume + 1
    #Decreases the volume level by 1
    def volume_dowm(self):
        self.volume = volume
        return self.volume -1
    

tv1 = TV(30, 3, True)
tv2 = TV(3, 2, True)
print("tv1's channel is", int(tv1.channel), "and volume level is", int(tv1.volume) )
print("tv2's channel is", int(tv2.channel), "and volume level is", int(tv2.volume) )
