"""
    Name: functions2_obstacle_avoidance.py
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

class ObstacleAvoidance:

    def __init__(self):
        ''' Initialize the program '''
        # Detection distance in inches
        self.distanceInches = 10
        # Initialize an EasyGoPiGo3 object
        self.gpg = easy.EasyGoPiGo3()
        self.servo = self.gpg.init_servo("SERVO1")
        # Set initial speed 
        self.gpg.set_speed(200)
        # Create an instance/object of the Distance Sensor class                     
        self.my_distance_sensor = self.gpg.init_distance_sensor()
        # Read the sensor into variables
        self.distanceInches = self.my_distance_sensor.read_inches()
        
        # Call the methods
        self.show_servo()
        self.obstacle_avoidance()

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

    
