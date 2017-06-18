#!/usr/bin/env python3
from tkinter import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def turn_on():
        print ("powering up amplifier...")
        GPIO.output(7, True)
        time.sleep(.1)
        GPIO.output(11, True)
        time.sleep(5)
        GPIO.output(11, False)
        time.sleep(.1)
        GPIO.output(7, False)
        print ("amp off...")
def gpio_cleanup():
        GPIO.cleanup()
def laser_on():
        print ("powering laser and VCO...")
        GPIO.output(13, False)
def laser_off():
        GPIO.output(13, True)
        print ("laser and VCO off...")

root = Tk()

button = Button(root, text="Turn off laser", command=laser_off)
button.pack(side=RIGHT, padx=10, pady=10, ipadx=10, ipady=10)

button2= Button(root, text="POWER UP 5s", command=turn_on)
button2.pack(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)

button3= Button(root, text="GPIO Cleanup Before Quit", command=gpio_cleanup)
button3.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)

button4= Button(root, text="Turn on laser", command=laser_on)
button4.pack(side=BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)

#labelText = StringVar()
#labelText.set("IT'S ON!")
#label1 = Label(root, textvariable=labelText, height=4)
#label1.pack(side=LEFT)

root.title("EMPower Tech. Inc.")
root.geometry('500x300+200+200')

root.mainloop()
