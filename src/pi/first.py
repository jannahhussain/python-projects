#!/usr/bin/env python

import time
import RPi.GPIO as gpio


# Declare the GPIO settings
gpio.setmode(gpio.BCM)


def run():

    def _pivot_left():
        gpio.output(5, gpio.LOW)  # Set AIN1
        gpio.output(6, gpio.HIGH)  # Set AIN2

        gpio.output(20, gpio.LOW)  # Set BIN1
        gpio.output(21, gpio.HIGH)  # Set BIN2

        gpio.output(17, gpio.LOW)  # Set AIN1
        gpio.output(18, gpio.HIGH)  # Set AIN2

        gpio.output(22, gpio.LOW)  # Set BIN1
        gpio.output(10, gpio.HIGH)  # Set BIN2
        # Set the motor speed
        gpio.output(13, gpio.HIGH)  # Set PWMA
        gpio.output(16, gpio.HIGH)  # Set PWMB
        gpio.output(23, gpio.HIGH)  # Set PWMA
        gpio.output(24, gpio.HIGH)  # Set PWMB
        time.sleep(2)

        # ----- STOP -------------------------
        gpio.output(13, gpio.LOW)  # Set PWMA
        gpio.output(16, gpio.LOW)  # Set PWMB
        gpio.output(23, gpio.LOW)  # Set PWMA
        gpio.output(24, gpio.LOW)  # Set PWMB

    def _forwards():
        gpio.output(5, gpio.HIGH) # Set AIN1
        gpio.output(6, gpio.LOW) # Set AIN2

        gpio.output(21, gpio.HIGH) # Set BIN2
        gpio.output(20, gpio.LOW) # Set BIN1

        gpio.output(17, gpio.HIGH) # Set AIN1
        gpio.output(18, gpio.LOW) # Set AIN2

        gpio.output(10, gpio.HIGH) # Set BIN2
        gpio.output(22, gpio.LOW) # Set BIN1
        # Set the motor speed
        gpio.output(13, gpio.HIGH) # Set PWMA
        gpio.output(16, gpio.HIGH) # Set PWMB
        gpio.output(23, gpio.HIGH) # Set PWMA
        gpio.output(24, gpio.HIGH) # Set PWMB
        time.sleep(2)

        # ----- STOP -------------------------
        gpio.output(13, gpio.LOW) # Set PWMA
        gpio.output(16, gpio.LOW) # Set PWMB
        gpio.output(23, gpio.LOW) # Set PWMA
        gpio.output(24, gpio.LOW) # Set PWMB
        # ------------------------------------

    def _backwards():

        gpio.output(5, gpio.LOW) # Set AIN1
        gpio.output(6, gpio.HIGH) # Set AIN2

        gpio.output(21, gpio.LOW) # Set BIN2
        gpio.output(20, gpio.HIGH) # Set BIN1

        gpio.output(17, gpio.LOW) # Set AIN1
        gpio.output(18, gpio.HIGH) # Set AIN2

        gpio.output(10, gpio.LOW) # Set BIN2
        gpio.output(22, gpio.HIGH) # Set BIN1
        # Set the motor speed
        gpio.output(13, gpio.HIGH) # Set PWMA
        gpio.output(16, gpio.HIGH) # Set PWMB
        gpio.output(23, gpio.HIGH) # Set PWMA
        gpio.output(24, gpio.HIGH) # Set PWMB
        time.sleep(2)

        # ----- STOP -------------------------
        gpio.output(13, gpio.LOW) # Set PWMA
        gpio.output(16, gpio.LOW) # Set PWMB
        gpio.output(23, gpio.LOW) # Set PWMA
        gpio.output(24, gpio.LOW) # Set PWMB
        # ------------------------------------

    def _pivot_right():
        gpio.output(5, gpio.HIGH) # Set AIN1
        gpio.output(6, gpio.LOW) # Set AIN2

        gpio.output(20, gpio.HIGH) # Set BIN1
        gpio.output(21, gpio.LOW) # Set BIN2

        gpio.output(17, gpio.HIGH) # Set AIN1
        gpio.output(18, gpio.LOW) # Set AIN2

        gpio.output(22, gpio.HIGH) # Set BIN1
        gpio.output(10, gpio.LOW) # Set BIN2
        # Set the motor speed
        gpio.output(13, gpio.HIGH) # Set PWMA
        gpio.output(16, gpio.HIGH) # Set PWMB
        gpio.output(23, gpio.HIGH) # Set PWMA
        gpio.output(24, gpio.HIGH) # Set PWMB
        time.sleep(2)

    def _clean_up():
        gpio.output(5, gpio.LOW) # Set AIN1
        gpio.output(6, gpio.LOW) # Set AIN2
        gpio.output(13, gpio.LOW) # Set PWMA

        gpio.output(17, gpio.LOW) # Set AIN1
        gpio.output(18, gpio.LOW) # Set AIN2
        gpio.output(23, gpio.LOW) # Set PWMA

        gpio.output(20, gpio.LOW) # Set BIN1
        gpio.output(21, gpio.LOW) # Set BIN2
        gpio.output(16, gpio.LOW) # Set PWMB

        gpio.output(22, gpio.LOW) # Set BIN1
        gpio.output(10, gpio.LOW) # Set BIN2
        gpio.output(24, gpio.LOW) # Set PWMB

    # ---------------setup pins ----------------------
    gpio.setup(13, gpio.OUT)  # Connected to PWMA
    gpio.setup(16, gpio.OUT)  # Connected to PWMB

    gpio.setup(23, gpio.OUT)  # Connected to PWMA
    gpio.setup(24, gpio.OUT)  # Connected to PWMB
    #
    gpio.setup(5, gpio.OUT)  # Connected to AIN1
    gpio.setup(6, gpio.OUT)  # Connected to AIN2
    gpio.setup(20, gpio.OUT)  # Connected to BIN1
    gpio.setup(21, gpio.OUT)  # Connected to BIN2
    #
    gpio.setup(17, gpio.OUT)  # Connected to AIN1
    gpio.setup(18, gpio.OUT)  # Connected to AIN2
    gpio.setup(22, gpio.OUT)  # Connected to BIN1
    gpio.setup(10, gpio.OUT)  # Connected to BIN2

    # -------------------set up pwm ----------------

    p1 = gpio.PWM(13, 50)
    p1.start(80)
    p2 = gpio.PWM(16, 50)
    p2.start(80)

    p3 = gpio.PWM(23, 50)
    p3.start(80)
    p4 = gpio.PWM(24, 50)
    p4.start(80)

    # --------------------------------------------

    _pivot_right()
    _forwards()
    _backwards()
    _pivot_left()
    _clean_up()


run()


