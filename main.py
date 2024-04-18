import pygame
import pygame.freetype
from data.thread_data import *
from data.screen_data import *
import keyboard

clock = pygame.time.Clock()


# main loop, mostly for GUI
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    bg = pygame.image.load("assets/background.png")
    font = pygame.freetype.Font("assets/segoeuib.ttf", 40)

    while True:
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (cursor.x*tile_size, cursor.y*tile_size, tile_size, tile_size), 1)

        font.render_to(screen, (61, 15), str(game.lives), (255, 255, 255))
        if game.curr_wave > 0:
            font.render_to(screen, (960 - 180, 15), "Wave " + str(game.curr_wave), (255, 255, 255))

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
