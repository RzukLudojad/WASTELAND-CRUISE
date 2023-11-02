#lista lokacji w grze. każda lokacja/pokój ma elementy takie jak opis (dwa opisy, w zależności czy odwiedzaliśmy to miejsce już wczesniej)
#przejścia do innych lokacji i zmienną 'visited' (patrz wyżej). Oprócz tego niektóre z nich mają dodatkowe elementy określające występowanie
#przeciwników, przedmiotów, npc, lub też zamkniętych drzwi (które trzeba otworzyć kluczem)

import npc

#POZIOM 1 - PUSTYNIA

desert = {
            1: {"name": "Bed area [spawn]",
                "description_new": """You open your eyes. You remember absolutely nothing about what happened before and how you got here
As you raise up from the pallet, you realize you're in some kind of shelter. You hear wind blowing
outside and notice that everything here is covered in sand.
There's also a door to your right with some person sitting in front of it, resting by the wall.""",
                "description": "This is where you've been sleeping. It surely had to be long time since you've been found.",
                "exits": ["east"],
                "east": 2,
                "visited": False
                },
            2: {"name": "Doorway",
                "description_new": """The person by the door seems to be sleeping, but maybe if you managed to wake him up, he'd be willing
to share some information about this place and provide you with some idea about circumstances in which you got here.\n
\n\033[34m(TIP: type 'talk' to interact with the npc)\n\033[0m""",
                "description": "Randy's still lying besides the wall. Raising his head on your sight he asks \044[32m'Have you found my book?\033[0m'",
                "npc": npc.Explorer,
                "exits": ["west"],
                "key": ["south"],
                "west": 1,
                "south": 3,
                "visited": False
                },

            3: {"name": "Desert (1)",
                "description_new": """As you open the door, you're imidiatelly faced with a powerful blizzard of sand,
which makes it hard to see anything beyond your own hands. You can only move forward
in hope of finding the house.""",
                "description": "It's windy out here, better not stay here for too long",
                "exits": ["north", "south"],
                "north": 2,
                "south": 4,
                "visited": False
                },
            4: {"name": "Desert (2)",
                "description_new": """As the wind calms down for a moment, you are able to notice some shape of a building at some distance
As the sandstorm returns, you tell yourself not to stop.""",
                "description": "It's windy out here, better not stay here for too long",
                "exits": ["north", "south"],
                "north": 3,
                "south": 5,
                "visited": False
                },
            5: {"name": "Desert (3)",
                "description_new": "You're getting closer... Just... Few... More... Steps.\n",
                "description": "It's windy out here, better not stay here for too long",
                "exits": ["north", "south"],
                "north": 4,
                "south": 6,
                "visited": False
                },
            6: {"name": "Desert (4)",
                "description_new": "You finally reach for the door.\n",
                "description": "It's windy out here, better not stay here for too long",
                "exits": ["north", "south"],
                "north" : 5,
                "south" : 7,
                "visited": False
                },

            7: {"name": "Hall",
                "description_new": """The house seems very old, with some ancient wooden furniture covered in cobweb.
You see two doors - one directly in front of you and the second one to your left""",
                "description": "You are in the hall.",
                "exits": ["north", "east", "south"],
                "north" : 6,
                "east": 8,
                "south": 9,
                "visited": False
                },

            8: {"name": "Bedroom",
                "description_new": """You see a small bed with some metal item dropped nearby. Apart from path leading to hall
there's one door on the south side. Looks like it's leading to bathroom.""",
                "description": "You entered the bedroom",
                "exits": ["west", "south"],
                "west": 7,
                "south": 10,
                "item": "club",
                "visited": False
                },

            9: {"name": "Kitchen",
                "description_new": """The kitchen seems all dirty and messy, covered in spilled cereals and rat excrements.
As you look around, you see something aproaching you. It's a big,
brown rat and it's trying to attack you\n
\n\033[34m(TIP: You can either choose to fight with your enemy or try to run away.
However, if the escape proves unsuccessful, you will lose some health points
and you will be forced to fight anyway.)\033[0m""",
                "description": "You are in the kitchen. It's still very stinky in here, though.",
                "exits": ["north"],
                "north": 7,
                "enemycode": 1,
                "enemy": npc.enemies[1]["name"],
                "item": "book",
                "visited": False
                },

            10: {"name": "Bathroom",
                "description_new" : "It's a very stinky place, better not settle your needs here unless you really need to.",
                "description": "You see nothing out of the ordinary.",
                "exits": ["north"],
                "north": 8,
                "visited": False
                }
            }

#POZIOM 2 - MIASTO
town = {

        1: {"name": "City Square [spawn]",
            "description_new": """After a long trip, Randy guides you through some barricades,
showing guard some piece of paper, he took from the book, you gave him.
After passing some tents and some makeshift wooden shelters, you arrive at something,
that seems like a main square of this village. Randy says:
\033[32m'We're finally there. Feel free to walk around and take a look.
You have a bar at the west side, a weaponry on the east and a town hall at the south.
Now excuse me, i need to go to the hospital, which, by the way, is located at the north'\033[0m,
then he turns and walks away.""",
            "description": """You're standing right in the middle of the city. There's pub on the west side, a market on the"
east, hospital up north, and something that looks like city council in the south.""",
            "exits": ["north", "south", "east", "west"],
            "north": 2,
            "south": 4,
            "east": 12,
            "west": 11,
            "visited": False
            },
        2: {"name": "City Square (north)",
            "description": "You’re on the north side of the main square, close to the 'Hospital Street'",
            "description_new": "You see a street leading to a hospital, directly in front of you",
            "exits": ["north", "south", "east", "west"],
            "north": 3,
            "south": 1,
            "east": 13,
            "west": 6,
            "visited": False
            },
        3: {"name": "Hospital Street",
            "description": "You’re halfway between hospital and the main square",
            "description_new": """As you move forward, you see some tents on both sides of the road and a big,
red cross in front of you. The building looks rather rusty, but solid.
That’s the place where Randy went, maybe you’ll be able to visit him there?""",
            "exits": ["north", "south"],
            "north": 30,
            "south": 2,
            "visited" : False
            },
        4: {"name": "City Square (south)",
            "description": "You're on the south side of the main square, close to the Town Hall",
            "description_new":  """As you move to the south, you see a surprisingly good looking building.
According to Randy, this should be the Town Hall""",
            "exits": ["north", "south", "east", "west"],
            "north": 1,
            "south": 5,
            "east": 14,
            "west": 7,
            "visited": False
            },
        5: {"name": "Town Hall Street",
            "description": """You’re halfway between the Town Hall and the main square.
You’re on a street leading from the main square to The Town Hall""",
            "description_new":  "After passing some houses, you reach the building, which is supposedly the Town Hall",
            "exits": ["north", "west"],
            "north": 4,
            "west": 8,
            "visited": False
            },
        6: {"name": "City Square (north-west)",
            "description": "You’re at the north-west corner of the main square.",
            "description_new":  "You see some houses and a garden behind them",
            "exits": ["south", "east"],
            "south": 11,
            "east": 2,
            "visited": False
            },
        7: {"name": "City Square (south-west)",
            "description": "You’re at the south-west corner of the main square.",
            "description_new": "Pub's wall on the west side, and you see a house on the south side.",
            "exits": ["north", "east"],
            "north": 11,
            "east": 4,
            "visited": False
            },
        8: {"name": "Side Street",
            "description": "You're on the begging of a small road, south from pub.",
            "description_new": """Turning from the Town Hall Street, you see some rather claustrophobic looking road with
big, wooden barracks on both sides.""",
            "exits": ["east", "west"],
            "east": 5,
            "west": 9,
            "visited": False
            },
        9: {"name": "Side Street (2)",
            "description": "You enter this small, narrow road, which, to be honest, still feels kinda out of place.",
            "description_new": """You’re enter a small, narrow street, going by the south wall of the bar.
                                You see some rather ruined cabins on the other side. Are people really living in these?""",
            "exits": ["east", "west"],
            "east": 8,
            "west": 10,
            "visited": False
            },
        10: {"name": "Side Street (3)",
             "description": "You reach the very end of this street.",
             "description_new":  """The street ends with a building that seems like a storage. The further road is closed,
but you can see a small greenhouse behind the storage. The greenhouse has some small,
weird fruits faintly growing. There’s very few of them and it’s no way that it could feed
the whole population of this town.""",
             "exits": ["east"],
             "east": 9,
             "visited": False
            },
        11:{"name": "City Square (west)",
            "description": "You're standing in front of 'Papa John's Pub'",
            "description_new": """You're on the west side of main square. In front of you there's some hovel with a big signboard
saying 'Papa John's Pub'. Sounds like fun, eh?""",
            "exits": ["north", "south", "east", "west"],
            "north": 6,
            "south": 7,
            "east": 1,
            "west": 18,
            "visited": False
             },
        12:{"name": "City Square (east)",
            "description": "You’re on the east side of city square, close to weaponry",
            "description_new":  "Moving to the east side of main square, you see a market place nearby.",
            "exits": ["north", "south","west","east"],
            "north": 13,
            "south": 14,
            "east": 29,
            "west": 1,
            "visited": False
            },
        13:{"name": "City Square (north-east)",
            "description": "You’re at the north-east corner of the main square",
            "description_new":  "",
            "exits": ["south", "west"],
            "south": 12,
            "west": 2,
            "visited": False
            },
        14:{"name": "City Square (south-east)",
            "description": "You’re at the south-east corner of the main square",
            "description_new":  "You see a street, going by the south side of the market.",
            "exits": ["north", "west"],
            "north": 12,
            "west": 4,
            "east": 15,
            "visited": False
            },
        15:{"name": "South Street",
            "description": "You're on a street leading to wastelands.",
            "description_new": "You pass some market stands on the left, along with few tents and shelters on the right.",
            "exits": ["east", "west"],
            "east": 16,
            "west": 14,
            "visited": False
            },
        16:{"name": "South Street (2)",
            "description": "You're on a street leading to wastelands.",
            "description_new":  "You're already close to the gates.",
            "exits": ["east", "west"],
            "east": 17,
            "west": 15,
            "visited": False
            },
        17:{"name": "Gates",
            "description": "You're at the town gates. Guard stares at you suspiciously.",
            "description_new":  """You see the town's gates, however speaking accurately, it's rather just some junk
and bags stored on one another, barricading the village from outsiders.
There's also a guard standing in front of it.""",
            "npc": npc.Guard,
            "exits": ["east"],
            "east": 16,
            "visited": False
            },

#PUB
        18:{"name": "Entrance",
            "description": "You’re close to the door. The pub seems as loud and vulgar as ever",
            "description_new":  "The whole place seems to be rather dirty and smokey, with some local drunkards, making loud toasts.\n"
                    "There are, however, some calm people, like that guy on the north corner.\n"
                    "Also the barman looks like he can spare some information about the locals.",
            "exits": ["north", "south", "east", "west"],
            "north": 19,
            "south": 22,
            "east": 11,
            "west": 23,
            "visited": False
            },
        19:{"name": "Bob's table",
            "description": "Bob smiles as you approach him. Looks like he’s been here for hours.",
            "description_new":  "You arrive at a table, occupied by a gently looking guy somewhere in his thirties, wearing a cowboy hat.",
            "npc": npc.Bob,
            "exits": ["south", "west"],
            "south": 18,
            "west": 20,
            "visited": False
            },
        20:{"name": "Empty Table",
            "description": "The table on the on the north side of the pub is empty as usual. Seems like people don’t like to sit here,\n"
                           "is something wrong with it?",
            "description_new":  "This is the only free table in the whole room. Would be a perfect place to drink, but…\n"
                                "Maybe let’s talk to some people instead.",
            "exits": ["south", "east", "west"],
            "south": 23,
            "east": 19,
            "west": 21,
            "visited": False
            },
        21:{"name": "Jack's Table",
            "description": "Drunk ass Jack shouts """"Hey, barman! Where’s mah beer?!"""", then he notices you.\n"
                           """""Oh, hi landlubberr, it’s you again!""""",
            "description_new":  "Seems like you’ve come across the loudest, most obnoxious drunkard in this place.\n"
                                "There’s however something interesting in this guy. His beard looks like he’s been hit\n"
                                "by a lightning and he’s wearing a pirate hat. A pirate hat!",
            "npc": npc.Jack,
            "exits": ["south", "east"],
            "south": 25,
            "east": 20,
            "visited": False
            },
        22:{"name": "Restrooms",
            "description": "You’re in the restrooms. Seems like it’s haven’t been cleaned for at least few days.",
            "description_new":  "",
            "exits": ["north"],
            "north": 18,
            "visited": False
            },
        23:{"name": "Middle Section",
            "description": "You’re right in the middle of the pub, surrounded by noise and cheap beer.",
            "description_new":  "You stand roght in the middle of the bar, observing all the other tables where people talk and drink beer.",
            "exits": ["north", "south", "east", "west"],
            "north": 20,
            "south": 24,
            "east": 18,
            "west": 25,
            "visited": False
            },
        24:{"name": "Bar",
            "description": "You arrive at the bar. “”””What for you?”””” - barman says.",
            "description_new":  "You see a bar with some cheap alcohol along with a tired and bored person behind it.\n"
                                "“”””How can i serve you?”””” - he asks.",
            "npc": npc.Barman,
            "exits": ["north", "west"],
            "north": 23,
            "west": 22,
            "visited": False
            },
        25:{"name": "West Wing",
            "description": "You’re on the west side of pub. You see some drunk people chanting some silly songs.",
            "description_new":  "",
            "exits": ["north", "east", "south"],
            "north": 21,
            "east": 23,
            "south": 26,
            "visited": False
            },
        26:{"name" : "Basement door",
            "description" : "You see a door leading to basement.",
            "description_new":  "You see a door at the very corner of the pub. You try to open it, but it won’t move.",
            "exits": ["north", "east"],
            "key": ["south"],
            "north": 25,
            "south": 27,
            "east": 7,
            "visited": False
            },

        27:{"name": "Basement",
            "description": "You’re in the basement.",
            "description_new":  "As you go down the stairs it gets a little bit colder. You see some boxes and barrels along mossy walls.\n"
                                "There are some bugs on the floor and you swear, that you caught a glimpse of a rat.",
            "exits": ["north", "east"],
            "north": 26,
            "east": 2,
            "visited": False
            },
        28:{"name": "Basement Chest",
            "description" : "Few bugs and an old, rotten chest.",
            "description_new":  "There's an old chest standing in front of you. Suddenly something bites your leg.",
            "enemycode": 1,
            "enemy": npc.enemies[1]["name"],
            "chest_description": "",
            "chest": ["album"],
            "exits" : ["west"],
            "west" : 27,
            "visited": False
            },

#MARKET, HOSPITAL

        29:{"name": "Market",
            "description" : "You, reach the market place. Few vendors. Kinda loud, kinda irritating.",
            "description_new":  """You see few stands with products of all sorts and some noisy guys advertising them. It seems like"
you'd be able to find basically everything, you can think of at the moment.""",
            "npc" : npc.Tradesman,
            "exits" : ["east"],
            "east" : 12,
            "visited": False
            },

        30:{"name": "Hospital",
            "description": "Broken tiles and pale walls. It still seems much cleaner and polished than everything else out here.",
            "description_new":  """Though not in perfect shape, this place still looks suprisingly clean, when compared to the rest of this city.",
you see a doctor behind a desk, doing some paperwork.""",
            "npc": npc.Doctor,
            "exits": ["south"],
            "south": 3,
            "visited": False
            },
    }
