#!/usr/bin/env python3
"""
    Name:    thingspeak_distance_sensor.py
    Author:  William A Loring
    Created: 10/17/21 Revised:
    Purpose: Example of uploading data to a ThingSpeak Channel
"""
# This uses the EasyGoPiGo3 library
# https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3

# Import the time library for the sleep function
import time
import urllib.request
# Substitute your api key for updating that ThingSpeak channel
import thingspeak_api_key
# Import GoPiGo3 library
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class
# GPG is the GoPiGo3 object used to access methods and properties
gpg = EasyGoPiGo3()

# Initialize an object of the Distance Sensor class.
# I2C1 and I2C2 are just labels used for identifying the port on the GoPiGo3 board.
# Technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
my_distance_sensor = gpg.init_distance_sensor()

THINGS_URL = 'https://api.thingspeak.com/update?api_key=%s' % thingspeak_apikey.THINGS_API_KEY


def main():
    while True:
        # Read the sensor data into millimeters and inches variables
        mm = str(my_distance_sensor.read_mm())
        inches = str(my_distance_sensor.read_inches())

        # Print the values of the sensor to the console
        print("Distance Sensor Reading: " + inches + " inches " + mm + " mm")

        # Send data to ThingSpeak
        thingspeak_send(mm, inches)

        time.sleep(15)


def thingspeak_send(mm, inches):
    # Parameters to upload to ThingSpeak.com
    print("Upload to Thingspeak")
    # Open url and upload ThingSpeak data
    coms = urllib.request.urlopen(
        THINGS_URL + '&field1=%s&field2=%s' % (mm, inches))
    # Print response to console
    print("ThingSpeak Entry: " + str(coms.read().decode("utf-8")))
    # Close connection
    coms.close()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
