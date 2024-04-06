import pygame
from data.thread_data import *
from data.screen_data import height, width, tile_size
import keyboard

clock = pygame.time.Clock()

# main loop, mostly for GUI
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    while True:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (cursor.x, cursor.y, tile_size, tile_size), 1)
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

main()
