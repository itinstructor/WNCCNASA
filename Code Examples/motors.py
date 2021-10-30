#!/usr/bin/env python3
#
# History
# ------------------------------------------------
# Author     Date      	    Comments
# Loring     09/12/21       Example of motor control with Python 3.5
#
# This code is an example for controlling the GoPiGo3 motors.
# EasyGoPiGo3 documentation: https://gopigo3.readthedocs.io/en/latest

import time                 # Import the time library for the sleep function
import easygopigo3 as easy  # Import the GoPiGo3 library
gpg = easy.EasyGoPiGo3()    # Initialize a EasyGoPiGo3 object
gpg.set_speed(200)          # Set initial speed
SLEEP_2_SECOND = 2
SLEEP_1_SECOND = 1


def main():

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

    print("Turn left 180 degrees")
    gpg.turn_degrees(-180)

    print("Turn right 180 degrees")
    gpg.turn_degrees(180)

    print("Orbiting right for 360 degrees")
    gpg.orbit(360, 20, True)

    print("Stop!")
    gpg.stop()
    print("Done!")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
