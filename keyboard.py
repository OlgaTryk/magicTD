from ctypes import *
from imports import *


def listener():
    user = windll.user32
    # GetKeyState() returns 16 bit value, MSB is 1 when key is down
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate#:~:text=The%20return%20value,key%20is%20untoggled.
    while True:
        # 0x1B - escape key ASCII code
        if user.GetKeyState(0x1B) >> 15:
            event_stop.set()

        if event_stop.is_set():
            break
