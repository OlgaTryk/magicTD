import threading
import cursor as cr

# event to exit the program
event_stop = threading.Event()

cursor = cr.Cursor(4, 3)

__all__ = ['threading', 'event_stop', 'cursor']

