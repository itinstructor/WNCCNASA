#!/usr/bin/env python3
#
# EasyGoPiGo3 documentation: https://gopigo3.readthedocs.io/en/latest
# DI sensor documentation: https://di-sensors.readthedocs.io/en/master/
# Copyright (c) 2017 Dexter Industries Released under the MIT license
#
# History
# ------------------------------------------------
# Author     Date      	    Comments
# Loring     10/30/21       Change to I2C bus, add EasyIMUSensor
#
# Python example program for the Dexter IMU Sensor

##############################################################################
#
# !Connect to I2C port
#
##############################################################################

from time import sleep  # For sleep function

from di_sensors.easy_inertial_measurement_unit import EasyIMUSensor
# EasyIMUSensor library does not read temperature
# Use a lower level library to read temperature
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

from easygopigo3 import EasyGoPiGo3  # Import GoPiGo3 library
gpg = EasyGoPiGo3()  # Initialize an EasyGoPiGo3 object
print("Reading Dexter Industries IMU Sensor on a GoPiGo3 I2C port.")


easy_imu = EasyIMUSensor(port="I2C")
# Initialize IMU object on I2C bus: RPI_1SW to read temperature
imu = InertialMeasurementUnit(bus="RPI_1SW")

try:
    print("Calibrating the IMU . . . . please be patient . . .")
    easy_imu.safe_calibrate()    # Allow time for selfcalibration
    while True:
        # Read the magnetometer, gyroscope, accelerometer, euler, and temperature values
        mag = easy_imu.safe_read_magnetometer()
        gyro = easy_imu.safe_read_gyroscope()
        accel = easy_imu.safe_read_accelerometer()
        euler = easy_imu.safe_read_euler()
        temp = imu.read_temperature()

        string_to_print = "Magnetometer X: {:.1f}  Y: {:.1f}  Z: {:.1f} " \
            "Gyroscope X: {:.1f}  Y: {:.1f}  Z: {:.1f} " \
            "Accelerometer X: {:.1f}  Y: {:.1f} Z: {:.1f} " \
            "Euler Heading: {:.1f}  Roll: {:.1f}  Pitch: {:.1f} " \
            "Temperature: {:.1f}C".format(mag[0], mag[1], mag[2],
                                          gyro[0], gyro[1], gyro[2],
                                          accel[0], accel[1], accel[2],
                                          euler[0], euler[1], euler[2],
                                          temp)
        print(string_to_print)

        sleep(0.2)

# The program gets interrupted by Ctrl+C on the keyboard
except KeyboardInterrupt:
    # Unconfigure the sensors, disable the motors
    # Restore the LED's to the control of the GoPiGo3 firmware
    gpg.reset_all()
