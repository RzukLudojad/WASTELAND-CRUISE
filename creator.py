class Player(object):

    name = ''
    strength = 0
    health = 0
    intelligence = 0
    dexterity = 0
    points = 30

    level = 1
    exp = 0
    inventory = []
    money = 0
    damage_multiplier = 1.0
    currentRoom = 1
#zmienna podmieniana w grze na lokalizację
    place = 1
#słownik zapisujący wszystkie odwiedzone przez gracza pomieszczenia
    visited_loc = {1: [], 2: []}
#lista wszystkich poznanych przez gracza npc
    npc_known = []

#lista, określająca ilość doświadczenia, potrzebnego by przejść na wyższy poziom
#klucz to poziom, a wartość mu odpowiadająca to wymagana ilość doświadczenia
    levelup = {1: 25, 2: 70, 3: 130, 4: 200}

    def __init__(self, name):
        self.name = name

#komenda __repr__ zwraca listę wszystkich atrybutów gracza wraz z informacjami o aktualnej lokacji, życiu, ekwipunku itp.
#jest wykorzystana w zapisie gry
    def __repr__(self):
        player = (self.name, str(self.strength), str(self.health), str(self.intelligence), str(self.dexterity),
                  str(self.points), str(self.level), str(self.exp), str("-".join(self.inventory)),
                  str(self.damage_multiplier), str(self.money), str(self.currentRoom), str(self.place),
                  str(self.visited_loc).replace(",", "-"),str(self.npc_known).replace(",", "-"))
        return(",".join(player))

    def __str__(self):
        player = (str(self.strength), str(self.health), str(self.intelligence), str(self.dexterity),
                  str(self.points), str(self.level), str(self.exp), str(self.inventory), str(self.damage_multiplier),
                  str(self.money), str(self.currentRoom), str(self.place))
        return(self.name +" = ["+", ".join(player)+"]")
#metoda tworzenia postaci
    def creator(self, name):
        while True:
            print("----------------------------------------\n")
            print("\nYou have", name.points, "points left.")
            print("""
      --------------------------------
      | 1 - add points               |
      | 2 - take points              |
      | 3 - see points per attribute |
      | 4 - save and exit            |
      --------------------------------
      """)
#gracz wybiera jedną z trzech opisanych powyżej opcji, wpisując cyfrę od 1 do 4
            choice_c = input("choice: ")
            if choice_c == "1":
                name.add_points()
            elif choice_c == "2":
                name.take_points()
            elif choice_c == "3":
                name.show_stats()
            elif choice_c == "4":
                if name.points > 0:
                    print("Use all your points!")

                if name.strength == 0 or name.intelligence == 0 or name.health == 0 or name.dexterity == 0:
                    print("You need to have at least 1 point in each attribute.")
                else:
                    print("Congratulations! You've succesfully made", name.name, ".\nHe has:")
                    print(name.strength, "strength")
                    print(name.health, "health")
                    print(name.intelligence, "intelligence")
                    print(name.dexterity, "dexterity")
                    save(name)
                    break

        else:
            print("Invalid choice.")

#metoda przydzielania punktów, używany zarówno w kreatorze postaci jak i również przy "levelowaniu"
    def add_points(self):

        _attributes = {"1": self.strength,
                       "2": self.health,
                       "3": self.intelligence,
                       "4": self.dexterity}

        _attribute_names = {"1": "Strength",
                            "2": "Health",
                            "3": "Intelligence",
                            "4": "Dexterity"}

        print("""
      which attribute?
      1 - strength
      2 - health
      3 - intelligence
      4 - dexterity
      ENTER - exit""")
        choice_a = str(input("choice:"))
        while choice_a in _attributes:
            try:
                print("\n" + _attribute_names[choice_a] + " - " + str(_attributes[choice_a]) + "\n")
                print("how many points?")
                add = int(input("choice:"))
            except ValueError:
                print("Invalid input!")
                return
            except choice_a == "":
                name.creator()
            else:
                if add <= self.points and add > 0:
                    self.points -= add
                    if choice_a == "1":
                        self.strength += add
                        print(self.name, "now has", self.strength, "strength points.")
                        break
                    elif choice_a == "2":
                        self.health += add
                        print(self.name, "now has", self.health, "health points.")
                        break
                    elif choice_a == "3":
                        self.intelligence += add
                        print(self.name, "now has", self.intelligence, "intelligence points.")
                        break
                    elif choice_a == "4":
                        self.dexterity += add
                        print(self.name, "now has", self.dexterity, "dexterity points.")
                        break


                else:
                    print("Invalid number of points.")

        else:
            print("invalid attribute.")

#metoda odejmowania punktów, używana w kreatorze postaci
    def take_points(self):
        _attributes = {"1": self.strength,
                       "2": self.health,
                       "3": self.intelligence,
                       "4": self.dexterity}

        _attribute_names = {"1": "Strength",
                            "2": "Health",
                            "3": "Intelligence",
                            "4": "Dexterity"}

        choice_a = str(input("""
      which attribute?
      1 - strength
      2 - health
      3 - intelligence
      4 - dexterity
      ENTER - exit"""))
        while choice_a in _attributes:
            try:
                print("\n" + _attribute_names[choice_a] + " - " + str(_attributes[choice_a]))
                print("how many points?")
                take = int(input("choice:"))
            except ValueError as valerr:
                print("Invalid data:", valerr)
                return
            except choice_a == "":
                name.creator()
            else:
                if take <= _attributes[choice_a] and take > 0:
                    self.points += take
                    if choice_a == "1":
                        self.strength -= take
                        print(self.name, "now has", self.strength, "strength points.")
                        break
                    elif choice_a == "2":
                        self.health -= take
                        print(self.name, "now has", self.health, "health points.")
                        break
                    elif choice_a == "3":
                        self.intelligence -= take
                        print(self.name, "now has", self.intelligence, "intelligence points.")
                        break
                    elif choice_a == "4":
                        self.dexterity -= take
                        print(self.name, "now has", self.dexterity, "dexterity points.")
                        break
                    else:
                        print("Invalid number of points.")
                else:
                    print("Invalid attribute.")

#wyświetlanie statystyk w kreatorze
    def show_stats(self):

        print("strength -", self.strength)
        print("health -", self.health)
        print("intelligence -", self.intelligence)
        print("dexterity -", self.dexterity)

#levelowanie
    def level_up(self):

        if self.exp >= levelup[self.level]:
            self.level += 1
            self.points += 1
            self.add_points()
#nazwanie postaci
def chose_name():
    print("\n-----------------------------\n")
    print("What's your character's name? ")

    global name
    name = input("choice:")
    name = Player(name)
    name.creator(name)

#zapis do pliku "pickle"
def save(name):
    import os, pickle
    import game
    try:
        from fight import hp_p
    except ImportError:
        hp_p = 3 * name.health + 2 * name.level
#obecna lokalizacja + folder "saves", nazwa od nazwy gracza + rozszerzenie "pkl"
    savename = (os.getcwd(), "\saves", "\\", name.name, ".pkl")
    savename = "".join(savename)
    with open(savename, "wb") as file:
#komenda repr zwracająca wszystkie atrybuty postaci (patrz wyżej)
        player_data = repr(name).split(",")
        player_data.append(hp_p)
        #player_data.append(str(game.visited_loc))
        pickle.dump(player_data, file)
#rozpoczęcie rozgrywki
    print("You've succesfully saved " + name.name + "!")
    print("""What do you want to do?
          p - continue playing
          e - exit to menu""")
    choice_save = input(">")
    if choice_save == "p":
        game.game(name)
    elif choice_save == "e":
        from main import menu
        menu()
