"""
data regarding screen dimensions, tile size and kinds of tiles
"""

from enum import Enum

HEIGHT = 540
WIDTH = 960
TILE_SIZE = 60

# coordinates of path tiles
PATH = [
    [-1, 5],  # offscreen tile the enemies spawn on
    [0, 5], [1, 5], [2, 5], [3, 5],
    [3, 4], [3, 3], [3, 2],
    [4, 2], [5, 2], [6, 2], [7, 2],
    [7, 3], [7, 4], [7, 5], [7, 6],
    [8, 6], [9, 6], [10, 6],
    [10, 5], [10, 4],
    [11, 4], [12, 4], [13, 4], [14, 4], [15, 4],
    [16, 4]  # offscreen tile the enemies despawn on (if they reach the end)
]


class Tile(Enum):
    """ enum for different types of tiles """
    UI = 0,
    EMPTY_GRASS = 1,
    PATH = 2,
    TOWER = 3
