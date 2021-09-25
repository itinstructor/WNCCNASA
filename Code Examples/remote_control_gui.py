#!/usr/bin/env python3
#############################################################################################################
# Basic example for controlling the GoPiGo using the Keyboard
# Contributed by casten on Gitub https://github.com/DexterInd/GoPiGo/pull/112
#
# This uses the EasyGoPiGo3 library.  You can find more information on the library
# here:  https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3
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
#   l:  Spin left
#   r:  Spin right
#   t:  Increase speed
#   g:  Decrease speed
#   z:  Exit
# http://www.dexterindustries.com/GoPiGo/
# History
# ------------------------------------------------
# Author        Date            Comments
# Loring        04/28/18        Ported from GoPiG, converted to GoPiGo3
# Loring        09/06/21        Converted to Python3
# Loring        09/24/21        Refactored to OOP
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


class RemoteControlGUI():
    """ Initialize remote control """

    def __init__(self):
        # Try to create aa EasyGoPiGo23 object
        try:
            self.gpg = easy.EasyGoPiGo3()
        # Handle the exception if it doesn't work.
        except Exception as e:
            print("GoPiGo3 cannot be instantiated. Most likely wrong firmware version")
            print(e)

        import atexit
        atexit.register(self.gpg.stop)
        self.WHITE = (250, 250, 250)
        self.BLACK = (10, 10, 10)

        # Turn the blinkers off
        self.gpg.led_off("left")
        self.gpg.led_off("right")

        # Initialization for pygame
        pygame.init()
        self.screen = pygame.display.set_mode((425, 350))
        pygame.display.set_caption('GoPiGo Remote Control')

        # Create a background object the same size as the screen
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        # Fill the background with black
        self.background.fill(self.BLACK)

#--------------------------------- DISPLAY INSTRUCTIONS -------------------------------------#
    def display_instructions(self):
        # Create instructions for remote control of the robot
        instructions = '''                 GOPIGO REMOTE CONTROL

        (Put focus on this window to control the gopigo!)

        Press:
            W: Forward        L: Spin left
            A: Left                 O: Spin right
            D: Right
            S: Backward
            T: Increase speed    
            G: Decrease speed
            Z: Exit
        '''

        # Create font for display
        self.font = pygame.font.SysFont(None, 24)

        size_inc = 22
        index = 0

        # Print instructions on screen one line at a time
        for line in instructions.split('\n'):
            text = self.font.render(line, True, self.WHITE)
            self.background.blit(text, (10, 10+size_inc*index))
            index += 1

        # Create label to display speed
        label = self.font.render(
            'Speed: ' + str(self.gpg.get_speed()), True, self.WHITE)
        # Blit everything to a screen buffer
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(label, (10, 300))
        # Update the screen from the screen buffer
        pygame.display.update()

#--------------------------------- INCREASE SPEED -------------------------------------#
    def increase_speed(self):
        speed = self.gpg.get_speed()
        speed = speed + 100
        self.gpg.set_speed(speed)
        # Keep speed from going beyond 1000
        if(self.gpg.get_speed() > 1000):
            self.gpg.set_speed(1000)
        # Display speed
        lbl_speed = self.font.render(
            'Speed: ' + str(self.gpg.get_speed()), True, self.WHITE)
        # Blit everything to the screen buffer
        self.screen.blit(
            self.background,  # What to draw
            (0, 0)            # x, y coordinates
        )
        self.screen.blit(
            lbl_speed,        # Object to draw
            (10, 300)         # x, y coordinates
        )
        # Update the screen from the buffer
        pygame.display.update()

#--------------------------------- DECREASE SPEED -------------------------------------#
    def decrease_speed(self):
        speed = self.gpg.get_speed()
        speed = speed - 100
        self.gpg.set_speed(speed)
        # Keep speed from going below 0
        if(self.gpg.get_speed() < 0):
            self.gpg.set_speed(0)
        # Create label for speed
        label = self.font.render(
            'Speed: ' + str(self.gpg.get_speed()), True, self. WHITE)
        # Blit everything to a background buffer
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(label, (10, 300))
        # Update the screen from the buffer
        pygame.display.update()

#--------------------------------- MENU LOOP -------------------------------------#
    def menu_loop(self):
        # Loop to capture keystrokes
        while True:
            event = pygame.event.wait()
            if (event.type == pygame.KEYUP):
                self.gpg.stop()
                # Make sure the blinkers are off
                self.gpg.led_off("left")
                self.gpg.led_off("right")
                continue
            if (event.type != pygame.KEYDOWN):
                continue

            # Get the keyboard character from the keyevent
            char = event.unicode

            # Move forward
            if char == 'w':
                self.gpg.forward()

            # Turn left
            elif char == 'a':
                self.gpg.left()
                self.gpg.led_on("left")

            # Turn Right
            elif char == 'd':
                self.gpg.right()
                self.gpg.led_on("right")

            # Move backward
            elif char == 's':
                self.gpg.backward()
                # Turn both blinkers on
                self.gpg.led_on("left")
                self.gpg.led_on("right")

            # Spin left
            elif char == 'l':
                self.gpg.spin_left()
                self.gpg.led_on("left")

            # Spin right
            elif char == 'o':
                self.gpg.spin_right()
                self.gpg.led_on("right")

            # Increase speed
            elif char == 't':
                self.increase_speed()

            # Decrease speed
            elif char == 'g':
                self.decrease_speed()

            # Exit program
            elif char == 'z':
                print("\nExiting")
                sys.exit()


def main():
    remote_control_gui = RemoteControlGUI()
    remote_control_gui.display_instructions()
    remote_control_gui.menu_loop()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
