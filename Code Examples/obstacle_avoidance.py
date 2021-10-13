#!/usr/bin/env python3
# This uses the EasyGoPiGo3 library
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3
#
########################################################################
# This example demonstrates using the distance sensor with the GoPiGo
# In this examples, the GoPiGo keeps reading from the distance sensor
# When it close to the an obstacle, it stops.
#
# http://www.dexterindustries.com/GoPiGo/
# History
# ------------------------------------------------
# Author     Date      		Comments
# Karan      21 Aug 14 		Initial Authoring
# Loring	 10/12/21		Convert to EasyGoPiGo, test with Python 3.5
#
########################################################################
#
# ! Attach Distance sensor to Ic2 Port.
#
########################################################################
import time                             # Import the time library for the sleep function
import easygopigo3 as easy              # Import the GoPiGo3 library
gpg = easy.EasyGoPiGo3(use_mutex=True)  # Create a EasyGoPiGo3 object
distance_sensor = gpg.init_distance_sensor()
# Initialize a servo object on Servo Port 1
servo = gpg.init_servo("SERVO1")

# Set servo pointing straight ahead at 90 degrees
# You may have to change the degrees to adapt to your servo
# All servos line up slightly differently
# Less than 90 moves the servo to the right
# Greater than 90 moves the servo to the left
servo.rotate_servo(90)

gpg.set_speed(200)						# Set initial speed

distance_to_stop = 12  # Distance in inches from obstacle where the GoPiGo should stop
print("Press ENTER to start")
input()        # Wait for input to start
gpg.forward()  # Start moving

loop = True    # Boolean to control the while loop

while loop:
    dist = distance_sensor.read_inches()  # Find the distance of the object in front
    print("Dist:", dist, 'inches')        # Print feedback to the console
    if dist < distance_to_stop:  # If the object is closer than the "distance_to_stop" distance, stop the GoPiGo
        print("Stopping")
        gpg.stop()          # Stop the GoPiGo
        loop = False        # Set loop to false to break out of the loop, end the program

    # sleep is only needed to see the measurements
    # sleep is blocking code, nothing else can happen during sleep
    time.sleep(.05)
