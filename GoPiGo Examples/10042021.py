# Import time and the GoPiGo3 library
import time
import easygopigo3 as EasyGoPiGo3

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
gpg = EasyGoPiGo3()

# Create an instance/object of the Distance Sensor class.
# I2C1 and I2C2 are just labels used for identifying the port on the GoPiGo3 board.
# But technically, I2C1 and I2C2 are the same thing, so we don't have to pass any port to the constructor.
my_distance_sensor = gpg.init_distance_sensor()

while True:
    # Read the sensor into variables
    mm = str(my_distance_sensor.read_mm())
    inches = int(my_distance_sensor.read_inches())

    # Print the values of the sensor to the console
    print("Distance Sensor Reading: " + int(inches) + " inches " + int(mm) + " mm")

    if inches <= 10 :
        gpg.stop()

    # sleep is only needed to see the measurements
    # sleep is blocking code, nothing else can happen during sleep
    # Don't use in production code
    time.sleep(1)
