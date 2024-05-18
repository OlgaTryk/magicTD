"""
shared between threads, can't be in thread_data because of a circular import
"""
import game

game = game.Game()
