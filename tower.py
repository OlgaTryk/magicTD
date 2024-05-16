"""
class for stats and behaviour of a single placed tower
"""
from data.wave_data import TOWER_TYPES
from data.thread_data import cursor
from data.screen_data import TILE_SIZE

class Tower:
    def __init__(self, tower_type):
        self.tower_type = tower_type
        self.damage = TOWER_TYPES.get(tower_type)["damage"]
        self.speed = TOWER_TYPES.get(tower_type)["speed"]
        self.pos = [cursor.x * TILE_SIZE, cursor.y * TILE_SIZE]
