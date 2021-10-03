#!/usr/bin/env python3

from tkinter import *
import sys     # Used to exit the program
import atexit  # Used for stopping the GoPiGo when closing the running program
import easygopigo3 as easy


# servo_range = [2,3,4,5,6,7,8]

class GoPiGoGUI:
    def __init__(self):
        self.gpg = easy.EasyGoPiGo3()
        # When the program exits, stop the GoPiGo
        # Unconfigure the sensors, disable the motors
        # and restore the LED to the control of the GoPiGo3 firmware
        atexit.register(self.gpg.reset_all)

        # Turn the blinkers off
        self.gpg.led_off("left")
        self.gpg.led_off("right")

        self.window = Tk()
        self.window.title("GoPiGo Remote Control")
        self.window.geometry("350x200")
        self.window.bind_all('<Key>', self.key_input)

        self.create_widgets()

        self.window.mainloop()

    def create_widgets(self):
        """
        W = Forward      Q = Spin Left
        S = Backward     E = Spin Right
        A = Left         
        D = Right        Spacebar = Stop
        T = Increase Speed
        G = Decrease Speed
        Speed: 300
        """
        lbl_remote_w = Label(text="W: Forward")
        lbl_remote_q = Label(text="Q: Spin Left")
        lbl_remote_s = Label(text="S: Backward")
        lbl_remote_e = Label(text="E: Spin Left")
        lbl_remote_a = Label(text="A: Left")
        lbl_remote_spacebar = Label(text="Spacebar: Stop")
        lbl_remote_d = Label(text="D: Right")
        lbl_remote_t = Label(text="T: Increase Speed")
        lbl_remote_g = Label(text="G: Decrease Speed")
        lbl_remote_z = Label(text="Z: Exit")

        # Get and display current GoPiGo speed setting
        speed = self.gpg.get_speed()
        self.lbl_speed = Label(text="Speed: " + str(speed))

        lbl_remote_w.grid(row=0, column=0, sticky=W)
        lbl_remote_q.grid(row=0, column=1, sticky=W)
        lbl_remote_s.grid(row=1, column=0, sticky=W)
        lbl_remote_e.grid(row=1, column=1, sticky=W)
        lbl_remote_a.grid(row=2, column=0, sticky=W)
        lbl_remote_spacebar.grid(row=2, column=1, sticky=W)
        lbl_remote_d.grid(row=3, column=0, sticky=W)
        lbl_remote_t.grid(row=4, column=0, sticky=W)
        lbl_remote_g.grid(row=5, column=0, sticky=W)

        self.lbl_speed.grid(row=6, column=0, sticky=W)
        lbl_remote_z.grid(row=6, column=1, sticky=W)

        # Set padding for all widgets
        for child in self.window.winfo_children():
            child.grid_configure(padx=4, pady=4)

    #--------------------------------- INCREASE SPEED -------------------------------------#
    def increase_speed(self):
        """ Increase the speed of the GoPiGo """
        # Get the current speed
        speed = self.gpg.get_speed()
        # Add 100 to the current speed
        speed = speed + 100
        # Keep speed from going beyond 1000
        if(speed > 1000):
            speed = 1000
        # Set the new speed
        self.gpg.set_speed(speed)
        # Display speed
        self.lbl_speed.config(text="Speed: " + str(speed))

#--------------------------------- DECREASE SPEED -------------------------------------#
    def decrease_speed(self):
        """ Decrease the speed of the GoPiGo """
        # Get current speed
        speed = self.gpg.get_speed()
        # Subtract 100 from the current speed
        speed = speed - 100
        # Keep speed from going below 0
        if(speed < 0):
            self.gpg.set_speed(0)
        # Set the speed
        self.gpg.set_speed(speed)
        # Display speed
        self.lbl_speed.config(text="Speed: " + str(speed))

#--------------------------------- KEY INPUT -------------------------------------#
    def key_input(self, event):
        key_press = event.keysym.lower()
        print(key_press)

        # Move Forward
        if key_press == 'w':
            self.gpg.forward()

        # Move Backward
        elif key_press == 's':
            self.gpg.backward()
            # Turn both blinkers on
            self.gpg.led_on("left")
            self.gpg.led_on("right")

        # Turn Left
        elif key_press == 'a':
            self.gpg.left()
            self.gpg.led_on("left")

        # Turn Right
        elif key_press == 'd':
            self.gpg.right()
            self.gpg.led_on("right")

        # Spin Left
        elif key_press == 'q':
            self.gpg.spin_left()
            self.gpg.led_on("left")

        # Spin Right
        elif key_press == 'e':
            self.gpg.spin_right()
            self.gpg.led_on("right")

        # Increase Speed
        elif key_press == 't':
            self.increase_speed()

        # Decrease Speed
        elif key_press == 'g':
            self.decrease_speed()

        # Stop
        elif key_press == 'space':
            self.gpg.stop()
            # Turn off the blinkers
            self.gpg.led_off("left")
            self.gpg.led_off("right")

        # Exit program
        elif key_press == 'z':
            print("\nExiting")
            sys.exit()

        # elif key_press == 'u':
        #     print(us_dist(15))

        # elif key_press.isdigit():
        #     if int(key_press) in servo_range:
        #         enable_servo()
        #         servo(int(key_press)*14)
        #         time.sleep(1)
        #         disable_servo()


# Create object from the program class
if __name__ == '__main__':
    # Create remote control object
    gopigo_gui = GoPiGoGUI()
