
class Game:

    def __init__(self):
        self.lives = 100
        self.money = 200
        self.curr_wave = 0
        self.max_wave = 10
        self.is_wave_over = True  # is there a wave in progress ( aka unspawned or unkilled enemies)
        # is_game_over == True and is_game_won == False means the game was lost
        self.is_game_over = False
        self.is_game_won = False

    def next_wave(self):
        self.curr_wave += 1
        self.is_wave_over = False

        # start enemy threads

        # join all enemy threads
        # self.is_wave_over = True
        if self.curr_wave == self.max_wave:
            self.is_game_won = True
            self.is_game_over = False

    def lose_lives(self, lives_lost):
        if self.lives >= lives_lost:
            self.lives -= lives_lost
        else:
            self.lives = 0
        if self.lives == 0:
            self.is_game_won = False
            self.is_game_over = True






