#!/usr/bin/env python3
# Name: buzzer.py
# Purpose: Play the Dextor buzzer
# ------------------------------------------------
# History
# ------------------------------------------------
# Author    Date        Comments
#
# EasyGoPiGo3 documentation: https://gopigo3.readthedocs.io/en/latest

import time # Import time library sleep function
import easygopigo3 as easy  # import the GoPiGo3 drivers
gpg = easy.EasyGoPiGo3()    # Create an instance of the GoPiGo3 class

# Create an instance of the Buzzer on port AD1
my_buzzer = gpg.init_buzzer("AD1")

# List of first few notes for Twinkle, Twinkle little start
twinkle = ["C4", "C4", "G4", "G4", "A4", "A4", "G4"]

print("Expecting a buzzer on Port AD1")
print("A4")
my_buzzer.sound(440)    # Play 440 hz
time.sleep(1)
print("A5")
my_buzzer.sound(880)    # Play 880 hz
time.sleep(1)
print("A3")
my_buzzer.sound(220)    # Play 220 hz
time.sleep(1)

# Go through list one note at a time
for note in twinkle:
    print(note)
    my_buzzer.sound(my_buzzer.scale[note])
    time.sleep(0.5)
    my_buzzer.sound_off()
    time.sleep(0.25)

my_buzzer.sound_off()

