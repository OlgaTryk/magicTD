"""
controls the cursor used for placing towers
"""

from data.screen_data import HEIGHT, WIDTH, TILE_SIZE, Tile
from data.board_data import board


class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        """ moves the cursor one tile to the left unless the destination tile is UI/offscreen """
        if self.x > 0:
            if board.get_tile(self.x-1, self.y) != Tile.UI:
                self.x -= 1

    def move_right(self):
        """ moves the cursor one tile to the right unless the destination tile is UI/offscreen """
        if self.x < int(WIDTH/TILE_SIZE) - 1:
            if board.get_tile(self.x+1, self.y) != Tile.UI:
                self.x += 1

    def move_up(self):
        """ moves the cursor one tile up unless the destination tile is UI/offscreen """
        if self.y > 0:
            if board.get_tile(self.x, self.y-1) != Tile.UI:
                self.y -= 1

    def move_down(self):
        """ moves the cursor one tile down unless the destination tile is UI/offscreen """
        if self.y < int(HEIGHT/TILE_SIZE) - 1:
            if board.get_tile(self.x, self.y+1) != Tile.UI:
                self.y += 1
