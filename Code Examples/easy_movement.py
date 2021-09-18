#!/usr/bin/env python3
'''
    Name: easy_simple_movement.py
    Author: William Loring
    Created: 09-18-21 Revised:
    Purpose: Demonstrate a sampling of GoPiGo dead reckoning movements
'''
# import the time library for the sleep function
import time
# import the GoPiGo3 drivers
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
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

    square_left(5)
    # Turn left to reverse the square
    print("Turn Left 90")
    gpg.turn_degrees(-90)
    square_right(5)

    print("Spin left.")
    gpg.spin_left()
    time.sleep(1)

    waggle()

    print("Spin right.")
    gpg.spin_right()
    time.sleep(2)

    print("Stop!")
    gpg.stop()
    print("Done!")

    # print("Drive the motors 5 inches and then stop.")
    # gpg.drive_inches(5, True)
    # time.sleep(1)

    # print("Turn right 1 second.")
    # gpg.right()
    # time.sleep(1)

    # print("Turn left 1 second.")
    # gpg.left()
    # time.sleep(1)

    # print("Turn left 90 degrees")
    # gpg.turn_degrees(-90)

    # print("Turn right 90 degrees")
    # gpg.turn_degrees(90)

    # print("Stop!")
    # gpg.stop()
    # print("Done!")


main()
