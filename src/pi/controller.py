# Code for CamJam EduKit 3 robot
#
# By Mike Horne, based on code by Tom Oinn/Emma Norling code

# Need floating point division of integers
# Test
from __future__ import division

from time import sleep

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

try:
    # Attempt to import the GPIO Zero library. If this fails, because we're running somewhere
    # that doesn't have the library, we create dummy functions for set_speeds and stop_motors which
    # just print out what they'd have done. This is a fairly common way to deal with hardware that
    # may or may not exist!

    # Use GPIO Zero implementation of CamJam EduKit robot (thanks Ben Nuttall/Dave Jones!)
    from gpiozero import CamJamKitRobot

    print('GPIO Zero found')

    # Get the robot instance and the independent motor controllers
    robot = CamJamKitRobot()
    motor_left = robot.left_motor
    motor_right = robot.right_motor

    # Motors are reversed. If you find your robot going backwards, set this to 1
    motor_multiplier = -1


    def set_speeds(power_left, power_right):
        """
        As we have an motor hat, we can use the motors

        :param power_left:
            Power to send to left motor
        :param power_right:
            Power to send to right motor, will be inverted to reflect chassis layout
        """

        # If one wants to see the 'raw' 0-100 values coming in
        # print("source left: {}".format(power_left))
        # print("source right: {}".format(power_right))

        # Take the 0-100 inputs down to 0-1 and reverse them if necessary
        power_left = (motor_multiplier * power_left) / 100
        power_right = (motor_multiplier * power_right) / 100

        # Print the converted values out for debug
        # print("left: {}".format(power_left))
        # print("right: {}".format(power_right))

        # If power is less than 0, we want to turn the motor backwards, otherwise turn it forwards
        if power_left < 0:
            motor_left.backward(-power_left)
        else:
            motor_left.forward(power_left)

        if power_right < 0:
            motor_right.backward(-power_right)
        else:
            motor_right.forward(power_right)


    def stop_motors():
        """
        As we have an motor hat, stop the motors using their motors call
        """
        # Turn both motors off
        motor_left.stop()
        motor_right.stop()

except ImportError:

    print('GPIO Zero not found, using dummy functions.')


    def set_speeds(power_left, power_right):
        """
        No motor hat - print what we would have sent to it if we'd had one.
        """
        print('DEBUG Left: {}, Right: {}'.format(power_left, power_right))
        sleep(0.3)


    def stop_motors():
        """
        No motor hat, so just print a message.
        """
        print('DEBUG Motors stopping')

# All we need, as we don't care which controller we bind to, is the ControllerResource
from approxeng.input.selectbinder import ControllerResource


# Enable logging of debug messages, by default these aren't shown
# import logzero
# logzero.setup_logger(name='approxeng.input', level=logzero.logging.DEBUG)

class RobotStopException(Exception):
    """
    The simplest possible subclass of Exception, we'll raise this if we want to stop the robot
    for any reason. Creating a custom exception like this makes the code more readable later.
    """
    pass


def mixer(yaw, throttle, max_power=100):
    """
    Mix a pair of joystick axes, returning a pair of wheel speeds. This is where the mapping from
    joystick positions to wheel powers is defined, so any changes to how the robot drives should
    be made here, everything else is really just plumbing.

    :param yaw:
        Yaw axis value, ranges from -1.0 to 1.0
    :param throttle:
        Throttle axis value, ranges from -1.0 to 1.0
    :param max_power:
        Maximum speed that should be returned from the mixer, defaults to 100
    :return:
        A pair of power_left, power_right integer values to send to the motor driver
    """
    left = throttle + yaw
    right = throttle - yaw
    scale = float(max_power) / max(1, abs(left), abs(right))
    return int(left * scale), int(right * scale)


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

SPEED = 80
FREQ = 100
PWM_MIN = 0

p1 = gpio.PWM(13, FREQ)
p2 = gpio.PWM(16, FREQ)
p3 = gpio.PWM(23, FREQ)
p4 = gpio.PWM(24, FREQ)


def forwards():
    _set_motor_speed()

    gpio.output(5, gpio.HIGH)  # Set AIN1
    gpio.output(6, gpio.LOW)  # Set AIN2

    gpio.output(21, gpio.HIGH)  # Set BIN2
    gpio.output(20, gpio.LOW)  # Set BIN1

    gpio.output(17, gpio.HIGH)  # Set AIN1
    gpio.output(18, gpio.LOW)  # Set AIN2

    gpio.output(10, gpio.HIGH)  # Set BIN2
    gpio.output(22, gpio.LOW)  # Set BIN1

    _start_motors()


def backwards():
    _set_motor_speed()

    gpio.output(5, gpio.LOW)  # Set AIN1
    gpio.output(6, gpio.HIGH)  # Set AIN2

    gpio.output(21, gpio.LOW)  # Set BIN2
    gpio.output(20, gpio.HIGH)  # Set BIN1

    gpio.output(17, gpio.LOW)  # Set AIN1
    gpio.output(18, gpio.HIGH)  # Set AIN2

    gpio.output(10, gpio.LOW)  # Set BIN2
    gpio.output(22, gpio.HIGH)  # Set BIN1

    _start_motors()


def pivot_right():
    _set_motor_speed()

    gpio.output(5, gpio.LOW)  # Set AIN1
    gpio.output(6, gpio.HIGH)  # Set AIN2

    gpio.output(20, gpio.LOW)  # Set BIN1
    gpio.output(21, gpio.HIGH)  # Set BIN2

    gpio.output(17, gpio.LOW)  # Set AIN1
    gpio.output(18, gpio.HIGH)  # Set AIN2

    gpio.output(22, gpio.LOW)  # Set BIN1
    gpio.output(10, gpio.HIGH)  # Set BIN2

    _start_motors()


def pivot_left():
    _set_motor_speed()

    gpio.output(5, gpio.HIGH)  # Set AIN1
    gpio.output(6, gpio.LOW)  # Set AIN2

    gpio.output(20, gpio.HIGH)  # Set BIN1
    gpio.output(21, gpio.LOW)  # Set BIN2

    gpio.output(17, gpio.HIGH)  # Set AIN1
    gpio.output(18, gpio.LOW)  # Set AIN2

    gpio.output(22, gpio.HIGH)  # Set BIN1
    gpio.output(10, gpio.LOW)  # Set BIN2

    _start_motors()


def halt():
    gpio.output(5, gpio.LOW)  # Set AIN1
    gpio.output(6, gpio.LOW)  # Set AIN2
    gpio.output(13, gpio.LOW)  # Set PWMA

    gpio.output(17, gpio.LOW)  # Set AIN1
    gpio.output(18, gpio.LOW)  # Set AIN2
    gpio.output(23, gpio.LOW)  # Set PWMA

    gpio.output(20, gpio.LOW)  # Set BIN1
    gpio.output(21, gpio.LOW)  # Set BIN2
    gpio.output(16, gpio.LOW)  # Set PWMB

    gpio.output(22, gpio.LOW)  # Set BIN1
    gpio.output(10, gpio.LOW)  # Set BIN2
    gpio.output(24, gpio.LOW)  # Set PWMB

    _stop_motors()


def _set_motor_speed():
    p1.start(SPEED)
    p2.start(SPEED)
    p3.start(SPEED)
    p4.start(SPEED)


def _start_motors():
    gpio.output(13, gpio.HIGH)  # Set PWMA
    gpio.output(16, gpio.HIGH)  # Set PWMB
    gpio.output(23, gpio.HIGH)  # Set PWMA
    gpio.output(24, gpio.HIGH)  # Set PWMB


def _stop_motors():
    p1.stop(PWM_MIN)
    p2.stop(PWM_MIN)
    p3.stop(PWM_MIN)
    p4.stop(PWM_MIN)


# Outer try / except catches the RobotStopException we just defined, which we'll raise when we want to
# bail out of the loop cleanly, shutting the motors down. We can raise this in response to a button press
try:
    while True:
        # Inner try / except is used to wait for a controller to become available, at which point we
        # bind to it and enter a loop where we read axis values and send commands to the motors.
        try:
            # Bind to any available joystick, this will use whatever's connected as long as the library
            # supports it.
            with ControllerResource(dead_zone=0.1, hot_zone=0.2) as joystick:
                print('Controller found, press HOME button to exit, use left stick to drive.')
                print(joystick.controls)
                # Loop until the joystick disconnects, or we deliberately stop by raising a
                # RobotStopException
                while joystick.connected:
                    # Get joystick values from the left analogue stick
                    x_axis, y_axis = joystick['rx', 'ry']
                    # Get power from mixer function
                    power_left, power_right = mixer(yaw=x_axis, throttle=y_axis)
                    # Set motor speeds
                    set_speeds(power_left, power_right)
                    # Get a ButtonPresses object containing everything that was pressed since the last
                    # time around this loop.
                    joystick.check_presses()
                    # Print out any buttons that were pressed, if we had any

                    if y_axis > 0:
                        forwards()

                    if y_axis < 0:
                        backwards()

                    if power_left > 0 and y_axis == 0:
                        pivot_left()

                    if power_right > 0 and y_axis == 0:
                        pivot_right()

                    if x_axis == 0 and y_axis == 0:
                        halt()

                    if joystick.has_presses:
                        print(joystick.presses)

                    # If home was pressed, raise a RobotStopException to bail out of the loop
                    # Home is generally the PS button for playstation controllers, XBox for XBox etc
                    if 'home' in joystick.presses:
                        raise RobotStopException()
        except IOError:
            # We get an IOError when using the ControllerResource if we don't have a controller yet,
            # so in this case we just wait a second and try again after printing a message.
            print('No controller found yet')
            sleep(1)
except RobotStopException:
    # This exception will be raised when the home button is pressed, at which point we should
    # stop the motors.
    stop_motors()