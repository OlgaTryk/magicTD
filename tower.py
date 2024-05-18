"""
class for stats and behaviour of a single placed tower
"""
from data.wave_data import TOWER_TYPES
from data.thread_data import time, cursor
from data.screen_data import TILE_SIZE
from data.game_data import game


class Tower:
    def __init__(self, tower_type):
        self.tower_type = tower_type
        self.damage = TOWER_TYPES.get(tower_type)["damage"]
        self.speed = TOWER_TYPES.get(tower_type)["speed"]
        self.range = TOWER_TYPES.get(tower_type)["range"]
        self.pos = [cursor.x * TILE_SIZE, cursor.y * TILE_SIZE]
        self.is_attacking = False
        self.target = (0, 0)

    def attack(self):
        """ attacks the first enemy found in range """
        while True:
            self.is_attacking = False
            for enemy in game.enemies:
                # range is asymmetrical because self.pos is upper left corner
                if self.pos[0] - self.range * TILE_SIZE < enemy.pos[0] < self.pos[0] + (self.range + 1) * TILE_SIZE:
                    if self.pos[1] - self.range * TILE_SIZE < enemy.pos[1] < self.pos[1] + (self.range + 1) * TILE_SIZE:
                        self.is_attacking = True
                        self.target = (enemy.pos[0], enemy.pos[1])
                        enemy.take_damage(self.damage)
                        break
            time.sleep(1/self.speed)
