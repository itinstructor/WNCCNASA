#!/usr/bin/env python3
#############################################################################################################
# Example for controlling the GoPiGo using the Keyboard and obstacle avoidance
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
# William Loring  10/15/21		    Created as an example
# This uses the EasyGoPiGo3 library
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html
##############################################################################################################


#--------------------------------- IMPORTS -------------------------------------#
import sys                              # For sys.exit
import time                             # Import the time library for the sleep function
import easygopigo3 as easy              # Import the GoPiGo3 library


#--------------------------------- INITIALIZE THE GOPIGO -------------------------------------#
gpg = easy.EasyGoPiGo3()  # Create a EasyGoPiGo3 object

# Initialize a distance sensor object
distance_sensor = gpg.init_distance_sensor()
# Initialize a servo object on Servo Port 1
servo = gpg.init_servo("SERVO1")

# Set servo pointing straight ahead at 90 degrees
# You may have to change the degrees to adapt to your servo
# All servos line up slightly differently
# Less than 90 moves the servo to the right
# Greater than 90 moves the servo to the left
servo.rotate_servo(90)

gpg.set_speed(200)  # Set initial speed

AVOIDANCE_DISTANCE = 12  # Distance in inches from obstacle where the GoPiGo should stop


#--------------------------------- MAIN PROGRAM LOOP -------------------------------------#
def main():
    print("Console GoPiGo Robot control")
    print("Press:\n\tw: Move GoPiGo Robot forward\n\ta: Turn GoPiGo Robot left\n\td: Turn GoPiGo Robot right\n\ts: Move GoPiGo Robot backward\nspace bar: Stop GoPiGo Robot\n\tz: Exit\n")
    print("Speed: " + str(gpg.get_speed()))
    # Main program loop
    while True:
        remote_control_console()
        # sleep is blocking code, nothing else can happen during sleep
        # For debouncing the keys
        time.sleep(.05)
        obstacle_avoidance()
        # sleep is blocking code, nothing else can happen during sleep
        # For debouncing the keys
        time.sleep(.05)


#--------------------------------- REMOTE CONTROL CONSOLE -------------------------------------#
def remote_control_console():
    """
        Remote control the GoPiGo from the console
    """
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
        sys.exit()          # Exit the program
    else:
        print("Unknown Command, Please Enter Again")


#--------------------------------- OBSTACLE AVOIDANCE -------------------------------------#
def obstacle_avoidance():
    """
        Stop the GoPiGo if an obstacle is detected
    """
    dist = distance_sensor.read_inches()  # Find the distance of the object in front
    print("Dist:", dist, 'inches')        # Print feedback to the console

    # If the object is closer than the "distance_to_stop" distance, stop the GoPiGo
    if dist < AVOIDANCE_DISTANCE:
        print("Stopping")                 # Print feedback to the console
        gpg.stop()                        # Stop the GoPiGo
        print("Exiting")
        sys.exit()                        # Exit the program


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
