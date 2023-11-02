#zwiększenie obrażeń jeśli w ekwipunku gracza znajduje się broń


def game(name):
    import locations
    global player
    player = name


    #wczytanie lokacji na podstawie zmiennej "place"
    global location
    if player.place == 2:
        location = locations.town
    else:
        location = locations.desert

    for key in location:
        #oznaczenie wszystkich lokacji z listy 'visited' jako odwiedzone (w mapie pomieszczeń)
        if key in player.visited_loc[player.place]:
            location[key]["visited"] = True

    #zmienna określająca, czy po ostatniej komendzie nastąpił ruch pomiędzy pomieszczeniami,
    # ma wpływ na wyświetlane informacje (showStatus/halfStatus)
    global moved
    moved = True
    #global hp_p

    def showInstructions():
    #podręczna lista komend, wyświetlana na początku rozgrywki
        print("""------------------------------------
        \033[32mWASTELAND CRUISE\033[0m
------------------------------------
    \033[36m'go [direction]'
    'get [item]'
    'talk'\033[0m - talk to an npc (if there's any)
    \033[36m'char'\033[0m - player information
    \033[36m'instr'\033[0m - this panel
    \033[36m'help'\033[0m - full 'help' panel
    \033[36m'save'\033[0m - save
------------------------------------""")

    def showChar():
        # wyświetla informacje na temat stanu naszej postaci oraz obecnej lokacji
        from fight import hp_p
        status = (""" \nName: {0}
    Level: {1}
    Points: {2}\tExp: {3}/{4}
    HP: {5}\t\tMoney: {6}
    Inventory: {7}
    S: {8} H: {9} I: {10} D: {11}
                  """).format(player.name, str(player.level), str(player.points), str(player.exp),
                              str(player.levelup[player.level]), str(hp_p), str(player.money), str(player.inventory),
                              str(player.strength), str(player.health), str(player.intelligence), str(player.dexterity))
        print(status)

    def showStatus():
    #wyświetla informacje na temat stanu naszej postaci oraz obecnej lokacji
        from fight import fightorrun
    #gracz
        showChar()
    #lokacja
        print("---------------------------\n")
        print("You are in the " + location[player.currentRoom]["name"] + "\n\n")
    #opis różni się w zależności od tego, czy gracz po raz pierwszy odwiedza dane miejsce
        if location[player.currentRoom]["visited"] == True:
            print(location[player.currentRoom]["description"])
        elif location[player.currentRoom]["visited"] == False:
            print(location[player.currentRoom]["description_new"])
        print("\n\nExits: " + ", ".join(map(str, location[player.currentRoom]["exits"])))
    #informacja o sposobie otwieranie drzwi kluczem (komenda "key")
        if "key" in location[player.currentRoom]:
            print("\nLocked door: " + ", ".join(map(str, location[player.currentRoom]["key"])))
            if "key" in player.inventory:
                print("\033[34m(TIP: write 'key' to open the door)\033[0m")
    #informacja o NPC (wyświetlana na turkusowo)
        if "npc" in location[player.currentRoom]:
            person = (location[player.currentRoom]["npc"])
            print("You see \033[36m" + person.__str__(person) + "\033[0m")
    #informacja o przedmiotach "leżących" w danym pomieszczeniu
        if "item" in location[player.currentRoom]:
            print("You see a \033[35m" + str(location[player.currentRoom]["item"]) + "\033[0m")
    #informacja o przeciwnikach
        if "enemy" in location[player.currentRoom]:
            print("You see \033[31m" + location[player.currentRoom]["enemy"] + "\033[0m")
            fightorrun(location[player.currentRoom]["enemycode"])
        print("\n---------------------------")



    def halfStatus():
    # skrócona wersja funkcji "showStatus", używana gdy gracz po wpisaniu komendy pozostaje w tym samym pomieszczeniu
    # (np. po rozmowie z npc) - oglądanie opisu lokacji po każdej rozmowie z npc, bądź po każdym podniesieniu przedmiotu
    # mogłoby być dla gracza irytujące
        print("---------------------------")
        print("You are in the " + location[player.currentRoom]["name"] + "\n")
        print("Exits: " + ", ".join(map(str, location[player.currentRoom]["exits"])))
        print("Inventory :" + str(player.inventory))
        if "key" in player.inventory:
            print("Locked door: " + ", ".join(map(str, location[player.currentRoom]["key"])))
            print("\n\033[34m(TIP: write 'key' to open the door)\033[0m")
        if "item" in location[player.currentRoom]:
            print("Item: \033[35m" + str(location[player.currentRoom]["item"]) + "\033[0m")

    #POCZĄTEK GRY
    showInstructions()

    while True:
    #jeśli gracz posiada broń (w tym wypadku pałkę) to jego mnożnik obrażeń odpowiednio się zwiększa
        if "club" in player.inventory:
            global damage_multiplier
            player.damage_multiplier = 2.0
    #wykrycie czy po poprzedniej komendzie gracz ruszył się pomiędzy pomieszczeniami i na tej podstawie wyświetlenie właściwych informacji
        if moved == True:
        #dodanie obecnej lokacji do listy odwiedzonych lokacji (w celach zapisu)
            if location == locations.desert:
                player.visited_loc[1].append(player.currentRoom)
            elif location == locations.town:
                player.visited_loc[2].append(player.currentRoom)

            showStatus()
        #oznaczenie lokacji jako 'odwiedzona'
            location[player.currentRoom]["visited"] = True
        #regeneracja zdrowia
            from fight import hp_p
        else:
            halfStatus()

    #zmiana statusu lokacji na odwiedzoną
        location[player.currentRoom]["visited"] = True

    #gracz wpisuje komendę (jedno lub dwuczłową)
        move = input(">").lower().split()

        global currentRoom
    #w przypadku gdy pierwszy człon komendy to "go", gra sprawdza czy drugi człon odpowiada któremuś z elementów
    #listy "exits" dla pomieszczenia, w którym znajduje się gracz

        if move[0] == "go":
            moved = True

            if "key" in location[player.currentRoom] and move[1] in location[player.currentRoom]["key"]:
                print("The door is locked.")
                moved = False
            elif move[1] in location[player.currentRoom]["exits"]:
                player.currentRoom = location[player.currentRoom][move[1]]
            else:
                print("You can't go that way!")
    #w przypadku gdy gracz wpisze komendę "talk", gra sprawdza czy w pomieszczeniu znajduje się npc, a w przypadku gdy tak jest
    #uruchamia metodę "talk()" danego npc
        elif move[0] == "talk":
            moved = False
            if "npc" in location[player.currentRoom]:
                char = location[player.currentRoom]["npc"]
                if char.known == False:
                #dodanie npc do listy poznanych postaci
                    player.npc_known.append(char.__str__(char))
                    char.talk(char)
                    print(player.npc_known)
                else:
                    char.quest(char)
            else:
                print("There is no one to talk to!")
    #jeśli pierwszym członem komendy jest "get", to gra sprawdza czy w pomieszczeniu znajduje się przedmiot o wpisanej przez
    #gracza nazwie i jeśli tak jest to dodaje ów przedmiot do ekwipunku
        elif move[0] == "get":
            moved = False
            if "item" in location[player.currentRoom] and move[1] in location[player.currentRoom]["item"]:
                player.inventory += [move[1]]
                print(move[1] + " got!")
                del location[player.currentRoom]["item"]
            else:
                print("Can't get " + move[1] + "!")
    #jeśli użyta została komenda "key", gra sprawdza czy gracz posiada w ekwipunku klucz oraz czy w pomieszczeniu znajdują się
    #drzwi do odblokowania, a następnie odblokowuje drzwi poprzez dołączenie listy "key" do listy "exits"
        elif move[0] == "key":
            moved = False
            if "key" in player.inventory and "key" in location[player.currentRoom]:
                location[player.currentRoom]["exits"] = location[player.currentRoom]["exits"] + (location[player.currentRoom]["key"])
                location[player.currentRoom]["key"].pop()
                player.inventory.remove("key")
                print("Door successfully unlocked!\n")
            else:
                print("There are no locked doors here!")
    #jeśli w pokoju znajduje się skrzynia, to gracz może ją otworzyć i zebrać jej zawartość
        elif move[0] == "chest":
            moved = False
            if "chest" in location[player.currentRoom]:
                print("Chest contains:" + location[player.currentRoom]["chest"])
                print("\033[34m(TIP: write 'get' to get all loot from chest)\033[0m")
                choice = input(">")
                if choice == "get":
                    player.inventory.append(location[player.currentRoom]["chest"])
            else:
                print("There's no chest here!")

    #jeśli komenda to "save", następuje zapis gry
        elif move[0] == "save":
            moved = False
            import creator
            creator.save(name)

        elif move[0] == "char":
            moved = False
            showChar()
    #wyświetlenie skróconych instrukcji
        elif move[0] == "instr":
            moved = False
            showInstructions()

    #pełny samouczek/pomoc/poradnik
    #(nie mogłem zaimportować funkcji z menu, z powodu pętli 'while', która się tam znajduje)
        elif move[0] == "help":
            moved = False
            help = open("help.txt", "r")
            lines = help.read()
            print(lines)
            help.close()
            choice_h = input("\n\n\t\tEXIT (enter)\n")
            if choice_h == "":
                game(name)
