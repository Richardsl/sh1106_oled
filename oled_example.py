import board
import busio
import time

# Initialize I2C bus.
i2c = busio.I2C(board.IO22, board.IO21)

# 1.3" monochrome OLED 128x64, adr 0x3C or 0x3D
import sh1106_oled
display = sh1106_oled.SH1106_I2C(128, 64, i2c, addr=0x3c, external_vcc=True)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

# Set a pixel in the origin 1,1 position as 0,0 is off the edge of the display and not visible.
display.pixel(1, 1, 1)
# Set a pixel in the middle 64,32 position.
display.pixel(64, 32, 1)
# Set a pixel in the opposite 125,63 position 127,63 is off the edge of the display and not visible.
display.pixel(125, 63, 1)

display.show()

while True:
    time.sleep(1)