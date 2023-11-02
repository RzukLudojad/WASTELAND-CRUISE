import creator

def menu():
#słownik przypisujący danemu kluczowi funkcję, którą uruchamia
    options = {
        'g': creator.chose_name,
        'l': load_game,
        'h': help,
        'e': ""
    }

    while True:
        print("""
------------------------
    \033[32mWASTELAND CRUISE\033[0m
------------------------

    NEW GAME  (g)
    LOAD GAME (l)
    HELP      (h)
    EXIT      (e)
        """)
        choice_m = input(">")
        choice_m = choice_m.lower()

#po wpisaniu klucza ze słownika "options" uruchamiana jest odpowiadająca mu funkcja
        if choice_m not in options.keys():
            print("Invalid input! Try again")
        else:
            for letter in options.keys():
                print("\033[2J")
                return options[choice_m]()
                break

#pomoc/samouczek
def help():
    help = open("help.txt", "r")
    lines = help.read()
    print(lines)
    help.close()
    choice_h = input("\n\n\t\tEXIT (enter)\n")
    if choice_h == "":
        menu()

#wczytanie gry
def load_game():
    import glob, os, pickle
#lista dostępnych zapisów
    files = []
#numery zapisów
    filenumber = {}
#obecna lokalizacja + folder "saves"
    saves = (os.getcwd(), "\saves")
    saves = "".join(saves)
#numer zapisu
    x = 1
#wyszukanie wszystkich plików w folderze "saves" z rozszerzeniem "pickle"
    for file in glob.glob(saves+"\*.pkl"):
        print(str(x)+" - ", end="")
        print(file.replace(saves+"\\","").replace(".pkl",""))
        files.append(file)
        filenumber.update({(str(x),file)})
        x += 1
    if len(files) == 0:
        print("There are no saves.")
    print("Press ENTER to return")

    choice_l = input("Choice:")
    if choice_l in filenumber:
        from creator import Player
        global name
    #załadowanie wybranego pliku pkl (zapisu)
        load = filenumber[choice_l]
        with open(load,"rb") as save_file:
            game_state = pickle.load(save_file)
            print(game_state)
            name = game_state[0]
            global player
        #stworzenie gracza o nazwie z pliku
            player = Player(name)
        #wczytanie statystyk gracza (wraz z informacjami o obecnej lokacji, ekwipunku itp. oraz zapisanie ich do instancji "player"
            global strength
            global health
            global wisdom
            global dexterity
            global points
            global level
            global exp
            global inventory
            global damage_multiplier
            global hp_p
            global money
            global currentRoom
            global place
            player.strength = int(game_state[1])
            player.health = int(game_state[2])
            player.intelligence = int(game_state[3])
            player.dexterity = int(game_state[4])
            player.points = int(game_state[5])
            player.level = int(game_state[6])
            player.exp = int(game_state[7])
            if len(game_state[8]) == 0:
                player.inventory = []
            else:
                player.inventory = list(game_state[8].split("-"))
            player.damage_multiplier = float(game_state[9])
            player.money = int(game_state[10])
            player.currentRoom = int(game_state[11])
            player.place = int(game_state[12])
            global hp_p
            global visited_loc
            global npc_known
            import ast
            loc_visited = game_state[13].replace("-", ",")
            visited_loc = ast.literal_eval(loc_visited)
            known_npc = game_state[14].replace("-", ",")
            npc_known = ast.literal_eval(known_npc)
            hp_p = float(game_state[15])
            from game import game
            game(player)
    elif choice_l == "":
        menu()
    else:
        print("Invalid input! Try again")
        return load_game()

menu()
