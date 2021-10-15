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


#--------------------------------- IMPORTS -------------------------------------#
import sys                              # For sys.exit
import time                             # Import the time library for the sleep function
import easygopigo3 as easy              # Import the GoPiGo3 library


#--------------------------------- INITIALIZE GOPIGO -------------------------------------#
gpg = easy.EasyGoPiGo3()  # Create a EasyGoPiGo3 object

# Set initial speed
gpg.set_speed(200)


#--------------------------------- MAIN FUNCTION -------------------------------------#
def main():
    # Display remote control menu
    print("Console GoPiGo Robot control")
    print("Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\nspace bar: Stop GoPiGo Robot\n\tz: Exit\n")
    print("Speed: " + str(gpg.get_speed()))

    # Main menu loop
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
        # Exit program
        elif key_press == 'z':
            print("Exiting")
            sys.exit()
        else:
            print("Unknown Command, Please Enter Again")
        # Debounce the keys
        time.sleep(.05)


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
