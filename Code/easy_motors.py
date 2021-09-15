#!/usr/bin/env python3
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license
# (http://choosealicense.com/licenses/mit/).
#
# For more information see
# https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is an example for controlling the GoPiGo3 motors.
# This uses the EasyGoPiGo3 library.  You can find more information on the library
# here:  https://gopigo3.readthedocs.io/en/master/api-basic/easygopigo3.html#easygopigo3
#
# Results:  The GoPiGo3 will move forward for 2 seconds, and then
# backward for 2 second.


# import the time library for the sleep function
import time
# import the GoPiGo3 drivers
from easygopigo3 import EasyGoPiGo3

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = EasyGoPiGo3()

print("Move the motors forward freely for 1 second.")
gpg.forward()
time.sleep(1)
gpg.stop()

print("Stop the motors for 1 second.")
time.sleep(1)

print("Drive the motors 5 inches and then stop.")
gpg.drive_inches(5, True)
time.sleep(1)

print("Turn right 1 second.")
gpg.right()
time.sleep(1)

print("Turn left 1 second.")
gpg.left()
time.sleep(1)

print("Stop!")
gpg.stop()
print("Done!")
