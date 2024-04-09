from data.screen_data import *
from data.screen_data import Tile
from data.board_data import board


class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        if self.x > 0:
            if board.get_tile(self.x-1, self.y) != Tile.UI:
                self.x -= 1

    def move_right(self):
        if self.x < int(width/tile_size) - 1:
            if board.get_tile(self.x+1, self.y) != Tile.UI:
                self.x += 1

    def move_up(self):
        if self.y > 0:
            if board.get_tile(self.x, self.y-1) != Tile.UI:
                self.y -= 1

    def move_down(self):
        if self.y < int(height/tile_size) - 1:
            if board.get_tile(self.x, self.y+1) != Tile.UI:
                self.y += 1

