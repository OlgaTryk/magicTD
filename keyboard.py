"""
keyboard input controller
"""

from ctypes import windll
import time
from data.thread_data import threading, cursor, game, event_stop


def listener():
    user = windll.user32
    # GetKeyState() returns 16 bit value, MSB is 1 when key is down
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate#:~:text=The%20return%20value,key%20is%20untoggled.
    while True:
        # escape key - exit
        if user.GetKeyState(0x1B) >> 15:
            event_stop.set()
        # left arrow - move cursor left
        if user.GetKeyState(0x25) >> 15:
            cursor.move_left()
            time.sleep(0.2)
        # up arrow - move cursor up
        if user.GetKeyState(0x26) >> 15:
            cursor.move_up()
            time.sleep(0.2)
        # right arrow - move cursor right
        if user.GetKeyState(0x27) >> 15:
            cursor.move_right()
            time.sleep(0.2)
        # down arrow - move cursor down
        if user.GetKeyState(0x28) >> 15:
            cursor.move_down()
            time.sleep(0.2)
        # space - start next wave
        if user.GetKeyState(0x20) >> 15:
            if game.is_wave_over:
                wave_thread = threading.Thread(target=game.next_wave, daemon=True)
                wave_thread.start()
                time.sleep(0.2)
        if event_stop.is_set():
            break
