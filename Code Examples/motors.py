#!/usr/bin/env python3
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license
# (http://choosealicense.com/licenses/mit/).
#
# For more information see
# https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is an example for controlling the GoPiGo3 motors.
# This uses the EasyGoPiGo3 library see
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3
#

import time                 # Import the time library for the sleep function
import easygopigo3 as easy  # Import the GoPiGo3 library

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = easy.EasyGoPiGo3()
# Reset GoPiGo to hardware defaults
gpg.reset_all()
gpg.set_speed(200)


def main():
    SLEEP_2_SECOND = 2
    SLEEP_1_SECOND = 1

    # Print the current speed
    print(str(gpg.get_speed()))
    time.sleep(SLEEP_1_SECOND)

    print("Move the motors forward freely for 2 second.")
    gpg.forward()
    time.sleep(SLEEP_2_SECOND)
    # Stop both motors
    gpg.stop()

    print("Stop the motors for 1 second.")
    time.sleep(SLEEP_2_SECOND)

    print("Drive the motors 12 inches and then stop.")
    gpg.drive_inches(12, True)
    time.sleep(SLEEP_2_SECOND)

    print("Turn right 1 second.")
    gpg.right()
    time.sleep(SLEEP_1_SECOND)

    print("Turn left 1 second.")
    gpg.left()
    time.sleep(SLEEP_1_SECOND)

    print("Spin left.")
    gpg.spin_left()
    time.sleep(SLEEP_2_SECOND)

    print("Spin right.")
    gpg.spin_right()
    time.sleep(SLEEP_2_SECOND)

    print("Turn left 90 degrees")
    gpg.turn_degrees(-180)

    print("Turn right 90 degrees")
    gpg.turn_degrees(180)

    print("Stop!")
    gpg.stop()
    print("Done!")


main()
