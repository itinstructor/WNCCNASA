# Import time and the GoPiGo3 library
import time
import easygopigo3 as easy

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = easy.EasyGoPiGo3()
servo = gpg.init_servo("SERVO1")


# Create an instance/object of the Distance Sensor class.
# I2C1 and I2C2 are just labels used for identifying the port on the GoPiGo3 board.
# But technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
my_distance_sensor = gpg.init_distance_sensor()

# Read the sensor into variables
# mm = str(my_distance_sensor.read_mm())
distanceInches = my_distance_sensor.read_inches()

# Print the values of the sensor to the console
#print("Distance Sensor Reading: " +
       # distanceInches + " inches ")  

# Right
print("Right")
servo.rotate_servo(150)
time.sleep(1)

# Left
print("Left")
servo.rotate_servo(10)
time.sleep(1)

# Forward
print("Forward")
servo.rotate_servo(90)
time.sleep(1)

gpg.forward()   


while True:
    
    # Read the distance
    distanceInches = my_distance_sensor.read_inches()
    # Decision
    if distanceInches <= 10:
        print("You're too close!")
        gpg.stop()
        # Servo
        servo.rotate_servo(150)
        time.sleep(1)
        distR = my_distance_sensor.read_inches()
        print("Distance to the right: " + format(distR))
        servo.rotate_servo(10)
        time.sleep(1)
        distL = my_distance_sensor.read_inches
        print("Distance to the left: " + format(distL))
        if distR > distL:
            servo.rotate_servo(90)
            time.sleep(1)
            gpg.turn_degrees(90)
            time.sleep(1)
            gpg.forward()
        else:
            servo.rotate_servo(90)
            time.sleep(1)
            gpg.turn_degrees(-90)
            time.sleep(1)
            gpg.forward()
    

    # sleep is only needed to see the measurements
    # sleep is blocking code, nothing else can happen during sleep
    # Don't use in production code
    # time.sleep(1)
