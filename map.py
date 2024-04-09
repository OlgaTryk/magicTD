from data.screen_data import *
from data.screen_data import Tile


class Map:
    def __init__(self):
        self.width = int(width / tile_size)
        self.height = int(height / tile_size)
        self.tiles = [[Tile.EMPTY_GRASS for i in range(self.width)] for j in range(self.height)]
        # left corner ui (wave number)
        self.tiles[0][0] = Tile.UI
        self.tiles[0][1] = Tile.UI
        # right corner ui (health)
        self.tiles[0][self.width - 2] = Tile.UI
        self.tiles[0][self.width - 1] = Tile.UI
        # bottom ui (towers and money)
        for i in range(self.width):
            self.tiles[self.height - 1][i] = Tile.UI
        # path


    def get_tile(self, x, y):
        return self.tiles[y][x]
