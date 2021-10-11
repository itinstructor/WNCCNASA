#!/usr/bin/env python3
#############################################################################################################
# Basic example for controlling the GoPiGo using the Keyboard
# Controls:
# 	w:	Move forward
#	a:	Turn left
#	d:	Turn right
#	s:	Move back
#	x:	Stop
#	t:	Increase speed
#	g:	Decrease speed
#	z: 	Exit
# http://www.dexterindustries.com/GoPiGo/
# History
# ------------------------------------------------
# Author          Date      	    Comments
# Karan	    	  27 June 14		Code cleanup
# William Loring  10/10/21		Convert to Python3
# This uses the EasyGoPiGo3 library
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html
##############################################################################################################

import time                 # For sleep function to debounce the keys
import sys                  # For sys.exit
import easygopigo3 as easy  # Import the GoPiGo library
gpg = easy.EasyGoPiGo3()    # Create GoPiGo object

# Set initial speed
gpg.set_speed(200)

# Create an instance/object of the Distance Sensor class.
# I2C1 and I2C2 are just labels used for identifying the port on the GoPiGo3 board.
# But technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
my_distance_sensor = gpg.init_distance_sensor()

print("Console GoPiGo Robot control")
print("Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\nspace bar: Stop GoPiGo Robot\n\tz: Exit\n")
print("Speed: " + str(gpg.get_speed()))
while True:

    # Read the sensor into variables
    #mm = str(my_distance_sensor.read_mm())
    inches = str(my_distance_sensor.read_inches())
    distanceInches = float(inches)

    # Print the values of the sensor to the console
    print("Distance Sensor Reading: " + format(distanceInches) + " inches ")

    # Fetch the input from the terminal
    key_press = input("Enter the Command: ")
    # Forward
    if key_press == 'w':
        gpg.forward()

        # Decision 
        if distanceInches <= 10:
            print("You're too close!")
            gpg.stop()
            gpg.turn_degrees(90)
            gpg.forward()
        else:
            print("Keep on moving!")
            gpg.forward() 

    # Turn Left
    elif key_press == 'a':
        gpg.left()

        # Decision 
        if distanceInches <= 10:
            print("You're too close!")
            gpg.stop()
            gpg.turn_degrees(90)
            gpg.forward()
        else:
            print("Keep on moving!")
            gpg.forward() 

    # Turn Right
    elif key_press == 'd':
        gpg.right()

        # Decision 
        if distanceInches <= 10:
            print("You're too close!")
            gpg.stop()
            gpg.turn_degrees(90)
            gpg.forward()
        else:
            print("Keep on moving!")
            gpg.forward() 

    # Backward
    elif key_press == 's':
        gpg.backward()

        # Decision 
        if distanceInches <= 10:
            print("You're too close!")
            gpg.stop()
            gpg.turn_degrees(90)
            gpg.forward()
        else:
            print("Keep on moving!")
            gpg.forward() 

    # Stop when spacebar pressed
    elif key_press == ' ':
        gpg.stop()
            
    # Exit program
    elif key_press == 'z':
        print("Exiting")
        sys.exit()
    else:
        print("Unknown Command, Please Enter Again")
    # Debounce the keys
    time.sleep(.1)
