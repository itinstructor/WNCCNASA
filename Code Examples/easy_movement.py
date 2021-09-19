#!/usr/bin/env python3
'''
    Name: easy_movement.py
    Author: William A Loring
    Created: 09-18-21 Revised:
    Purpose: Demonstrate a sampling of GoPiGo dead reckoning movements
'''
# Import the time library for the sleep function
import time
# Import GoPiGo3 library
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class
# GPG is the GoPiGo3 object used to access methods and properties
gpg = EasyGoPiGo3()


#------------------- SQUARE RIGHT ------------------#
def square_right(distance):
    """ Drive a right square """
    # Loop four times
    # Loop starts at 0,
    # Ends at 1 less than the last number
    # The loop increments 0, 1, 2, 3
    print("Square Right")
    for x in range(0, 4):
        print(x)
        gpg.led_off("right")
        gpg.drive_inches(distance, True)
        gpg.led_on("right")
        gpg.turn_degrees(90)
    gpg.led_off("right")


#------------------- SQUARE LEFT ------------------#
def square_left(distance):
    """ Drive a left square """
    print("Square Left")
    for x in range(0, 4):
        print(x)
        gpg.led_off("left")
        gpg.drive_inches(distance, True)
        gpg.led_on("left")
        gpg.turn_degrees(-90)
    gpg.led_off("left")


#------------------- GOPIGO WAGGLE ------------------#
def waggle():
    """ Waggle back and forth """
    print("Waggle")
    for x in range(0, 4):
        print(x)
        gpg.led_on("left")
        gpg.turn_degrees(-10)
        gpg.led_off("left")
        gpg.led_on("right")
        gpg.turn_degrees(10)
        gpg.led_off("right")
    gpg.led_off("right")
    gpg.led_off("right")


def main():
    # Drive a square turning left
    square_left(5)

    # Turn left to reverse the square
    print("Turn Left 90")
    gpg.turn_degrees(-90)

    # Drive a square turning right
    square_right(5)

    print("Spin left.")
    gpg.spin_left()
    time.sleep(1)

    # Waggle back and forth
    waggle()

    print("Spin right.")
    gpg.spin_right()
    time.sleep(3)

    print("Stop!")
    gpg.stop()
    print("Done!")


main()
