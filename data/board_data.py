"""
shared between threads, can't be in thread_data because of a cursor.py circular import
"""
import map

board = map.Map()
