#!/usr/bin/env python3
#############################################################################################################
# Basic example for controlling the GoPiGo using the Keyboard
# Contributed by casten on Gitub https://github.com/DexterInd/GoPiGo/pull/112
#
# This code lets you control the GoPiGo from the VNC or Pi Desktop.
# These are non-blocking calls so it is much more easier to use.
#
# Controls:
#   w:  Move forward
#   a:  Turn left
#   d:  Turn right
#   s:  Move back
#   x:  Stop
#   t:  Increase speed
#   g:  Decrease speed
#   z:  Exit
# http://www.dexterindustries.com/GoPiGo/
# History
# ------------------------------------------------
# Author        Date            Comments
# Loring        04/28/18        Ported from GoPiG, converted to GoPiGo3
# Loring        09/06/21        Converted to Python3
'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2017  Dexter Industries
'''
##############################################################################################################
# Includes the basic functions for controlling the GoPiGo Robot
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

    # Make sure the blinkers are off
    gpg.led_off("left")
    gpg.led_off("right")

    # Initialization for pygame
    pygame.init()
    screen = pygame.display.set_mode((425, 350))
    pygame.display.set_caption('Remote Control Window')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Create instructions for remote control of the robot
    instructions = '''                 GOPIGO REMOTE CONTROL

    (Put focus on this window to control the gopigo!)

    Press:
        W: Forward
        A: Left
        D: Right
        S: Backward
        T: Increase speed
        G: Decrease speed
        Z: Exit
    '''

    size_inc = 22
    index = 0
    # Print instructions on screen
    for i in instructions.split('\n'):
        font = pygame.font.Font(None, 24)
        text = font.render(i, True, (10, 10, 10))
        background.blit(text, (10, 10+size_inc*index))
        index += 1

    label = font.render('Speed: ' + str(gpg.get_speed()), True, (10, 10, 10))
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(label, (10, 300))

    pygame.display.flip()

    # Loop to capture keystrokes
    while True:
        event = pygame.event.wait()
        if (event.type == pygame.KEYUP):
            gpg.stop()
            # Make sure the blinkers are off
            gpg.led_off("left")
            gpg.led_off("right")
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
            gpg.led_on("left")
        # Turn Right
        elif char == 'd':
            gpg.right()
            gpg.led_on("right")

        # Move back
        elif char == 's':
            gpg.backward()
            # Turn both blinkers on
            gpg.led_on("left")
            gpg.led_on("right")

        # Increase speed
        elif char == 't':
            speed = gpg.get_speed()
            speed = speed + 100
            gpg.set_speed(speed)
            # Keep speed from going beyond 1000
            if(gpg.get_speed() > 1000):
                gpg.set_speed(1000)
            # Display speed
            label = font.render(
                'Speed: ' + str(gpg.get_speed()), True, (10, 10, 10))
            screen.blit(background, (0, 0))
            screen.blit(label, (10, 300))
            pygame.display.flip()

        # Decrease speed
        elif char == 'g':
            speed = gpg.get_speed()
            speed = speed - 100
            gpg.set_speed(speed)
            # Keep speed from going below 0
            if(gpg.get_speed() < 0):
                gpg.set_speed(0)
            # Display speed
            label = font.render(
                'Speed: ' + str(gpg.get_speed()), True, (10, 10, 10))
            screen.blit(background, (0, 0))
            screen.blit(label, (10, 300))
            pygame.display.flip()

        # Exit program
        elif char == 'z':
            print("\nExiting")
            sys.exit()


main()

