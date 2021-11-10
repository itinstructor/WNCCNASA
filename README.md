# WNCC NASA NeSpaceGrant.org
- Respository for Western Nebraska Community College NASA Nebraska Space Grant Student Fellowships 21-22
- All Python code is Python3 compatible with Python 3.5 on the GoPiGo3
- This is part of an ongoing project sponsored by the Nebraska Space Grant
  - Enhancing Computer Science Curriculum using off-the-shelf Robotics Kits to Increase Whole Brain Learning
## Equipment
- GoPiGo3 from Modular Robotics https://gopigo.io
- Sensors from Modular Robotics and Grove
- Raspberry Pi OS Buster, GoPiGo3 libraries
- Raspbian for Robots OS (Deprecated)
## Resources
- GoPiGo Getting Started
- GoPiGo Tutorials and Resources
- GoPiGo Cloud Data with ThingSpeak Tutorial (Using the Distance Sensor)
- GoPiGo Scratch for Robots Tutorial
- GoPiGo library documentation
  - https://di-sensors.readthedocs.io/en/latest
  - https://gopigo3.readthedocs.io/en/latest/index.html
- Programming Resources (General programming resources)
- Video Streaming --> This folder contains tutorials and programs that use the Python picamera library to take stills and stream video
### Sensors--> Folder contains sensor tutorial and code
- sensor_distance.py --> Read the Dexter distance sensor in inches and mm to the console
- sensor_imu.py --> Read Dexter IMU sensor (magnetometer, gyroscope, accelerometer, euler, and temperature)
- sensor_ir.py --> Dexter IR sensor reads the GoBox remote control
- sensor_light_color.py --> Dexter Light Color Sensor
### Code Examples (Python 3.5)
- Original program code from GoPiGo3 file system, or https://github.com/DexterInd/GoPiGo3
  - /Dexter/Software/Python/Examples/
- blinkers.py --> Turn the blinkers on the front on and off
- buzzer.py --> Play notes on the piezo buzzer
- dex_eyes.py --> Turn the led's on the top (robot eyes) to different colors
- motors.py --> Dead reckoning movement
- obstacle_avoidance.py --> Obstacle avoidance with distance sensor
- pygame_timer_countdown.py --> Example of using a pygame timer event, concept can be used to read sensors in rc_pygame.py
- rc_console.py --> Console remote control
- rc_obstacle_avoidance_console.py --> Multithreaded console remote control and obstacle avoidance
- rc_obstacle_avoidance_tkinter.py --> Tkinter GUI remote control and obstacle avoidance
- rc_pygame.py --> PyGame GUI remote control
- rc_tkinter.py --> Tkinter GUI remote control, battery voltage display
- servo.py --> Test the servo
- startup_mailer.py --> Email the IP address of the local device on startup
#### Run all Python programs at the console --> python3 filename.py
#### ThingSpeak logging: http://www.billthecomputerguy.com/gopigo 
### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
