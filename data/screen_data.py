from enum import Enum

height = 540
width = 960
tile_size = 60


class Tile(Enum):
    UI = 0,
    EMPTY_GRASS = 1,
    EMPTY_PATH = 2
    TOWER = 3,
    ENEMY = 4


__all__ = ['height', 'width', 'tile_size']
