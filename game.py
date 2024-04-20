"""
main game logic:
- tracking amount of lives
- tracking amount of money
- spawning waves of enemies
- checking if game was lost or won
"""
import time
from data.wave_data import WAVE_SPAWN_DATA
from data.thread_data import threading
from enemy import Enemy


class Game:

    def __init__(self):
        self.lives = 100
        self.money = 200
        self.curr_wave = 0
        self.max_wave = 10
        self.is_wave_over = True  # is there a wave in progress ( aka unspawned or unkilled enemies)
        self.is_game_over = False
        self.is_game_won = False
        # is_game_over == True and is_game_won == False means the game was lost
        self.enemies = []

    def next_wave(self):
        """ spawns the next wave and ends game after the last one """
        self.curr_wave += 1
        self.is_wave_over = False

        # adding enemy objects to a list
        for enemy_type in WAVE_SPAWN_DATA[self.curr_wave - 1]:
            for enemy in range(WAVE_SPAWN_DATA[self.curr_wave - 1][enemy_type]):
                self.enemies.append(Enemy(enemy_type))

        threads = []
        for enemy in self.enemies:
            enemy_thread = threading.Thread(target=enemy.move, args=(self, ), daemon=True)
            threads.append(enemy_thread)
            enemy_thread.start()
            time.sleep(60/enemy.speed)

        # self.is_wave_over = True
        if self.curr_wave == self.max_wave:
            self.is_game_won = True
            self.is_game_over = False

    def lose_lives(self, lives_lost):
        """ removes lives when an enemy reaches the end
            and ends game if they reach 0 """
        lives_lock = threading.Lock()
        lives_lock.acquire()
        if self.lives >= lives_lost:
            self.lives -= lives_lost
        else:
            self.lives = 0
        if self.lives == 0:
            self.is_game_won = False
            self.is_game_over = True
        lives_lock.release()
