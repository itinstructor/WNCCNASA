#!/usr/bin/env python
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is an example for reading the GoPiGo3 Motors' encoders
#
# Results:  When you run this program, the GoPiGo3 Motors' position will be printed.

# use python 3 syntax but make it compatible with python 2
from __future__ import print_function
from __future__ import division  # ''

import time     # import the time library for the sleep function
import gopigo3  # import the GoPiGo3 drivers

# Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.
GPG = gopigo3.GoPiGo3()

try:
    # Get the left and right motor position
    GPG.offset_motor_encoder(
        GPG.MOTOR_LEFT,
        GPG.get_motor_encoder(GPG.MOTOR_LEFT)
    )
    GPG.offset_motor_encoder(
        GPG.MOTOR_RIGHT,
        GPG.get_motor_encoder(GPG.MOTOR_RIGHT)
    )
    while True:
        # Print the position of the encoder
        print("Encoder L: %6d  R: %6d" % (
            GPG.get_motor_encoder(GPG.MOTOR_LEFT),
            GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
        )
        time.sleep(0.025)

# except the program gets interrupted by Ctrl+C on the keyboard.
except KeyboardInterrupt:
    # Unconfigure the sensors, disable the motors, and restore the LED to the control of the GoPiGo3 firmware.
    GPG.reset_all()
