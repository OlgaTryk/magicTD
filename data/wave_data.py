""" details of enemies in specific waves """

ENEMY_TYPES = {
    "goblin": {
        "health": 10,
        "speed": 60,
        "damage": 1
    },
    "orc": {
        "health": 25,
        "speed": 30,
        "damage": 5
    }
    # TODO: add more types (especially faster enemy)
}

WAVE_SPAWN_DATA = [
    # wave 1
    {
        "goblin": 10,
        "orc": 0
    }
    # TODO: add the rest of the waves one all the types are defined
]
