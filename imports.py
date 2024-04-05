import threading

#position of active tile
current_tile = [0, 0]

# event to exit the program
event_stop = threading.Event()

__all__ = ['threading', 'event_stop', 'current_tile']
