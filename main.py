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
btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5
btn7_pin = board.GP6
btn8_pin = board.GP7
btn9_pin = board.GP8
btn10_pin = board.GP9
btn11_pin = board.GP10
btn12_pin = board.GP11
btn13_pin = board.GP12
btn14_pin = board.GP13
btn15_pin = board.GP14
btn16_pin = board.GP15



btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN

btn15 = digitalio.DigitalInOut(btn15_pin)
btn15.direction = digitalio.Direction.INPUT
btn15.pull = digitalio.Pull.DOWN

btn16 = digitalio.DigitalInOut(btn16_pin)
btn16.direction = digitalio.Direction.INPUT
btn16.pull = digitalio.Pull.DOWN




keyboard = Keyboard(usb_hid.devices)
# below are the key values that you can change to
# fit your preferences. Change Keycode.ONE for example to
# (Keycode.CONTROL, Keycode.F4) for CTRL + F4
# on the first button.
# See the official CircuitPython docs
# for additional help
while True:
    #top row
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.F10)
        time.sleep(0.2)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.F12)
        time.sleep(0.2)
    if btn3.value:
        # keyboard.send(Keycode.THREE)
        time.sleep(0.2)
        
    if btn4.value:
        keyboard.send(Keycode.ENTER)
        time.sleep(0.2)

    #second row (arrow keys)
    if btn5.value:
        keyboard.send(Keycode.RIGHT)
        time.sleep(0.2)
    if btn6.value:
        keyboard.send(Keycode.LEFT)
        time.sleep(0.2)
    if btn7.value:
        keyboard.send(Keycode.UP)
        time.sleep(0.2)
    if btn8.value:
        keyboard.send(Keycode.DOWN)
        time.sleep(0.2)
        
        
    #THIRD ROW: 
    if btn9.value: #PASS
        keyboard.send(Keycode.P)
        time.sleep(0.2)
        
    if btn10.value: #FOUL
        keyboard.send(Keycode.F)
        time.sleep(0.2)
        
    if btn11.value: #N
        keyboard.send(Keycode.N)
        time.sleep(0.2)
        
    if btn12.value: #S
        keyboard.send(Keycode.S)
        time.sleep(0.1)
        
    #BOTTOM ROW FOR JUMPS (ALL POSSIBLE JUMPS) O, XO, XXO, XXX
    if btn13.value:
        keyboard.send(Keycode.O)
        time.sleep(0.2)
    if btn14.value:
        keyboard.send(Keycode.X)
        keyboard.send(Keycode.O)
        time.sleep(0.2)
    if btn15.value:
        keyboard.send(Keycode.X)
        keyboard.send(Keycode.X)
        keyboard.send(Keycode.O)
        time.sleep(0.2)
    if btn16.value:
        keyboard.send(Keycode.X)
        keyboard.send(Keycode.X)
        keyboard.send(Keycode.X)
        time.sleep(0.2)
        time.sleep(0.1)
    

