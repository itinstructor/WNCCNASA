#!/usr/bin/env python3
"""
    Name: thingspeak_distance_sensor.py
    Author: Wiiliam A Loring
    Created? 10/17/21 Revised:
    Purpose: Example of uploading data to a Thingspeak Channel
"""
# This uses the EasyGoPiGo3 library
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3

# Import the time library for the sleep function
import time
import requests
from easygopigo3 import EasyGoPiGo3     # Import GoPiGo3 library
