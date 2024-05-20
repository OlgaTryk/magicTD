"""
represents the screen as array of tiles of different types
"""

from data.screen_data import HEIGHT, WIDTH, TILE_SIZE, PATH, Tile


class Map:
    def __init__(self):
        self.width = int(WIDTH / TILE_SIZE)
        self.height = int(HEIGHT / TILE_SIZE)
        self.tiles = [[Tile.EMPTY_GRASS for i in range(self.width)] for j in range(self.height)]
        # UI
        for i in range(self.width):
            self.tiles[0][i] = Tile.UI
            self.tiles[self.height - 1][i] = Tile.UI
        # path
        for i, coords in enumerate(PATH):
            # only add tiles visible on screen
            if coords[1] >= 0 and coords[0] < 16:
                self.tiles[coords[1]][coords[0]] = Tile.PATH

    def get_tile(self, x, y):
        """  returns the type of given tile """
        return self.tiles[y][x]

    def set_tile(self, x, y, tile):
        """ sets the type of given tile """
        self.tiles[y][x] = tile
