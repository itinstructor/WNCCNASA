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
import time



    

class robot_gui():

    def __init__(self):
        self.__gpg = easy.EasyGoPiGo3()
        self.__inches = 0

        #while robot is stopped test direction

        # Initialize a servo object on Servo Port 1
        self.__servo = self.__gpg.init_servo("SERVO1")

        self.__my_distance_sensor = self.__gpg.init_distance_sensor()

        # Set servo pointing straight ahead at 90 degrees
        # The degrees have been changed to adapt to this servo
        # All servos line up slightly differently
        self.__servo.rotate_servo(85)

        self.setup()

    def distance_sensor_gui(self):
        # This example shows how to read values from the Distance Sensor

        # Create an instance of the GoPiGo3 class.
        # GPG will be the GoPiGo3 object.

        # Create an instance of the Distance Sensor class.
        # I2C1 and I2C2 are just labels used for identifyng the port on the GoPiGo3 board.
        # But technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
        #my_distance_sensor = self.__gpg.init_distance_sensor()

        while True:
            pass
           # Read the sensor into variables
            #self.__inches = str(my_distance_sensor.read_inches())

            # Print the values of the sensor to the console
            #print("Distance Sensor Reading: " + inches + " inches")

            #if distance sensor reads that robot is too close to something stop robot
            #robot then runs test to see which direction is best to go
            #if(inches < 10):

                #robot stops?

                #call function with servo test
                #self.distance_test()

    def distance_test(self):
        #rotate to right and test distance
        self.__servo.rotate_servo(0)
        time.sleep(5)
        if(self.__inches > 10):
            self.auto_pilot()
    
        self.__servo.rotate_servo(165)
        time.sleep(5)

    
    def setup(self):
        import atexit
        atexit.register(self.__gpg.stop)

        # Make sure the blinkers are off
        self.__gpg.led_off("left")
        self.__gpg.led_off("right")

        # Initialization for pygame
        pygame.init()
        self.__screen = pygame.display.set_mode((425, 350))
        pygame.display.set_caption('Remote Control Window')

        # Fill background
        self.__background = pygame.Surface(self.__screen.get_size())
        self.__background = self.__background.convert()
        self.__background.fill((250, 250, 250))

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

        size_inc = 22
        index = 0
        # Print instructions on screen
        for i in instructions.split('\n'):
            font = pygame.font.Font(None, 24)
            text = font.render(i, True, (10, 10, 10))
            self.__background.blit(text, (10, 10+size_inc*index))
            index += 1

        label = font.render('Speed: ' + str(self.__gpg.get_speed()), True, (10, 10, 10))
        # Blit everything to the screen
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(label, (10, 300))

        pygame.display.flip()

    def driving_gui(self):

        # Loop to capture keystrokes
        while True:
            self.auto_pilot()
            event = pygame.event.wait()
            if (event.type == pygame.KEYUP):
                self.__gpg.stop()
                # Make sure the blinkers are off
                self.__gpg.led_off("left")
                self.__gpg.led_off("right")
                continue
            if (event.type != pygame.KEYDOWN):
                continue

            # Get the keyboard character from the keyevent
            char = event.unicode

            # Move forward
            if char == 'w':
                self.__gpg.forward()

            # Turn left
            elif char == 'a':
                self.__gpg.left()
                self.__gpg.led_on("left")

            # Turn Right
            elif char == 'd':
                self.__gpg.right()
                self.__gpg.led_on("right")

            # Move backward
            elif char == 's':
                self.__gpg.backward()
                # Turn both blinkers on
                self.__gpg.led_on("left")
                self.__gpg.led_on("right")

            # Spin left
            elif char == 'l':
                self.__gpg.spin_left()
                self.__gpg.led_on("left")

            # Spin right
            elif char == 'o':
                self.__gpg.spin_right()
                self.__gpg.led_on("right")

            # Increase speed
            elif char == 't':
                speed = self.__gpg.get_speed()
                speed = speed + 100
                self.__gpg.set_speed(speed)
                # Keep speed from going beyond 1000
                if(self.__gpg.get_speed() > 1000):
                    self.__gpg.set_speed(1000)
                # Display speed
                label = self.__font.render(
                    'Speed: ' + str(self.__gpg.get_speed()), True, (10, 10, 10))
                self.__screen.blit(self.__background, (0, 0))
                self.__screen.blit(label, (10, 300))
                pygame.display.flip()

            # Decrease speed
            elif char == 'g':
                speed = self.__gpg.get_speed()
                speed = speed - 100
                self.__gpg.set_speed(speed)
                # Keep speed from going below 0
                if(self.__gpg.get_speed() < 0):
                    self.__gpg.set_speed(0)
                # Display speed
                label = self.__font.render(
                    'Speed: ' + str(self.__gpg.get_speed()), True, (10, 10, 10))
                self.__screen.blit(self.__background, (0, 0))
                self.__screen.blit(label, (10, 300))
                pygame.display.flip()

            # Exit program
            elif char == 'z':
                print("\nExiting")
                sys.exit()




    def auto_pilot(self):
        #robot drives forward freely
        
        self.__inches = int(self.__my_distance_sensor.read_inches())
        if(self.__inches > 10):
            self.__gpg.forward()
        if(self.__inches < 10):
            self.__gpg.stop()
    
        

robot = robot_gui()
robot.driving_gui()