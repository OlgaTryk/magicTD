"""
keyboard input controller
"""

from ctypes import windll
from data.board_data import board
from data.game_data import game
from data.screen_data import Tile, TILE_SIZE
from data.thread_data import threading, time, cursor, event_stop, tower_range
from data.wave_data import TOWER_TYPES
from tower import Tower


def check_for_tower():
    """ checks if the tile with the cursor has a tower (to show range)"""
    tower = game.check_for_tower(cursor.x * TILE_SIZE, cursor.y * TILE_SIZE)
    if tower is not None:
        tower_range[0] = True
        tower_range[1] = cursor.x
        tower_range[2] = cursor.y
        tower_range[3] = tower.range
    else:
        tower_range[0] = False


def place_tower(tower_type):
    """ places the tower and starts a thread for it """
    # check if tile is valid
    if board.get_tile(cursor.x, cursor.y) == Tile.EMPTY_GRASS:
        # check if the player can afford the tower
        if game.money >= TOWER_TYPES[tower_type]["price"]:
            game.change_money(-TOWER_TYPES[tower_type]["price"])
            tower = Tower(tower_type)
            game.towers.append(tower)
            check_for_tower()
            board.set_tile(cursor.x, cursor.y, Tile.TOWER)
            thread = threading.Thread(target=tower.attack, daemon=True)
            thread.start()
            game.tower_threads.append(thread)

def listener():
    user = windll.user32
    # GetKeyState() returns 16 bit value, MSB is 1 when key is down
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate#:~:text=The%20return%20value,key%20is%20untoggled.
    while True:
        # escape key - exit
        if user.GetKeyState(0x1B) >> 15:
            event_stop.set()
        if event_stop.is_set():
            break
        # disable all other keys after the game ends
        if game.is_game_over:
            continue
        # left arrow - move cursor left
        if user.GetKeyState(0x25) >> 15:
            cursor.move_left()
            check_for_tower()
            time.sleep(0.2)
        # up arrow - move cursor up
        if user.GetKeyState(0x26) >> 15:
            cursor.move_up()
            check_for_tower()
            time.sleep(0.2)
        # right arrow - move cursor right
        if user.GetKeyState(0x27) >> 15:
            cursor.move_right()
            check_for_tower()
            time.sleep(0.2)
        # down arrow - move cursor down
        if user.GetKeyState(0x28) >> 15:
            cursor.move_down()
            check_for_tower()
            time.sleep(0.2)
        # space - start next wave
        if user.GetKeyState(0x20) >> 15:
            if game.is_wave_over:
                wave_thread = threading.Thread(target=game.next_wave, daemon=True)
                wave_thread.start()
                time.sleep(0.2)
        # 1 key - place first tower
        if user.GetKeyState(0x31) >> 15:
            place_tower("magic")
            time.sleep(0.2)
        # 2 key - place second tower
        if user.GetKeyState(0x32) >> 15:
            place_tower("ice")
            time.sleep(0.2)
