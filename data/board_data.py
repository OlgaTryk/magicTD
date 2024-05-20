"""
shared between threads, can't be in thread_data because of a circular import
"""
import game_map

board = game_map.Map()
