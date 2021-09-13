#!/usr/bin/env python3

import RPi.GPIO as gpio
import time

speed = 0.01

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(24, gpio.OUT)
p = gpio.PWM(18, 50)
p.start(50)
gpio.setup(23, gpio.OUT)

# gpio.output(18, gpio.HIGH)
# gpio.output(23, gpio.HIGH)

while True: # do this forever
    for i in range(0, 5):
        gpio.output(23, gpio.HIGH) # close the gate
        time.sleep(0.125) # wait for half a second
        gpio.output(23, gpio.LOW) # open the gate
        time.sleep(0.125) # wait for half a second

    for i in range(0, 5):
        gpio.output(24, gpio.HIGH) # close the gate
        time.sleep(0.5) # wait for half a second
        gpio.output(24, gpio.LOW) # open the gate
        time.sleep(0.5) # wait for half a second

    for i in range(0, 100):
        p.ChangeDutyCycle(100 - i)
        time.sleep(speed)

    for i in range(0, 100):
        p.ChangeDutyCycle(i)
        time.sleep(speed)