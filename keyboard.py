from ctypes import *
from imports import *
import time

lock = threading.Lock()

def listener():
    user = windll.user32
    # GetKeyState() returns 16 bit value, MSB is 1 when key is down
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate#:~:text=The%20return%20value,key%20is%20untoggled.
    while True:
        # 0x1B - escape key ASCII code
        if user.GetKeyState(0x1B) >> 15:
            event_stop.set()
        # left arrow
        if user.GetKeyState(0x25) >> 15 and current_tile[0] > 0:
            with lock:
                current_tile[0] -= 1
            time.sleep(0.2)
        # up arrow
        if user.GetKeyState(0x26) >> 15 and current_tile[1] > 0:
            with lock:
                current_tile[1] -= 1
            time.sleep(0.2)
        # right arrow
        if user.GetKeyState(0x27) >> 15 and current_tile[0] < 15:
            with lock:
                current_tile[0] += 1
            time.sleep(0.2)
        # down arrow
        if user.GetKeyState(0x28) >> 15 and current_tile[1] < 8:
            with lock:
                current_tile[1] += 1
            time.sleep(0.2)
        # width of screen / width of tile = 960/60 = 16
        # height of screen / height of tile = 540/60 = 9
        # indexing starts from 0, therefore ranges above end at 15 and 8
        if event_stop.is_set():
            break
