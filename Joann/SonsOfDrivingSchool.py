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
    square(12)
    gpg.turn_degrees(90)
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
        #gpg.turn_degrees(-90)

# Retrace
def retrace(distance):
    # Drive a right square based on the distance argument
    # Loop four times, Loop starts at 0,
    # Ends at 1 less than the last number
    # The loop increments 0, 1, 2, 3
    print("Make a Retrace")
    square(12)
    gpg.turn_degrees(-90)
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
        gpg.turn_degrees(-90)

# ForwardReverse
def forwardReverse(distance):
    # Drive forward then turn 180 degrees, move backwards
    # Loop two times, Loop starts at 0
    # Ends at 1 less than the last number
    # The loop increments 0, 1
    print("Make a Forward Reverse")
    for x in range(0, 2):
        # Print the loop counter
        print(x)
        gpg.drive_inches(distance, True)
        gpg.turn_degrees(180)
        gpg.drive_inches(-distance, True)
        gpg.turn_degrees(180)

#--------------------------------Stage 2------------------------------------

# Octagon
def octagon(distance):
    # Drive 12" octagon
    # Starts and end at the same place and orientation
    # Each turn is a 45 degrees angle
    # Loop eight times, loop starts at 0
    # The loop increments 0, 1, 2, 3, 4, 5, 6, 7
    print("Make an Octagon")
    for x in range(0, 8):
        # Print the loop counter
        print(x)
        gpg.drive_inches(distance, True)
        gpg.turn_degrees(45)

# Equilateral Triangle
def equilateralTriangle(distance):
    # Drive 12" equilateral triangle
    # Start and end in the same place and orientation
    print("Make an Equilateral Triangle")
    for x in range(0,3):
        # Print the loop counter
        print(x)
        gpg.drive_inches(distance, True)
        gpg.turn_degrees(120)

def main():
    """ Main Program Entry Point """
    # Drive a square turning left
    square(12)
    time.sleep(1)

    # Drive a rectangle turning left
    rectangle(12, 24)
    time.sleep(1)

    # Drive a square turning left, then turn around and return to the beginning point.
    sentry(12)
    time.sleep(1)

    # Drive a square forward, and then reverse to trace the same square backwards.
    retrace(12)
    time.sleep(1)

    # Drive forward, turn 180 degrees, move backwards
    forwardReverse(12)
    time.sleep(1)

    # Drive 12" octagon
    octagon(12)
    time.sleep(1)

    # Drive 12" equilateral triangle
    equilateralTriangle(12)



# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()

