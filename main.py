import pygame
import pygame.freetype
from data.thread_data import threading, cursor, game, event_stop
from data.screen_data import HEIGHT, WIDTH, TILE_SIZE
import keyboard

clock = pygame.time.Clock()

WHITE = (255, 255, 255)


def main():
    """ main loop, mostly drawing the GUI """
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    bg = pygame.image.load("assets/background.png")
    font = pygame.freetype.Font("assets/segoeuib.ttf", 40)
    enemy_sprites = {
        "goblin": pygame.image.load("assets/goblin.png")
    }

    while True:
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, WHITE,
                         (cursor.x * TILE_SIZE, cursor.y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

        font.render_to(screen, (61, 15), str(game.lives), WHITE)
        if game.curr_wave > 0:
            font.render_to(screen, (960 - 180, 15), "Wave " + str(game.curr_wave), WHITE)
            if not game.is_wave_over:
                for enemy in game.enemies:
                    screen.blit(enemy_sprites[enemy.enemy_type], (enemy.pos[0], enemy.pos[1]))

        # sets event_stop after closing the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_stop.set()
        if event_stop.is_set():
            pygame.quit()
            break

        clock.tick(60)


# Keyboard event listener
threadKeyboard = threading.Thread(target=keyboard.listener)
threadKeyboard.start()

try:
    main()
except KeyboardInterrupt:
    event_stop.set()
