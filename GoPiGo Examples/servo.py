#!/usr/bin/env python3
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# This uses the EasyGoPiGo3 library.
# You can find more information on the library here:
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3
#
# This code is an example for controlling the GoPiGo3 Servos
#
# Results:  When you run this program, the GoPiGo3 Servos will rotate back and forth.


import time     # import the time library for the sleep function
import easygopigo3 as easy  # import the GoPiGo3 drivers

# Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.
gpg = easy.EasyGoPiGo3()

# Initialize a servo object on Servo Port 1
servo = gpg.init_servo("SERVO1")

# Set servo pointing straight ahead at 90 degrees
# The degrees have been changed to adapt to this servo
# All servos line up slightly differently

# Forward
servo.rotate_servo(85)
time.sleep(1)

# Right
servo.rotate_servo(20)
time.sleep(1)

# Left
servo.rotate_servo(155)
time.sleep(1)

# Forward
servo.rotate_servo(85)
time.sleep(1)

# Disable or "float" the servo
servo.disable_servo()

# Unconfigure the sensors, disable the motors
# and restore the LED to the control of the GoPiGo3 firmware
gpg.reset_all()


