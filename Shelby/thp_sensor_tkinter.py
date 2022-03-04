# thp_sensor.py with tkinter GUI addition

from time import sleep
from di_sensors.easy_temp_hum_press import EasyThpSensor
from tkinter import * 
import tkinter as tk

print("Temperature Humidity Pressure Sensor on an I2C port.")
my_thp = EasyThpSensor()


class TempGUI:
    def main():
       
        def __init__(self):

            while True:
                temp=self.temperature()
                hum=self.humidity()
                press=self.pressure()

                # print the values to the console
                print("Temperature: {:5.1f}F Humidity: {5.1f}% Pressure: {:5.2f}".format(
                    temp, hum, press))
                #Pause 5sec beteen readings
                sleep(5)


    def temperature(self):
            # read the temperature
            # temp=my_thp.safe_celsius()
            temp = my_thp.safe_fahrenheit()
            #Pause 5sec beteen readings
            sleep(5)
            return temp


    def humidity(self):

            # read the relative humidity
            hum = my_thp.safe_pressure()
            #Pause 5sec beteen readings
            sleep(5)
            return hum

    def pressure():
            #Read the pressure in pascals
            press=my_thp.safe_pressure()
            # convert pascals to inHg, compensate for 4000' altitude
            press = (press/3386.33857)+4.08
            #Pause 5sec beteen readings
            sleep(5)
            return press


    
    def create_widgets(self):
            """
            create and grid widgets
            """

            # Create a main label frame to hold widgets
            self.main_frame = LabelFrame(
                self.window,
                bg='#c6ff9e',
                text="Local temperature",
                relief=GROOVE)

            #label to display temp
            self.lbl_temp=LabelFrame(
                self.mainframe,
                text='Temperature',
                bg="light green",
                width=20,
                command=self.temperature)
                #label to display press
            self.lbl_press=LabelFrame(
                self.mainframe,
                text='Pressure',
                bg="light green",
                width=20,
                command=self.pressure)
                #label to display hum
            self.lbl_hum=LabelFrame(
                self.mainframe,
                text='Humidity',
                bg="light green",
                width=20,
                command=self.humidity)
            # Use grid layout manager to place widgets in the frame
            self.lbl_temp.grid(row=1, column=1)
            self.lbl_hum.grid(row=2, column=1)
            self.lbl_press.grid(row=3,column=1)

            # Set padding between frame and window
            self.main_frame.grid_configure(padx=2, pady=2)
            # set padding for all widgets in the frame
            for widget in self.main_frame.winfo_children():
                widget.grid_configure(padx=2, pady=2)



    





# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()

