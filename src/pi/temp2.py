#!/usr/bin/env python

import time
import RPi.GPIO as GPIO


def init():
    GPIO.setmode(GPIO.BCM)
    _setup_pins()
    _setup_pwm()


def _setup_pins():
    GPIO.setup(13, GPIO.OUT)  # Connected to PWMA
    GPIO.setup(5, GPIO.OUT)  # Connected to AIN1
    GPIO.setup(6, GPIO.OUT)  # Connected to AIN2

    GPIO.setup(16, GPIO.OUT)  # Connected to PWMB
    GPIO.setup(20, GPIO.OUT)  # Connected to BIN1
    GPIO.setup(21, GPIO.OUT)  # Connected to BIN2

    GPIO.setup(23, GPIO.OUT)  # Connected to PWMA
    GPIO.setup(17, GPIO.OUT)  # Connected to AIN1
    GPIO.setup(18, GPIO.OUT)  # Connected to AIN2

    GPIO.setup(24, GPIO.OUT)  # Connected to PWMB
    GPIO.setup(22, GPIO.OUT)  # Connected to BIN1
    GPIO.setup(10, GPIO.OUT)  # Connected to BIN2


def _setup_pwm():
    p1 = GPIO.PWM(13, 50)
    p1.start(60)

    p2 = GPIO.PWM(16, 50)
    p2.start(60)

    p3 = GPIO.PWM(23, 50)
    p3.start(60)

    p4 = GPIO.PWM(24, 50)
    p4.start(60)


def setup_to_go_pivot():
    GPIO.output(5, GPIO.LOW) # Set AIN1
    GPIO.output(6, GPIO.HIGH) # Set AIN2

    GPIO.output(20, GPIO.LOW) # Set BIN1
    GPIO.output(21, GPIO.HIGH) # Set BIN2

    GPIO.output(17, GPIO.LOW) # Set AIN1
    GPIO.output(18, GPIO.HIGH) # Set AIN2

    GPIO.output(22, GPIO.LOW) # Set BIN1
    GPIO.output(10, GPIO.HIGH) # Set BIN2


def setup_to_go_forward():
    GPIO.output(5, GPIO.LOW) # Set AIN1
    GPIO.output(6, GPIO.HIGH) # Set AIN2
    GPIO.output(20, GPIO.HIGH) # Set BIN1
    GPIO.output(21, GPIO.LOW) # Set BIN2

    GPIO.output(17, GPIO.LOW) # Set AIN1
    GPIO.output(18, GPIO.HIGH) # Set AIN2
    GPIO.output(22, GPIO.HIGH) # Set BIN1
    GPIO.output(10, GPIO.LOW) # Set BIN2


def enable_motors():
    GPIO.output(13, GPIO.HIGH) # Set PWMA
    GPIO.output(16, GPIO.HIGH) # Set PWMB
    GPIO.output(23, GPIO.HIGH) # Set PWMA
    GPIO.output(24, GPIO.HIGH) # Set PWMB


def cleanup():
    GPIO.output(5, GPIO.LOW)  # Set AIN1
    GPIO.output(6, GPIO.LOW)  # Set AIN2
    GPIO.output(13, GPIO.LOW)  # Set PWMA

    GPIO.output(17, GPIO.LOW)  # Set AIN1
    GPIO.output(18, GPIO.LOW)  # Set AIN2
    GPIO.output(23, GPIO.LOW)  # Set PWMA

    GPIO.output(20, GPIO.LOW)  # Set BIN1
    GPIO.output(21, GPIO.LOW)  # Set BIN2
    GPIO.output(16, GPIO.LOW)  # Set PWMB

    GPIO.output(22, GPIO.LOW)  # Set BIN1
    GPIO.output(10, GPIO.LOW)  # Set BIN2
    GPIO.output(24, GPIO.LOW)  # Set PWMB


def run():
    init()
    setup_to_go_forward()
    enable_motors()
    time.sleep(1)
    cleanup()


run()

