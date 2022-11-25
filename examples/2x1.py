# Originally coded by Novaspirit Tech
# Copy this code into your code.py file.
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio
# These are the corresponding GPIOs on the Pi Pico
# that you soldered
btn1_pin = board.A3
btn2_pin = board.A2




btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN


keyboard = Keyboard(usb_hid.devices)
# below are the key values that you can change to
# fit your preferences. Change Keycode.ONE for example to
# (Keycode.CONTROL, Keycode.F4) for CTRL + F4
# on the first button.
# See the official CircuitPython docs
# for additional help
while True:
    if btn1.value:
        keyboard.send(Keycode.ONE)
        time.sleep(0.2)
    if btn2.value:
        keyboard.send(Keycode.TWO)
        time.sleep(0.2)
    

