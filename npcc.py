#lista przeciwników w grze z potrzebnymi statystykami - reszta jest w module walki - nie ma potrzeby robić osobnej klasy
enemies = {
    1: {"name": "Rat",
        "hp": 20,
        "attack": 0.8,
        "dexterity": 6,
        "experience": 1,
        },
    2: {"name": "Giant Rat",
        "hp": 25,
        "attack": 1.2,
        "dexterity": 9,
        "experience": 3,
        },
    3: {"name": "Rat King",
        "hp": 50,
        "attack": 1.5,
        "dexterity": 4,
        "experience": 5
        }
}



class Explorer(object):
    known = False
    def __str__(self):
        if known == True:
            return("Randy")
        else:
            return("Explorer")

    def talk(self):
        global known
        from game import player
        print("Stranger slowly raises his head as you pat him on the shoulder. You realise he's in some pain as he frowns from"
              " time to time.\n")
        print("""\033[32mOh, you finally woke up... Hello, my name's Randy and i'm a local explorer, searching for possible supplies and, by occasion,
people like you - left high and dry on these wastelands. Talking of you, i've brought you here few days ago, as you were lying
somewhere in the house nearby. To be completely honest, at first i thought you were dead, but when i checed for the pulse and realised
you were breathing. What i didn't realise was that one of those horrible rats was aproaching me from behind.
I managed to get you out of there, but i was severly wounded in the process. I also dropped my book, which
- being my ancestor's legacy - is very important to me. If you managed to find it, i think i'd be able to guide you
to the city, where us both can seek some help. The town's not far away, but you need a guidance to find it
and what i need is this frickin' book! Now, take this key and go search for my book in the house. It's nearby,
if you head south, i'm sure you won't miss it. Just beware of this goddamn rat! It's bigger than one might expect.\n\033[0m""")
        known = True
        player.inventory.append("key")

    def quest(self):
        from game import player
        if "book" in player.inventory:
            print("\033[32mThank you for bringing my book back. I feel better now, we can go. Just follow me and look around for any\n"
                  "possible threat.\033[0m")
            player.inventory.pop("book")
            global location
            global currentRoom
            location = locations_new.town
            currentRoom = 1
        else:
            print("\033[32mHave you found my book?\033[0m")
class Guard(object):
    def speak(self):
        if "City Pass" not in player.inventory:
            line = "I can't let you out unless you show me your outside pass"
            return line
        else:
            pass

class Jack(object):

    def talk(self):
        from game import player
        print("""\033[47mOh hi tharr. My name JACK! ..en am a local pirate an storytellarr. I've wandarred thrrough more cantriez,
               then i can count! I'd love to tell yer a story, but it seems dat ma throat has dried out.
               If yer'd be so loveley and brought me a beer, then i can tell you some good ol' storiez!
               Umm... An if ya don't wan to, we can still play some good ol' coin toss and i'll win it from ya!\n\033[0m""")
        while True:
            if "beer" not in player.inventory:
                print("""1 - Let's play game of tic tac toe
                     2 - Ok, let's settle down for a drink, i'll be back in a second...
                     3 - Uh... I think i gotta go. """)
            else:
                print("""1 - Let's play game of tic tac toe
                     2 - Sure, let's drink. Here's your beer
                     3 - Uh... I think i gotta go. """)
            choice_t = input(">")
            if choice_t == "1":
                print("\033[47mOakaey, so de rules arr simple: I win, then you pay me for ma beer. You win, then... Well i don have\n"
                  "much money now, but i can give yer some special object, dat i managed to steal from the bar.\n"
                  "And ohhhh boooy, thrrrust me it'z worth it! Arr ya in?\n\033[0m"
                  "\033[34m Y - Yes / N - No")
                choice_ttt = input(">").lower()
                if choice_ttt == "y":
                    if player.money >=5:
                        self.game()
                    else:
                        print("\033[47mOh ye little bastard! I see yer poor as heck! Come back when you have sum money to sparre!\0330m")
                if choice_ttt == "n":
                    print("COWARRD!")
                    print(options)
                    return choice_t
            elif choice_t == "2":
                if "beer" not in player.inventory:
                    print("\033[47mGrreat! In case yer blind, the barman sits right at dee south side of dis shithole. Hurrey up, comrade!\033[0m")
                else:
                    print("\033[47mOooh yeah! Cold as a frozen hell, just how i liek it! Now landlubber, let me tell you a storey about...\n\033[0m"
                          "As Jack begins to tell all his tales about distant lands and seas, your head starts to feel heavier and heavier\n"
                          "\033[47m...well, and that's how i became a pirate! You know... I like ya, stranger! You're one of the few guys\n"
                          "who don't interrupt my speech. Actually... Have this thing. Yeah, i'm giving it away, no joke. Let them know that\n"
                          "Jack's hell of a generrous arrsehole! ...I'm not sure where it fits though, but it must be some goddamn trreasure!")
                    player.inventory.append("key")

            elif choice_t == "3":
                print("\033[47mOh, another one... """"Just messin' arround"""", huh?!\033[0m")
                break

    def game(self):
        pass

class Bob(object):
    known = False


    def talk(self):
        global known
        known = True
        print("\033[47mHello stranger! My name's Bob, Bob Bieber to be precise. What brings you here?\033[0m")
        while True:
            print("""1 - I was lost in the wastelands, man named Randy brought me here.
                     2 - That's an interesting name you have, i think i've heard it somewhere...
                     3 - Oh, i'm sorry. I think i confused the tables. """)
            choice_t = input(">")
            if choice_t == "1":
                print("""\033[47mRandy!? I know this guy! We've been close friends for over 10 years. He often escorts me in the desert
                            and helps me find new customers and barters. 'Cause i'm a trader, you know.\033[0m""")
            elif choice_t == "2":
                print("""\033[47mWell, i've heard that my grandpa was a famous singer. I'd love to find out more about him, but it seems
                             that no one here knows about him. If you managed to give me some information about my grandfather, i'd
                             be very thankful.\033[0m""")
                print(""" 1 - Well, i've heard about your grandfather. From what i remember, he was named Rick and played some folk
                            and country songs in the local bars.
                            2 - I don't care about your grandpa! What i wanna know is some information about this place and people here.
                            3 - Okay, if i'll manage to find anything about your grandfather i'll share it with you straightaway!""")
                choice_t2 = input(">")
                if choice_t2 == "1":
                    print("You must've confused him with someone then. My grandpa name was """"Justin"""" and i've heard that he was"
                      "something a lot bigger than just some noname playing few local gigs.")
                elif choice_t2 == "2":
                    print("Hey, don't be so rude! If you want some updates on what's goin' on 'round the city, you should ask the barman."
                      "He's the one, who's up to date with everything.")
                elif choice_t2 == "3":
                    print("Thanks, hat means a lot to me. If you'll get to be on the trail of him, you know where to find me!")
                    print(""" 1 - Okay. I still wanna ask you some questions
                         2 - Okay. I've gotta leave now. I'll come back when i'll get some information.""")
                    choice_t2_2 = input(">")
                    if choice_t2_2 == "1":
                        continue
                    elif choice_t2_2 == "2":
                        break
                    else:
                        print("Invalid input! Try again.")
                        return choice_t2_2
                else:
                    print("Invalid input! Try again.")
                    return choice_t2
            elif choice_t == "3":
                break
            else:
                print("Invalid input! Try again.")
    def quest(self):
        from game import player
        if "Album" in player.inventory:
            print("\033[47mOh, so that's how my grandpa looked! Great, can't wait to play it on the cd player i traded few weeks ago for a pair of jeans\n"
                  "Thank you, that really means a lot to me. Have this small gift as a proof of my gratitude.\033[0m")
            player.money += 100

class Barman(object):
    def talk(self):
        print("\033[47mHello sir! You look like a newcomer. What do you want? A drink, company, information?\033[0m")

        while True:
            if Bob.known == False:
                print("""1 - How much for a beer?
                2 - Actually i'd like to get some information about this place
                3 - Oh... It's already late, i have to go.""")
            else:
                print("""1 - How much for a beer?
                2 - Actually i'd like to get some information about this place
                3 - Oh... It's already late, i have to go.
                4 - Do you know anything about a singer named """"Bieber""""?""")
            choice = input(">")
            if choice == "1":
                print("\033[47mJust five bucks for a glass of cold, tasty beer!\033[0m")
                self.sell()
            elif choice == "2":
                print("\033[47m\033[0m")
            elif choice == "3":
                break
            elif choice == "4" and Bob.known == True:
                print("\033[47mOh, i see you've talked to Bob, haha! He's being obsessed with his supposedly famous grandpa!"
                  "He tells this story every person he meets. Listen up, there was NEVER a famous singer named """"Bieber"""","
                  "nor there ever will be.\033[0m")
                self.talk()
            else:
                print("Invalid input! Try again.")
    def sell(self):
        from game import player
        if player.money >= 5:
            print("Do you want to buy a beer? (y/n)")
            choice = input(">")
            if choice == "y":
                player.money -= 5
                player.inventory.append("beer")
            elif choice == "n":
                return talk(self)
        else:
            print("You don't have enough money!")

class Tradesman(object):

    def sell(self):
        from game import player
        prices = {"club" : 20, "beer" : 3, "radio" : 15, "album" : 7}
        offer = {}
        for key in prices:
            x = 1
            if item in prices and item in player.inventory:
                print(str(x) + key + "-" + str(prices[key]))
                offer.update({x : key})
            x+=1
        choice = input(">")
        if choice in offer:
            player.inventory.pop(offer[x])
            player.money += prices[offer[x]]
    def buy(self):
        from game import player
        prices = {"club" : 45, "radio" : 30, "first aid" : 10}
        offer = {}
        for key in prices:
            x = 1
            print(str(x) + key + "-" + str(prices[key]))
            x += 1
            offer.update({x: key})
        if choice in offer:
            player.inventory.pop(offer[x])
            player.money += prices[offer[x]]
        choice
    def talk(self):
        print("""\033[47mHey there, wanderer! Wanna buy something? I've got all sorts of goodies! Clubs, magazines, everything!"
              I've even got a working radio!\033[0m""")
        while True:
            if Bob.known == False:
                print("""1 - Show me your stuff!
                    2 - I have some junk to spare, wanna take a look?
                    3 - Not really interested, bye.""")
            else:
                print("""1 - Show me your stuff!
                    2 - I have some junk to spare, wanna take a look?
                    3 - Not really interested, bye.
                    4 - Do you know anything about a singer named """"Bieber""""?""")
            choice = input(">")
            if choice == "1":
                self.buy()
            elif choice == "2":
                self.sell()
            elif choice == "3":
                break
            elif choice == "4" and Bob.known == True:
                print("\033[47mOh, it seems like we have a Bob's friend over here! He still keeps asking everybody about his grandpa, hah!"
                  "By the way, when you see Bob, please tell him that i've got him a new jacket.\033[0m")
            else:
                print("Invalid input! Try again.")
class Doctor(object):
    def talk(self):
        print("\03347mHello sir! How may i help you?\0330m")
        while True:
            print("1 - I need healing"
              "2 - Can you guide me to Randy the Explorer?"
              "3 - I was just looking around...")
            choice = input(">")
            if choice == "1":
                print("\03347mHere you go...\0330m")
                self.heal()
            elif choice == "2":
                print("You mean the explorer? Why do you want to see him?")
                print("1 - He's my friend"
                      "2 - He rescued me from the wastelands few days ago"
                      "3 - I was just wondering if he's ok. He was severly wounded last time i saw him."
                      "4 - Nevermind.")
                choice_t = input(">")
                if choice_t == "1":
                    pass
                elif choice_t == "2":
                    pass
                elif choice_t == "3":
                    pass
                elif choice_t == "4":
                    continue
                else:
                    print("Invalid input! Try again.")
            elif choice == "3":
                break
            else:
                print("Invalid input! Try again.")
    def heal(self):
        from game import player
        from fight import hp_p
        global hp_p
        print("\03347m\0330m")
        hp_p = 3 * player.health + 2 * player.level

'''
weapon_seller
doctor
'''