'''Micropython ILI9341 with xpt2046 touch screen demo for CYD
    libraries and boilerplate altered from @rdagger ili9341 repo
    https://raw.githubusercontent.com/rdagger/micropython-ili9341
'''

from ili9341 import Display, color565
from xpt2046 import Touch
from machine import idle, Pin, SPI


class Demo(object):
    '''Touchscreen simple demo.'''
    CYAN = color565(0, 255, 255)
    PURPLE = color565(255, 0, 255)
    WHITE = color565(255, 255, 255)

    def __init__(self, display, spi2):
        '''Initialize box.

        Args:
            display (ILI9341): display object
            spi2 (SPI): SPI bus
        '''
        self.display = display
        self.touch = Touch(spi2, cs=Pin(33), int_pin=Pin(36),
                           int_handler=self.touchscreen_press)
        # Display initial message
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "TOUCH ME",
                                  self.WHITE,
                                  background=self.PURPLE)

        # A small 5x5 sprite for the dot
        self.dot = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

    def touchscreen_press(self, x, y):
        '''Process touchscreen press events.'''
        print("Display touched.")
        
        # Y needs to be flipped
        y = (self.display.height - 1) - y
        # Display coordinates
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "{0:03d}, {1:03d}".format(x, y),
                                  self.CYAN)
        # Draw dot
        self.display.draw_sprite(self.dot, x - 2, y - 2, 5, 5)


def test():
    
    '''
    Display Pins:
    IO2 	TFT_RS 	AKA: TFT_DC
    IO12 	TFT_SDO 	AKA: TFT_MISO
    IO13 	TFT_SDI 	AKA: TFT_MOSI
    IO14 	TFT_SCK 	
    IO15 	TFT_CS 	
    IO21 	TFT_BL

    Touch Screen Pins:
    IO25 	XPT2046_CLK 	
    IO32 	XPT2046_MOSI 	
    IO33 	XPT2046_CS 	
    IO36 	XPT2046_IRQ 	
    IO39 	XPT2046_MISO
    '''
    
    
    ''' Set up the display - ili9341
        Baud rate of 40000000 seems about the max '''
    spi1 = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))
    display = Display(spi1, dc=Pin(2), cs=Pin(15), rst=Pin(0))
    
    
    bl_pin = Pin(21, Pin.OUT)
    bl_pin.on()
    
    # Set up the touch screen digitizer - xpt2046
    spi2 = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))

    Demo(display, spi2)

    try:
        while True:
            idle()

    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        display.cleanup()


test()