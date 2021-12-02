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
import atexit
import os
import pygame  # Gives access to KEYUP/KEYDOWN events
import sys  # Used for closing the running program
from gopigo3 import *
import easygopigo3 as easy
import time
import sys


class robot_gui():

    def __init__(self):
        self.__gpg = easy.EasyGoPiGo3()
        self.__AVOIDANCE_DISTANCE = 12
        self.__is_moving_forward = True


        #while robot is stopped test direction

        # Initialize a servo object on Servo Port 1
        self.__servo = self.__gpg.init_servo("SERVO1")

        self.__my_distance_sensor = self.__gpg.init_distance_sensor()

        # Set servo pointing straight ahead at 90 degrees
        # The degrees have been changed to adapt to this servo
        # All servos line up slightly differently
        self.__servo.rotate_servo(90)

        # When the program exits, stop the GoPiGo
        # Unconfigure the sensors, disable the motors
        # and restore the LED to the control of the GoPiGo3 firmware
        atexit.register(self.__gpg.reset_all)

        # Manage event loop speed
        self.clock = pygame.time.Clock()

        # Create timer for obstacle avoidance
        self.timer_event = pygame.USEREVENT+1

        # Set the timer to fire the even every 1000 ms
        # When the timer fires, it will appear on the event queue
        # This is a non blocking call, the program continues until the timer fires
        pygame.time.set_timer(self.timer_event, 300)

        

        self.setup()

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
            W: Forward              L: Spin left
            A: Left                 O: Spin right
            D: Right                M: Switch Mode
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

            event = pygame.event.wait()

            #self.auto_pilot()
            if event.type == self.timer_event:
                self.auto_pilot()

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

            # Decrease speed
            elif char == 'g':
                speed = self.__gpg.get_speed()
                speed = speed - 100
                self.__gpg.set_speed(speed)
                # Keep speed from going below 0
                if(self.__gpg.get_speed() < 0):
                    self.__gpg.set_speed(0)

            elif char == 'm':
                while True:
                    if (event.type != pygame.KEYDOWN):
                        continue
                    # Get the keyboard character from the keydown event
                    char = event.unicode
                    if char == 'n':
                        # goes out of the loop back to the main event loop
                        break
                        # runs once every loop until user presses n
                    self.auto_pilot()


            # Exit program
            elif char == 'z':
                print("\nExiting")
                sys.exit()

            # Limit loop to 60 frames per second
            self.clock.tick(60)

            # Update the screen from the backbuffer
            pygame.display.update()
            

    def auto_pilot(self):

        #running = True  # Boolean/flag to control the while loop

        #while running == True:                  # Loop while running == True
        #robot drives forward freely
        #self.__gpg.forward()   # Start moving forward, GoPiGo will continue moving forward until it receives another movement command
        dist = self.__my_distance_sensor.read_inches()  # Find the distance of the object in front
        #if we want to print distance to display below is code
        if(dist < 35):
            print("Dist:", dist, 'inches')        # Print feedback to the console
        # If the object is closer than the "distance_to_stop" distance, stop the GoPiGo
        if dist < self.__AVOIDANCE_DISTANCE:
            print("Stopping")                 # Print feedback to the console
            self.__gpg.stop()                        # Stop the GoPiGo
            #running = False
            #call function to determine best path
            self.testDistance()

    def testDistance(self):
        #pasue for 1 second
        time.sleep(1)
        print("Testing distance....")

        #servo looks left or right to determine best route to go
        #while looking left and right servo gets distance of object while looking that way
        self.__servo.rotate_servo(10)
        right_distance1 = self.__my_distance_sensor.read_inches() #right
        time.sleep(.5)
        self.__servo.rotate_servo(170)
        left_distance2 = self.__my_distance_sensor.read_inches() #left
        time.sleep(.5)
        self.__servo.rotate_servo(90)

        #determine which direction has most distance to go
        if(right_distance1 > left_distance2):
            #robot chooses direction 1 over 2 because it has more room to drive
            #robot turns to direct 1 and drives
            time.sleep(1)
            self.__gpg.turn_degrees(90)
            self.__gpg.forward()
        else:
            #robot chooses direction 2 over 1 because it has more room to drive
            #robot turns to direct 2 and drives
            time.sleep(1)
            self.__gpg.turn_degrees(-90)
            self.__gpg.forward()
            #running = False
    
        
#creates new robot object and calls function
robot = robot_gui()
robot.driving_gui()