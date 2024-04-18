import threading
import cursor as cr
import game

# event to exit the program
event_stop = threading.Event()

cursor = cr.Cursor(4, 3)
game = game.Game()

__all__ = ['threading', 'event_stop', 'cursor', 'game']

