#!/usr/bin/env python3
from tkinter import *
import time
import RPi.GPIO as GPIO

# setup IO pins here, you will have to search for your specific boards GPIO pinout diagrams to find out the numbering system
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def turn_on():
        print ("turning on GPIO ")
        GPIO.output(7, True)
# using the speep function as a delay, default unit here is in seconds
        time.sleep(.1)
        GPIO.output(11, True)
        time.sleep(5)
        GPIO.output(11, False)
        time.sleep(.1)
        GPIO.output(7, False)
        print ("turning off...")
def gpio_cleanup():
        GPIO.cleanup()
def laser_off():
        print ("power down")
        GPIO.output(13, False)
def laser_on():
        GPIO.output(13, True)
        print ("power on")

root = Tk()

button = Button(root, text="Turn off laser", command=laser_off)
button.pack(side=RIGHT, padx=10, pady=10, ipadx=10, ipady=10)

button2= Button(root, text="POWER UP 5s", command=turn_on)
button2.pack(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)

button3= Button(root, text="GPIO Cleanup Before Quit", command=gpio_cleanup)
button3.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)

button4= Button(root, text="Turn on laser", command=laser_on)
button4.pack(side=BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)

root.title("Raspberry PI GPIO Example")
root.geometry('500x300+200+200')

root.mainloop()
