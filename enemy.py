"""
class for stats and behaviour of a single enemy
"""

from data.thread_data import threading, time
from data.wave_data import ENEMY_TYPES
from data.screen_data import TILE_SIZE, PATH


class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        self.health = ENEMY_TYPES.get(enemy_type)["health"]
        self.speed = ENEMY_TYPES.get(enemy_type)["speed"]
        self.damage = ENEMY_TYPES.get(enemy_type)["damage"]
        self.money = ENEMY_TYPES.get(enemy_type)["money"]
        self.pos = [(PATH[0][0] * TILE_SIZE) - TILE_SIZE,
                    PATH[0][1] * TILE_SIZE]  # enemies spawn offscreen
        self.tile = 0  # index of the current tile on the path
        self.health_lock = threading.Lock()

    def move(self, game):
        """ moves along the path towards the exit """
        while self.tile != len(PATH) - 1:
            if self.health <= 0:
                game.change_money(self.money)
                game.enemies.remove(self)
                return
            if PATH[self.tile][0] * TILE_SIZE != PATH[self.tile + 1][0] * TILE_SIZE:
                # different X coordinate of the next tile -> move right
                self.pos[0] += 1
            elif PATH[self.tile][1] * TILE_SIZE < PATH[self.tile + 1][1] * TILE_SIZE:
                # current Y < next Y -> move up
                self.pos[1] += 1
            else:
                # the path never leads back to the left, so only other option is down
                self.pos[1] -= 1
            if (self.pos[0] == PATH[self.tile + 1][0] * TILE_SIZE
                    and self.pos[1] == PATH[self.tile + 1][1] * TILE_SIZE):
                # current position == next tile -> set next tile as current tile
                self.tile += 1
            time.sleep(1/self.speed)
        game.lose_lives(self.damage)
        game.enemies.remove(self)

    def take_damage(self, damage):
        """ lowers health while avoiding negative values """
        with self.health_lock:
            if self.health >= damage:
                self.health -= damage
            else:
                self.health = 0

    def reached_end(self):
        """ returns True if the enemy has reached the end of the path"""
        return bool(self.tile != len(PATH) - 1)
