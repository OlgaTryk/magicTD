import pygame
import pygame.freetype
from data.thread_data import threading, event_stop, cursor, tower_range
from data.screen_data import HEIGHT, WIDTH, TILE_SIZE
from data.game_data import game
from data.wave_data import TOWER_TYPES
import keyboard

clock = pygame.time.Clock()

# font colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("assets/background.png")
font = pygame.freetype.Font("assets/segoeuib.ttf", 40)
enemy_sprites = {
    "goblin": pygame.image.load("assets/goblin.png"),
    "orc": pygame.image.load("assets/orc.png")
}
tower_sprites = {
    "magic": pygame.image.load("assets/magic_tower.png"),
    "ice": pygame.image.load("assets/ice_tower.png")
}
tower_attack_sprites = {
    "magic": pygame.image.load("assets/magic_attack.png"),
    "ice": pygame.image.load("assets/ice_attack.png")
}


def draw_towers():
    """ draws tower assets on screen """
    # tower range
    if tower_range[0]:
        tr = (tower_range[3] * 2 + 1) * TILE_SIZE
        s = pygame.Surface((tr, tr))
        s.set_alpha(80)
        s.fill(WHITE)
        screen.blit(s, (tower_range[1] * TILE_SIZE - (tower_range[3] * TILE_SIZE),
                        tower_range[2] * TILE_SIZE - (tower_range[3] * TILE_SIZE)))
    # towers
    for tower in game.towers:
        screen.blit(tower_sprites[tower.tower_type], (tower.pos[0], tower.pos[1]))
        if tower.is_attacking:
            tower.attack_on += 1
            if tower.attack_on < 60 / tower.speed:
                screen.blit(tower_attack_sprites[tower.tower_type],
                            (tower.pos[0], tower.pos[1]))
            elif tower.attack_on == 2 * (60 / tower.speed):
                tower.attack_on = 0


def main():
    """ main loop, mostly drawing the GUI """
    while True:
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        font.render_to(screen, (61, 15), str(game.lives), WHITE)
        font.render_to(screen, (61, 495), str(game.money), BLACK)
        for i in range(0, len(tower_sprites)):
            font.render_to(screen, (360 + 60 * 3 * i, 495),
                           str(TOWER_TYPES.get(list(TOWER_TYPES.keys())[i])["price"]), BLACK)

        if game.curr_wave > 0:
            font.render_to(screen, (960 - 180, 15), "Wave " + str(game.curr_wave), WHITE)
            if not game.is_wave_over:
                for enemy in game.enemies:
                    screen.blit(enemy_sprites[enemy.enemy_type], (enemy.pos[0], enemy.pos[1]))
        draw_towers()
        pygame.draw.rect(screen, WHITE,
                         (cursor.x * TILE_SIZE, cursor.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        # sets event_stop after closing the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_stop.set()
        if event_stop.is_set():
            pygame.quit()
            break
        if game.is_game_over:
            endgame()
            pygame.quit()
            break
        clock.tick(60)


def endgame():
    """ shows the game over screen """
    screen.fill(BLACK)
    font_end = pygame.font.Font("assets/segoeuib.ttf", 100)
    font_end_small = pygame.font.Font("assets/segoeuib.ttf", 50)
    while True:
        if game.is_game_won:
            text = font_end.render("YOU WON!", True, WHITE)
        else:
            text = font_end.render("YOU LOST", True, WHITE)
        text2 = font_end_small.render("Press esc to quit", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        text_rect_2 = text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))
        screen.blit(text, text_rect)
        screen.blit(text2, text_rect_2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_stop.set()
        if event_stop.is_set():
            return
        clock.tick(60)


# Keyboard event listener
threadKeyboard = threading.Thread(target=keyboard.listener)
threadKeyboard.start()

try:
    main()
except KeyboardInterrupt:
    event_stop.set()
