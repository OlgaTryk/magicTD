from data.screen_data import *
from data.screen_data import Tile


class Map:
    def __init__(self):
        self.width = int(width / tile_size)
        self.height = int(height / tile_size)
        self.tiles = [[Tile.EMPTY_GRASS for i in range(self.width)] for j in range(self.height)]
        # ui
        for i in range(self.width):
            self.tiles[0][i] = Tile.UI
            self.tiles[self.height - 1][i] = Tile.UI
        # path

    def get_tile(self, x, y):
        return self.tiles[y][x]
