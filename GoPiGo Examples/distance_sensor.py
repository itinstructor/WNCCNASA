#!/usr/bin/env python3
"""
    Name: distance_sensor.py
    Author: William A Loring
    Created: 09-25-21 Revised:
    Purpose: Demonstrate reading the distance sensor in mm and inches
"""
# This uses the EasyGoPiGo3 library.  You can find more information on the library
# here:  https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3

# Dexter Industries Distance Sensor example for the GoPiGo3
#
# This example shows a basic example to read sensor data from the Dexter Industries Distance Sensor.  This sensor is a white PCB.
#
# Connect the Dexter Industries Distance Sensor to an I2C port on the GoPiGo3.
# You can find the Distance Sensor here: https://www.dexterindustries.com/shop/distance-sensor/
# Have a question about this example?  Ask on the forums here:
# http://forum.dexterindustries.com/c/gopigo
#
# Initial Date: 16 Jun 2017  John Cole
# http://www.dexterindustries.com/GoPiGo

# Import time and the GoPiGo3 library
import time
import easygopigo3 as easy

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = easy.EasyGoPiGo3()

# Create an instance/object of the Distance Sensor class.
# I2C1 and I2C2 are just labels used for identifying the port on the GoPiGo3 board.
# But technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
my_distance_sensor = gpg.init_distance_sensor()

while True:
    # Read the sensor into variables
    mm = str(my_distance_sensor.read_mm())
    inches = str(my_distance_sensor.read_inches())

    # Print the values of the sensor to the console
    print("Distance Sensor Reading: " + inches + " inches " + mm + " mm")

    # sleep is only needed to see the measurements
    # sleep is blocking code, nothing else can happen during sleep
    # Don't use in production code
    time.sleep(1)
