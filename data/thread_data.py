"""
data shared between threads
"""
import threading
import time
from cursor import Cursor

cursor = Cursor(4, 3)

# event to exit the program
event_stop = threading.Event()

# highlighted tower to show the range of [show range?, x, y, range]
tower_range = [False, 0, 0, 0]
