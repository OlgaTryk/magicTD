""" details of enemies in specific waves """

ENEMY_TYPES = {
    "goblin": {
        "health": 10,
        "speed": 200,
        "damage": 100,
        "money": 10
    },
    "orc": {
        "health": 25,
        "speed": 30,
        "damage": 5,
        "money": 50
    }
    # TODO: add more types (especially faster enemy)
}

TOWER_TYPES = {
    "magic": {
        "damage": 2,
        "speed": 2,
        "price": 100,
        "range": 2
    },
    "flame": {
        "damage": 5,
        "speed": 1,
        "price": 300,
        "range": 1
    }
    # TODO: add 1-2 more types, add more stats to all
}

WAVE_SPAWN_DATA = [
    # wave 1
    {
        "goblin": 2
    },
    # wave 2
    {
        "goblin": 3
    },
    # wave 3
    {
        "goblin": 5
    },
    # wave 4
    {
        "goblin": 7
    },
    # wave 5
    {
        "goblin": 10
    },
    # wave 6
    {
        "goblin": 11
    },
    # wave 7
    {
        "goblin": 12
    },
    # wave 8
    {
        "goblin": 13
    },
    # wave 9
    {
        "goblin": 14
    },
    # wave 10
    {
        "goblin": 15
    }
    # TODO: change the waves once all the enemy types are defined
]
