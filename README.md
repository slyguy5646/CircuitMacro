# MacroPad

### A collection of RP2040/Circuit Python based macropad code
#### The `examples` directory (example macropad configurations): 
 - 4x4.py: 4x4 pad
 - 2x1.py: 2x1 pad

#### The `KeycodeValues.md` file:
 - A guide to almost all possible keymappings for your reference

### The `adafruit_hid` directory:
 - A CircuitPython library that is used by this guide

## Setup Guide

### Configuration:
 - #### This guide assumes you already have CircuitPython setup on your board and you're hardware is setup. It also assumes you have an editor to write CircuitPython.
   -  If you don't have any hardware yet, a great sample tutorial can be found [here](https://www.hackster.io/1NextPCB/how-to-build-a-pico-macro-pad-3638e6) (You don't *have* to follow this guide exactly but it is a good starting point in terms of hardware if you don't have an idea of where to start). 
  
   -  If you don't have CircuitPython setup yet, a great guide can be found [here](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
  
    -  If you have an editor like VS Code that will work fine. I personally recommend Thonny because you can execute code on and interact with your board right from the editor. A download and setup tutorial is available [here](https://www.youtube.com/watch?v=_ouzuI_ZPLs&ab_channel=CoreElectronics) (you can skip to about the 0:40 mark to get to the tutorial). This guide uses MicroPython but make sure you select CircuitPython as the interpreter for this guide to work.
  
### Software Setup:
1.  Grab the `adafruit_hid` folder from this repository or from the official CircuitPython Libraries Bundle which includes all of the current CircuitPython libraries(You can download it [here](https://circuitpython.org/libraries)).
   
2.  Next put the library on your RP2040 or CircuitPython board by copying it to the under the `lib` directory on your board.

3. Next, start coding! You can take a look at an example  file from the `examples` directory to see what some MacroPad software might look like. When you are ready to write code for your own macro pad, you can grab the `template.py` file. This file sets up and configures 16 keys (this is tedious and `template.py` will save you some time). From their, you can check out the `KeycodeValues.md` file for a detailed explanation on what each `Keycode` value does.
   
4.  Add your finished CircuitPython file to the root directory of your RP2040 or CircuitPython board and rename it to `main.py` or `code.py` (the name depends on the board so you may have to experiment) so that the MacroPad will work as soon as it is plugged in and you won't have to run the your script everytime.
