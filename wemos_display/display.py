from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


class RossumDisplay:
    def __init__(self, sda, scl, resolution):
        i2c = I2C(scl=Pin(scl), sda=Pin(sda))
        width, height = resolution
        self.display = SSD1306_I2C(width, height, i2c)

    def show_text(self, text, x=0, y=0, width=1):
        self.display.fill(0)
        self.display.text(text, x, y, width)
        self.display.show()
