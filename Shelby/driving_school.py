# name: driving_school.py


#--------------------------------- IMPORTS -------------------------------------#
import time                                   # Import time library for sleep function
import easygopigo3 as easy                    # Import the GoPiGo3 library
gpg = easy.EasyGoPiGo3()                      # Create a EasyGoPiGo3 object
# Initialize a distance sensor object
distance_sensor = gpg.init_distance_sensor()
# Initialize a servo object on Servo Port 1
servo = gpg.init_servo("SERVO1")

# Set servo pointing straight ahead at 90 degrees
# You may have to change the degrees to adapt to your servo
# All servos line up slightly differently
# Less than 90 moves the servo to the right
# Greater than 90 moves the servo to the left
servo.rotate_servo(90)
gpg.set_speed(200)       # Set initial speed
AVOIDANCE_DISTANCE = 12  # Distance in inches from obstacle where the GoPiGo should stop


def main():
    right = right_square_turn()



def right_square_turn():
    # need a way to start it I think
    for x in range(4):
        gpg.forward(12)
        gpg.turn(90)

def left_square_turn(): 
    for x in range(4): # loop the things so I don't have to type that shit 4 times 
        gpg.forward(12) #go forward 12 inches
        gpg.turn(180) #180 degrees is turning left I think

def triangle_turn():
    for x in range(3):
        gpg.forward(12) #go forward 12 inches
        gpg.turn(60) # 60 degrees is interior angle for a triangle. If this gives weird results, try the anterior angle of 120


def octagon_turn(): #45 degrees for each turn
    for x in range(8): #Loop it 8 times to complete the shape
        gpg.forward(12) #forward 12inches
        gpg.turn(45)

def five_point_star(): #stars have like a lot of angles. 
    for x in range (5):
        gpg.forward(12)#12 inches
        gpg.turn(252) #idk if that is right maybe 72, or 108

def obstacle_avoid():
    print("Press ENTER to start")
    input()        # Wait for input to start

    gpg.forward()   # Start moving forward, GoPiGo will continue moving forward until it receives another movement command
    running = True  # Boolean/flag to control the while loop

    while running == True:                    # Loop while running == True
        dist = distance_sensor.read_inches()  # Find the distance of the object in front
        print("Dist:", dist, 'inches')        # Print feedback to the console
        # If the object is closer than the "distance_to_stop" distance, stop the GoPiGo
        if dist < AVOIDANCE_DISTANCE:
            print("Stopping")                 # Print feedback to the console
            gpg.stop()                        # Stop the GoPiGo
            running = False                   # Set running to false to break out of the loop

        # sleep is blocking code, nothing else can happen during sleep
        time.sleep(.1)  # 100 milliseconds



# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
