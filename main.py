from microbit import *
import neopixle
import music
from random import randint
rgb = neopixel.NeoPixel(pin1, 4)
 
class PIANO():
    def __init__(self):
        #The piano key corresponds to the touch screen value.
        self.Zero = 0x0000
        self.C    = 0x0001
        self.bD   = 0x0002
        self.D    = 0x0004
        self.bE   = 0x0008
        self.E    = 0x0010
        self.F    = 0x0020
        self.bG   = 0x0040
        self.G    = 0x0080
        self.bA   = 0x0100
        self.A    = 0x0200
        self.bB   = 0x0400
        self.B    = 0x0800
        self.C1   = 0x1000
        self.play = self.Zero
 
    def TouchPress(self):
        try:
            arr = i2c.read(0x57, 2)
            val = arr[0] + arr[1] * 256
        except OSError:
            val = 0xffff
        return val
 
    def ShowRGB(self,RGB):
        for rgb_id in range(0, 4):
            rgb[rgb_id] = (RGB[rgb_id][0], RGB[rgb_id][1], RGB[rgb_id][2])
            rgb.show()
 
    def Color(self):
        red   = randint(0, 30)
        green = randint(0, 30)
        blue  = randint(0, 30)
        for rgb_id in range(0, 4):
            rgb[rgb_id] = (red, green, blue)
        return rgb
 
    def PlayPiano(self):
        TPval = self.TouchPress()
        if TPval & self.play != 0:
            TPval = TPval & self.play
        elif TPval == self.C:
            self.ShowRGB(self.Color())
            music.pitch(262, wait=False)
        elif TPval == self.bD:
            self.ShowRGB(self.Color())
            music.pitch(277, wait=False)
        elif TPval == self.D:
            self.ShowRGB(self.Color())
            music.pitch(294, wait=False)
        elif TPval == self.bE:
            self.ShowRGB(self.Color())
            music.pitch(311, wait=False)
        elif TPval == self.E:
            self.ShowRGB(self.Color())
            music.pitch(330, wait=False)
        elif TPval == self.F:
            self.ShowRGB(self.Color())
            music.pitch(349, wait=False)
        elif TPval == self.bG:
            self.ShowRGB(self.Color())
            music.pitch(370, wait=False)
        elif TPval == self.G:
            self.ShowRGB(self.Color())
            music.pitch(392, wait=False)
        elif TPval == self.bA:
            self.ShowRGB(self.Color())
            music.pitch(415, wait=False)
        elif TPval == self.A:
            self.ShowRGB(self.Color())
            music.pitch(440, wait=False)
        elif TPval == self.bB:
            self.ShowRGB(self.Color())
            music.pitch(466, wait=False)
        elif TPval == self.B:
            self.ShowRGB(self.Color())
            music.pitch(494, wait=False)
        elif TPval == self.C1:
            self.ShowRGB(self.Color())
            music.pitch(523, wait=False)
        elif TPval == self.Zero:
            rgb.clear()
            music.stop()
        if TPval != 0xffff:
            self.play = TPval
 
Piano = PIANO()
while True:
    Piano.PlayPiano()
