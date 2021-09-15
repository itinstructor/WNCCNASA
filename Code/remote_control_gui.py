#!/usr/bin/env python3
#############################################################################################################
# Basic example for controlling the GoPiGo using the Keyboard
# Contributed by casten on Gitub https://github.com/DexterInd/GoPiGo/pull/112
#
# This code lets you control the GoPiGo from the VNC or Pi Desktop.
# Also, these are non-blocking calls so it is much more easier to use.
#
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
# Author     	Date      		Comments
# Loring        04/28/18        Converted to GoPiGo3
# Loring        09/06/21        Converted to Python3
'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2017  Dexter Industries
'''
##############################################################################################################
# Has the basic functions for controlling the GoPiGo Robot
import pygame  # Gives access to KEYUP/KEYDOWN events
import sys  # Used for closing the running program
from gopigo3 import *
import easygopigo3 as easy


def main():
    # Try to create aa EasyGoPiGo23 object
    try:
        gpg = easy.EasyGoPiGo3()
    # Handle the exception if it doesn't work.
    except Exception as e:
        print("GoPiGo3 cannot be instantiated. Most likely wrong firmware version")
        print(e)

    import atexit
    atexit.register(gpg.stop)

    left_led = 100
    right_led = 0

    # Initialization for pygame
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Remote Control Window')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Create instructions for remote control of the robot
    instructions = '''
                GOPIGO CONTROL GUI

    This is a basic example for GoPiGo Robot control 
    (Put focus on this window to control the gopigo!)

    Press:
        ->W: Move GoPiGo Robot forward
        ->A: Turn GoPiGo Robot left
        ->D: Turn GoPiGo Robot right
        ->S: Move GoPiGo Robot backward
        ->T: Increase speed
        ->G: Decrease speed
        ->Z: Exit
    '''

    size_inc = 22
    index = 0
    # Print instructions on screen
    for i in instructions.split('\n'):
        font = pygame.font.Font(None, 30)
        text = font.render(i, 1, (10, 10, 10))
        background.blit(text, (10, 10+size_inc*index))
        index += 1

    label = font.render('Speed: ' + str(gpg.get_speed()), False, (10, 10, 10))
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(label, (10, 330))

    pygame.display.flip()
    remote_control()


def remote_control():
    # Loop to capture keystrokes
    while True:
        event = pygame.event.wait()
        if (event.type == pygame.KEYUP):
            gpg.stop()
            continue
        if (event.type != pygame.KEYDOWN):
            continue

        # Get the keyboard character from the keyevent
        char = event.unicode

        # Move forward
        if char == 'w':
            gpg.forward()

        # Turn left
        elif char == 'a':
            gpg.left()

        # Turn Right
        elif char == 'd':
            gpg.right()

        # Move back
        elif char == 's':
            gpg.backward()

        # Increase speed
        elif char == 't':
            speed = gpg.get_speed()
            speed = speed + 100
            gpg.set_speed(speed)
            # Keep speed from going beyond 1000
            if(gpg.get_speed() > 1000):
                gpg.set_speed(1000)
            label = font.render(
                'Speed: ' + str(gpg.get_speed()), False, (10, 10, 10))
            screen.blit(background, (0, 0))
            screen.blit(label, (10, 330))
            pygame.display.flip()

        # Decrease speed
        elif char == 'g':
            speed = gpg.get_speed()
            speed = speed - 100
            gpg.set_speed(speed)
            if(gpg.get_speed() > 1000):
                gpg.set_speed(1000)
            label = font.render(
                'Speed: ' + str(gpg.get_speed()), False, (10, 10, 10))
            screen.blit(background, (0, 0))
            screen.blit(label, (10, 330))
            pygame.display.flip()

        # Exit program
        elif char == 'z':
            print("\nExiting")
            sys.exit()


main()
