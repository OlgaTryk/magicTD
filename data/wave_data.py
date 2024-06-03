""" details of enemies in specific waves """

ENEMY_TYPES = {
    "goblin": {
        "health": 15,
        "speed": 200,
        "damage": 2,
        "money": 5
    },
    "orc": {
        "health": 200,
        "speed": 50,
        "damage": 10,
        "money": 15
    },
    "bat": {
        "health": 50,
        "speed": 1000,
        "damage": 5,
        "money": 5
    }
}

TOWER_TYPES = {
    "magic": {
        "damage": 2,
        "speed": 5,
        "price": 100,
        "range": 2
    },
    "ice": {
        "damage": 0,
        "speed": 10,
        "price": 200,
        "range": 1
    },
    "fire": {
        "damage": 10,
        "speed": 2,
        "price": 500,
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
        "goblin": 4
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
        "bat": 1,
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
        "bat": 5,
        "orc": 30
    },
    # wave 9
    {
        "bat": 10,
        "goblin": 30,
        "orc": 30
    },
    # wave 10
    {
        "bat": 30,
        "goblin": 50,
        "orc": 50
    }
]
