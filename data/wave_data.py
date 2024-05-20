""" details of enemies in specific waves """

ENEMY_TYPES = {
    "goblin": {
        "health": 15,
        "speed": 200,
        "damage": 2,
        "money": 10
    },
    "orc": {
        "health": 100,
        "speed": 50,
        "damage": 10,
        "money": 30
    }
}

TOWER_TYPES = {
    "magic": {
        "damage": 1,
        "speed": 5,
        "price": 100,
        "range": 2
    },
    "ice": {
        "damage": 5,
        "speed": 1,
        "price": 300,
        "range": 1
    }
}

WAVE_SPAWN_DATA = [
    # wave 1
    {
        "goblin": 3
    },
    # wave 2
    {
        "goblin": 5
    },
    # wave 3
    {
        "goblin": 7,
        "orc": 3
    },
    # wave 4
    {
        "goblin": 10,
        "orc": 5
    },
    # wave 5
    {
        "goblin": 10,
        "orc": 10
    },
    # wave 6
    {
        "goblin": 20,
        "orc": 10
    },
    # wave 7
    {
        "goblin": 25,
        "orc": 15
    },
    # wave 8
    {
        "orc": 30
    },
    # wave 9
    {
        "goblin": 30,
        "orc": 30
    },
    # wave 10
    {
        "goblin": 50,
        "orc": 50
    }
]
