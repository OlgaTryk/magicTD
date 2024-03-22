import pygame
from imports import *
import keyboard

clock = pygame.time.Clock()


# main loop, mostly for GUI
def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    while True:
        pygame.display.flip()

        # sets event_stop after closing the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_stop.set()

        if event_stop.is_set():
            pygame.quit()
            break

        clock.tick(30)


# Keyboard event listener
threadKeyboard = threading.Thread(target=keyboard.listener)
threadKeyboard.start()

main()
