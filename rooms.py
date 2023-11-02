import fight

rooms = {

        1: {"name": "Hall",
            "exits": ["east", "south"],
            "east": 2,
            "south": 3},

        2: {"name": "Bedroom",
            "exits": ["west", "south"],
            "west": 1,
            "south": 4,
            "item": "sword"},

        3: {"name": "Kitchen",
            "exits": ["north"],
            "north": 1,
            "enemycode": 1,
            "enemy": fight.enemies[1]["name"]
            },

        4: {"name": "Bathroom",
            "exits": ["north"],
            "north": 2}

    }