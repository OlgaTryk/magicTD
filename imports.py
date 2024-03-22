import threading

# event to exit the program
event_stop = threading.Event()

__all__ = ['threading', 'event_stop']
