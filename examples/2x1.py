
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

# pin defenitions
btn1_pin = board.A3 
btn2_pin = board.A2



#key configuration
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

#initialize keyboard object
keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.send(Keycode.ONE) #input 1
        time.sleep(0.2) #wait for 0.2 seconds before listening for another keypress
    if btn2.value:
        keyboard.send(Keycode.TWO)
        time.sleep(0.2)
    

