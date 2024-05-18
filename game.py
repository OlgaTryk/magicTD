"""
main game logic:
- tracking amount of lives
- tracking amount of money
- spawning waves of enemies
- checking if game was lost or won
"""
from data.wave_data import WAVE_SPAWN_DATA
from data.thread_data import threading, time
from enemy import Enemy

money_lock = threading.Lock()
lives_lock = threading.Lock()


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
        self.enemy_threads = []
        self.towers = []
        self.tower_threads = []

    def next_wave(self):
        """ spawns the next wave and ends game after the last one """
        self.curr_wave += 1
        self.is_wave_over = False

        # adding enemy objects to a list
        for enemy_type in WAVE_SPAWN_DATA[self.curr_wave - 1]:
            for enemy in range(WAVE_SPAWN_DATA[self.curr_wave - 1][enemy_type]):
                self.enemies.append(Enemy(enemy_type))

        # creating a thread for each enemy
        for enemy in self.enemies:
            enemy_thread = threading.Thread(target=enemy.move, args=(self, ), daemon=True)
            self.enemy_threads.append(enemy_thread)
            enemy_thread.start()
            time.sleep(60/enemy.speed)
        # joining threads and removing dead enemies
        for thread in self.enemy_threads:
            thread.join()
        for thread in self.enemy_threads:
            if not thread.is_alive():
                self.enemy_threads.remove(thread)
            for enemy in self.enemies:
                if enemy.health <= 0 or enemy.reached_end():
                    self.enemies.remove(enemy)
        # ending wave after all enemies are dead
        self.is_wave_over = True
        if self.curr_wave == self.max_wave:
            self.is_game_won = True
            self.is_game_over = True
        else:
            with money_lock:
                self.money += self.curr_wave * 50

    def lose_lives(self, lives_lost):
        """ removes lives when an enemy reaches the end
            and ends game if they reach 0 """
        with lives_lock:
            if self.lives >= lives_lost:
                self.lives -= lives_lost
            else:
                self.lives = 0
            if self.lives == 0:
                self.is_game_won = False
                self.is_game_over = True

    def check_for_tower(self, x, y):
        """ returns a tower at a given location """
        for tower in self.towers:
            if tower.pos[0] == x and tower.pos[1] == y:
                return tower
        return None

    def change_money(self, amount):
        with money_lock:
            self.money += amount
