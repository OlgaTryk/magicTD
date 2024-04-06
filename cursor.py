from data.screen_data import *

class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        if self.x > 0:
            self.x -= tile_size

    def move_right(self):
        if self.x < width - tile_size:
            self.x += tile_size

    def move_up(self):
        if self.y > 0:
            self.y -= tile_size

    def move_down(self):
        if self.y < height - tile_size:
            self.y += tile_size

