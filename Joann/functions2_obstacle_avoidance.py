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
        # 