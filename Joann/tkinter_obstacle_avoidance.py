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
        

# Create an instance/object of the Distance Sensor class.
self.my_distance_sensor = gpg.init_distance_sensor()

# Read the sensor into variables
self.distanceInches = self.my_distance_sensor.read_inches()