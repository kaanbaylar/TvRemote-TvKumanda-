class TVRemote:
    def __init__(self):
        self.power = False
        self.volume = 50
        self.channel = 1

    def power_button(self):
        if self.power:
            self.power = False
            print("TV turned off")
        else:
            self.power = True
            print("TV turned on")

    def volume_up(self):
        if self.power:
            if self.volume < 100:
                self.volume += 1
                print("Volume increased to", self.volume)
            else:
                print("Volume already at maximum")
        else:
            print("Turn on the TV first")

    def volume_down(self):
        if self.power:
            if self.volume > 0:
                self.volume -= 1
                print("Volume decreased to", self.volume)
            else:
                print("Volume already at minimum")
        else:
            print("Turn on the TV first")

    def channel_up(self):
        if self.power:
            self.channel += 1
            print("Channel changed to", self.channel)
        else:
            print("Turn on the TV first")

    def channel_down(self):
        if self.power:
            if self.channel > 1:
                self.channel -= 1
                print("Channel changed to", self.channel)
            else:
                print("Already on the first channel")
        else:
            print("Turn on the TV first")

    def number_button(self, number):
        if self.power:
            print("Pressed number", number)
        else:
            print("Turn on the TV first")

    def up_button(self):
        if self.power:
            print("Up button pressed")
        else:
            print("Turn on the TV first")

    def down_button(self):
        if self.power:
            print("Down button pressed")
        else:
            print("Turn on the TV first")

    def left_button(self):
        if self.power:
            print("Left button pressed")
        else:
            print("Turn on the TV first")

    def right_button(self):
        if self.power:
            print("Right button pressed")
        else:
            print("Turn on the TV first")

    def center_button(self):
        if self.power:
            print("Center button pressed")
        else:
            print("Turn on the TV first")

    def list_button(self):
        if self.power:
            print("List button pressed")
        else:
            print("Turn on the TV first")

    def settings_button(self):
        if self.power:
            print("Settings
    def settings_button(self):
        if self.power:
            print("Settings button pressed.")
        # Burada ayarlar menüsünü açmak için gerekli kodları yazabilirsiniz
        else:
            print("Device is not powered on. Press power button first.")
