"""
data shared between threads
"""
import threading
from cursor import Cursor
import game

# event to exit the program
event_stop = threading.Event()

cursor = Cursor(4, 3)
game = game.Game()
