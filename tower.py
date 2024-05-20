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
        self.attack_on = 0  # number of frames the attack has been displayed

    def attack(self):
        """ attacks the enemy/enemies found in range """
        while True:
            self.is_attacking = False
            for enemy in game.enemies:
                # range is asymmetrical because self.pos is upper left corner
                if self.pos[0] - self.range * TILE_SIZE <= enemy.pos[0] < self.pos[0] + (self.range + 1) * TILE_SIZE:
                    if self.pos[1] - self.range * TILE_SIZE <= enemy.pos[1] < self.pos[1] + (self.range + 1) * TILE_SIZE:
                        self.is_attacking = True
                        enemy.take_damage(self.damage)
                        # magic towers target only the first enemy, ice towers attack all enemies in range
                        if self.tower_type == "magic":
                            break
            time.sleep(1/self.speed)
