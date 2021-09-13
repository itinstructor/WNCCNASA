#!/usr/bin/env python3

from tkinter import *
from gopigo3 import *
import easygopigo3 as easy
try:
    gpg = easy.EasyGoPiGo3()
except Exception as e:
    print("GoPiGo3 cannot be instantiated. Most likely wrong firmware version")
    print(e)

# servo_range = [2,3,4,5,6,7,8]


def key_input(event):
    key_press = event.keysym.lower()
    print(key_press)

    if key_press == 'w':
        gpg.forward()
    elif key_press == 's':
        gpg.backward()
    elif key_press == 'a':
        gpg.left()
    elif key_press == 'd':
        gpg.right()
    elif key_press == 'q':
        gpg.spin_left()
    elif key_press == 'e':
        gpg.spin_right()
    elif key_press == 'space':
        gpg.stop()
    elif key_press == 'u':
        print(us_dist(15))

    # elif key_press.isdigit():
    #     if int(key_press) in servo_range:
    #         enable_servo()
    #         servo(int(key_press)*14)
    #         time.sleep(1)
    #         disable_servo()


window = Tk()
window.title("Remote Control")
window.geometry("350x200")
window.bind_all('<Key>', key_input)

instructions = """
W = Forward      Q = Spin Left
S = Backward     E = Spin Right
A = Left         Spacebar = Stop
D = Right
"""
lbl_remote = Label(text=instructions)
lbl_remote.grid(row=0, column=0)

window.mainloop()
