"""
    Name: sons_of_driving_school.py
    Author:
    Created: 10-19-2021
    Purpose: 
"""
# Import the time library for the sleep function
import time
# Import GoPiGo3 library
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class
# GPG is the GoPiGo3 object used to access methods and properties
gpg = EasyGoPiGo3()

#-------------------------Stage 1--------------------------------#
# Square
def square(distance):
    # Drive a right square based on the distance argument
    # Loop four times, Loop starts at 0,
    # Ends at 1 less than the last number
    # The loop increments 0, 1, 2, 3
    print("Make a square")
    for x in range(0, 4):
        # Print the loop counter
        print(x)
        gpg.led_off("right")
        gpg.drive_inches(
            distance,       # How far to drive in inches
            True            # Blocking, nothing else can happen while moving
        )
        gpg.led_on("right")
        # Turn right 90 degrees, positive number is right
        gpg.turn_degrees(90)
    # Turn both blinkers off
    gpg.led_off("right")
    gpg.led_off("left")


# Rectangle
def rectangle(distance1, distance2):
    # Drive a right rectangle based on the distance argument
    # Loop two times, Loop starts at 0,
    # Ends at 1 less than the last number
    # The loop increments 0, 1
    print("Make a rectangle")
    for x in range(0, 2):
        # Print the loop counter
        print(x)
        gpg.led_off("right")
        gpg.drive_inches(
            distance1,       # How far to drive in inches
            True            # Blocking, nothing else can happen while moving
        )
        gpg.led_on("right")
        # Turn right 90 degrees, positive number is right
        gpg.turn_degrees(90)

        gpg.led_off("right")
        gpg.drive_inches(
            distance2,       # How far to drive in inches
            True            # Blocking, nothing else can happen while moving
        )
        gpg.led_on("right")
        # Turn right 90 degrees, positive number is right
        gpg.turn_degrees(90)

    # Turn both blinkers off
    gpg.led_off("right")
    gpg.led_off("left")

# Sentry
def sentry(distance):
    # Drive a right square based on the distance argument
    # Loop four times, Loop starts at 0,
    # Ends at 1 less than the last number
    # The loop increments 0, 1, 2, 3
    print("Make a Sentry")
    for x in range(0, 4):
        # Print the loop counter
        print(x)
        gpg.led_off("right")
        gpg.drive_inches(
            distance,       # How far to drive in inches
            True            # Blocking, nothing else can happen while moving
        )
        gpg.led_on("right")
        # Turn right 90 degrees, positive number is right
        gpg.turn_degrees(90)

    for x in range(0, 4):
        # Print the loop counter
        print(x)
        gpg.led_off("right")
        gpg.drive_inches(
            -distance,       # How far to drive in inches
            True            # Blocking, nothing else can happen while moving
        )
        gpg.led_on("right")
        # Turn right 90 degrees, positive number is right
        gpg.turn_degrees(90)
    # Turn both blinkers off
    gpg.led_off("right")
    gpg.led_off("left")



def main():
    """ Main Program Entry Point """
    # Drive a square turning left
    square(12)

    # Drive a rectangle turning left
    rectangle(12, 24)

    # Drive a square turning left and drive backwards to the starting point
    sentry(12)



# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()

