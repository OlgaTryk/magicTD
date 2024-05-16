""" details of enemies in specific waves """

ENEMY_TYPES = {
    "goblin": {
        "health": 10,
        "speed": 200,
        "damage": 1
    },
    "orc": {
        "health": 25,
        "speed": 30,
        "damage": 5
    }
    # TODO: add more types (especially faster enemy)
}

TOWER_TYPES = {
    "magic": {
        "damage": 1,
        "speed": 5,
        "price": 100
    },
    "flame": {
        "damage": 5,
        "speed": 1,
        "price": 300
    }
    # TODO: add 1-2 more types, add more stats to all
}

WAVE_SPAWN_DATA = [
    # wave 1
    {
        "goblin": 10,
        "orc": 0
    }
    # TODO: add the rest of the waves once all the types are defined
]
