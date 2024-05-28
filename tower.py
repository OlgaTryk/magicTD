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
        self.target = None
        self.attack_on = 0  # number of frames the attack has been displayed

    def attack(self):
        """ attacks the enemy/enemies found in range """
        while True:
            self.is_attacking = False
            for enemy in game.enemies:
                if self.is_in_range(enemy):
                    self.is_attacking = True
                    # ice towers don't do damage
                    if self.tower_type == "ice":
                        enemy.is_slowed = True
                    else:
                        enemy.take_damage(self.damage)
                    # magic towers target only the first enemy
                    if self.tower_type == "magic":
                        self.target = enemy
                        break
                elif self.tower_type == "ice":
                    enemy.is_slowed = False

            time.sleep(1/self.speed)

    def is_in_range(self, enemy):
        """ returns True if the enemy is in range of the tower
            range is asymmetrical because self.pos is upper left corner """
        lower_x = self.pos[0] - self.range * TILE_SIZE
        upper_x = self.pos[0] + (self.range + 1) * TILE_SIZE
        lower_y = self.pos[1] - self.range * TILE_SIZE
        upper_y = self.pos[1] + (self.range + 1) * TILE_SIZE
        return lower_x <= enemy.pos[0] < upper_x and lower_y <= enemy.pos[1] < upper_y
