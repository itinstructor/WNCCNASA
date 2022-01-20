"""
    Name: tkinter_obstacle_avoidance.py
    Written by:
    Written on:
    Purpose:

"""
# Import time and the GoPiGo3 library
import time
import easygopigo3 as easy
# Import tkinter for GUI
from tkinter import * 
# Override tk widgets with themed ttk widgets if available
from tkinter.ttk import *
# Used to exit the program 
import sys

class ObstacleAvoidanceGUI:

    def __init__(self):
        ''' Initialize the program '''
        # Detection distance in inches
        self.distanceInches = 10
        # Initialize an EasyGoPiGo3 object                    
        self.gpg = easy.EasyGOPiGo3()               
        self.servo = self.gpg.init_servo("SERVO1")  #
        # Set initial speed 
        self.gpg.set_speed(200)
        # Create an instance/object of the Distance Sensor class                     
        self.my_distance_sensor = self.gpg.init_distance_sensor()
        # Read the sensor into variables
        self.distanceInches = self.my_distance_sensor.read_inches()
        self.show_servo()
    
    def show_servo(self):
        '''show_servo is for show purposes only'''
        # Right
        print("Right")
        self.servo.rotate_servo(150)
        time.sleep(1)

        # Left
        print("Left")
        self.servo.rotate_servo(10)
        time.sleep(1)

        # Forward
        print("Forward")
        self.servo.rotate_servo(90)
        time.sleep(1)

    def obstacle_avoidance(self):

        # Drive Forward
        self.gpg.forward()

        # While true desicion to detect the obstacle
        while True:
            # Read the distance
            self.distanceInches = self.my_distance_sensor.read_inches()
            # Desicion to detect the distance
            if self.distanceInches <= 10:
                print("You're too close!")
                self.gpg.stop()
                # Servo turn right
                self.servo.rotate_servo(150)
                time.sleep(1)
                # Read the sensor into a variable
                self.distR = self.my_distance_sensor.read_inches()
                # Rotate the servo to the left
                self.servo.rotate_servo(10)
                time.sleep(1)
                # Read the sensor into a variable
                self.distL = self.my_distance_sensor.read_inches()

                # Desicion which distance is longer
                if self.distR > self.distL:
                    # Rotate the servo forward before moving
                     
                




            
        

# Create an instance/object of the Distance Sensor class.
self.my_distance_sensor = gpg.init_distance_sensor()

# Read the sensor into variables
self.distanceInches = self.my_distance_sensor.read_inches()