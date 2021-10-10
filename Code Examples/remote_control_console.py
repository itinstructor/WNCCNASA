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
"""
This uses the EasyGoPiGo3 library located here.
https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html
"""
##############################################################################################################

import time                 # For sleep function to debounce the keys
import sys                  # For sys.exit
import easygopigo3 as easy  # Import the GoPiGo library
gpg = easy.EasyGoPiGo3()    # Create GoPiGo object
gpg.reset_all()
gpg.set_speed(200)

print("Console GoPiGo Robot control")
print("Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\nspace bar: Stop GoPiGo Robot\n\tz: Exit\n")
print("Speed: " + str(gpg.get_speed()))
while True:
    # Fetch the input from the terminal
    key_press = input("Enter the Command: ")
    # Forward
    if key_press == 'w':
        gpg.forward()
    # Turn Left
    elif key_press == 'a':
        gpg.left()
    # Turn Right
    elif key_press == 'd':
        gpg.right()
    # Backward
    elif key_press == 's':
        gpg.backward()
    # Stop when spacebar pressed
    elif key_press == ' ':
        gpg.stop()
    elif key_press == 'z':
        print("Exiting")		# Exit
        gpg.reset_all()
        sys.exit()
    else:
        print("Wrong Command, Please Enter Again")
    # Debounce the keys
    time.sleep(.1)
