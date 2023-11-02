import random, game
from npc import enemies
from game import player

exp = int(player.exp)
hp_p = round(3 * player.health + 2 * player.level, 2)


def fightorrun(enemy):
    global attack_p
    attack_p = int(player.strength) / 10 * float(player.damage_multiplier)
    enemy_chosen = enemies[enemy]
    print("------------------------------------")
    print("You\t\t\tvs\t\t" + enemy_chosen["name"])
    print("HP: " + str(hp_p) + "\t\t\t\tHP: " + str(enemy_chosen["hp"]))
    print("Damage: K20 * " + str(attack_p) + "\tDamage: K20 * " + str(enemy_chosen["attack"]))
    print("Dexterity: " + str(player.dexterity) + "\t\tDexterity: " + str(enemy_chosen["dexterity"]))
    print("------------------------------------")
    decision = input("What do you do? (f - fight, r - run)")
    if decision == "f":
        fight(enemy)

    elif decision == "r":
        run(enemy)

    else:
        print("Invalid input! You have to write 'f' or 'r' ")


def fight(enemy):
#zaimportowanie przeciwnika z listy (w module "npc")
    enemy_chosen = enemies[enemy]
    enemy_name = str("\033[31m" + str(enemy_chosen["name"]) + "\033[0m")

#życie gracza
    global hp_p
    hp = enemy_chosen["hp"]

    print("""
            -----------------------------
                        FIGHT
            -----------------------------""")

    global hp_p
    global attack_p
    global exp
    global currentRoom
#uderzenia oraz rzuty kością dla gracza oraz przeciwnika
    hit = random.randint(1, 20) * enemy_chosen["attack"]
    hit_p = random.randint(1, 20) * attack_p
    roll1 = int(hit / enemy_chosen["attack"])
    roll2 = int(hit_p / attack_p)

#walka toczy się dopóki zarówno gracz jak i przeciwnik są żywi (mają więcej niż 0 życia)
    while hp_p > 0 and hp > 0:
        hp_p = round(hp_p - hit, 2)
        print("(",enemy_name,"'s roll -", roll1, ")")
        print(enemy_name, "attacked you, taking your ", round(hit, 2), " thealh points")
        print("You have ", round(hp_p, 2), "HP\n")
        if hp_p <= 0:
            break
        else:
            hp = hp - hit_p
        print("( Your roll -", roll2, ")")
        print("You attacked enemy for ", round(hit_p, 2), " health points")
        print(enemy_name, "has ", round(hp, 2), "health points\n")

    if hp_p > 0 and hp <= 0:
        from game import location, game
        print("You won!")
        player.exp += enemy_chosen["experience"] * player.intelligence
        player.money += enemy_chosen["money"]
        print("You gained \033[32m" + str(enemy_chosen["experience"] * player.intelligence)
              + "\033[0m experience points and \033[33m" + str(enemy_chosen["money"]) + "\033[0mmoney!")
        del location[player.currentRoom]["enemy"]
        del location[player.currentRoom]["enemycode"]
        game(player)
    elif hp_p <= 0 and hp > 0:
        print("""You died.
            (PRESS ENTER TO RETURN TO MAIN MENU)""")
        while True:
            choice_d = input(">")
            if choice_d == "":
                from main import menu
                menu()
                break



#opcja ucieczki przed przeciwnikiem: gracz wybiera kierunek, w którym chce uciekać. Następnie losowane są dwa rzuty kością
#(dla gracza i dla przeciwnika) i mnożone przez statystykę zwinności dają współczynnik ucieczki. Jeśli współczynnik ucieczki
#jest większy u gracza, to udaje mu się uciec i w efekcie zostaje przeniesiony do sąsiedniego pokoju. W przeciwnym wypadku
#gracz zostaje złapany i dodatkowo traci ilość życia zdeterminowaną przez współczynnik ataku przeciwnika oraz trzeci rzut.
#Oprócz tego musi też stoczyć walkę z przeciwnikiem

def run(enemy):
    from game import location
    global currentRoom
    global hp_p
    enemy_chosen = enemies[enemy]
    enemy_name = str("\033[31m" + str(enemy_chosen["name"]) + "\033[0m")
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

#zapytanie gracza o to, w którą stronę chce uciekać
    print("\nWhere do you wanna run?", location[player.currentRoom]["exits"], "\n")
    direction = input(">")
#sprawdzenie czy gracz wpisał właściwy kierunek
    if direction not in location[player.currentRoom]["exits"]:
        print("You can't go that way!")
        return direction
    else:
        player_run = roll1 * player.dexterity
        enemy_run = roll2 * enemy_chosen["dexterity"]

        print("\nYour roll:", roll1, "*", player.dexterity, "dexterity =", player_run)
        print(enemy_name,"'s roll:", roll2, "*", enemy_chosen["dexterity"], "dexterity =", enemy_run)

    #jeśli ucieczka się nie powiedzie tj. przeciwnik będzie miał wyższy współczynnik ucieczki od gracza
        if enemy_run >= player_run:
        #trzeci rzut, determinujący utratę życia
            roll3 = random.randint(1, 20)
            hp_p -= roll3 * enemy_chosen["attack"]
            print(enemy_name.upper(), "CATCHED YOU! YOU LOSE", round(roll3 * enemy_chosen["attack"], 2), "HP")
        #walka
            fight(enemy)
    #w razie udanej ucieczki
        else:
    #przeniesienie postaci do sąsiedniego pokoju (w wybranym przez gracza kierunku)
            print("Succesful escape!")
            player.currentRoom = rooms[player.currentRoom][direction]
            print("""\n\033[34m(TIP: If the enemy seems too strong for you, make sure to search other rooms,
as there may be some weapon hidden somewhere)\033[0m\n""")
    game.game(showStatus())

