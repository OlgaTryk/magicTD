from ctypes import *
from data.thread_data import *
import time

def listener():
    user = windll.user32
    # GetKeyState() returns 16 bit value, MSB is 1 when key is down
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate#:~:text=The%20return%20value,key%20is%20untoggled.
    while True:
        #escape key
        if user.GetKeyState(0x1B) >> 15:
            event_stop.set()
        # left arrow
        if user.GetKeyState(0x25) >> 15:
            cursor.move_left()
            time.sleep(0.2)
        # up arrow
        if user.GetKeyState(0x26) >> 15:
            cursor.move_up()
            time.sleep(0.2)
        # right arrow
        if user.GetKeyState(0x27) >> 15:
            cursor.move_right()
            time.sleep(0.2)
        # down arrow
        if user.GetKeyState(0x28) >> 15:
            cursor.move_down()
            time.sleep(0.2)
        if event_stop.is_set():
            break
