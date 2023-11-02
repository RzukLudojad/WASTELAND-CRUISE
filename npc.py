#lista przeciwników w grze z potrzebnymi statystykami
enemies = {
    1: {"name": "Rat",
        "hp": 20,
        "attack": 0.8,
        "dexterity": 6,
        "experience": 1,
        "money": 2
        },
    2: {"name": "Giant Rat",
        "hp": 25,
        "attack": 1.2,
        "dexterity": 9,
        "experience": 3,
        "money": 5
        },
    3: {"name": "Rat King",
        "hp": 50,
        "attack": 1.5,
        "dexterity": 4,
        "experience": 5,
        "money": 10
        }
}

#klasa npc przypisuje zmienną "known" do funkcji talk
class NPC:
    known = False


    def talk (self):
        #pierwsza rozmowa z npc
        from game import player
        #zmienna określająca, czy spotkaliśmy tego npc już wcześniej
        global known
        self.known = True
        player.exp += 1
        pass
    def quest (self):
        pass

class Explorer(NPC):

    def __str__(self):
        if self.known == True:
            return "Randy"
        else:
            return "Explorer"

    def talk(self):
        super().talk(self)
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
        player.inventory.append("key")

    def quest(self):
        from game import player, game
        if "book" in player.inventory:
            print("\033[32mThank you for bringing my book back. I feel better now, we can go. Just follow me and look around for any\n"
                  "possible threat.\033[0m")
            player.inventory.remove("book")
            player.exp += 10
            global place
            global currentRoom
            player.place = 2
            player.currentRoom = 1
            game(player)
        else:
            print("\033[32mHave you found my book?\033[0m")

class Guard(NPC):

    def __str__(self):
        return "Guard"

    def talk(self):
        if "city pass" not in player.inventory:
            line = "I can't let you out unless you show me your outside pass"
            return line
        else:
            pass


class Jack(NPC):

    def __str__(self):
        return "Jack"

    def talk(self):
        super().talk(self)
        from game import player
        print("""\033[32mOh hi tharr. My name JACK! ..en am a local pirate an storytellarr. I've wandarred thrrough more cantriez,
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
"2 - Sure, let's drink. Here's your beer
"3 - Uh... I think i gotta go.""")
            choice_t = input(">")
            if choice_t == "1":
                print("""\033[32mOakaey, so de rules arr simple: I win, then you pay me for ma beer. You win, then... Well i don have
much money now, but i can give yer some special object, dat i managed to steal from the bar.
And ohhhh boooy, thrrrust me it'z worth it! Arr ya in?\n\033[0m"""
                  "\033[34m Y - Yes / N - No\033[0m")
                choice_ttt = input(">").lower()
                if choice_ttt == "y":
                    if player.money >=5:
                        self.coin()
                    else:
                        print("\033[32mOh ye little bastard! I see yer poor as heck! Come back when you have sum money to sparre!\0330m")
                if choice_ttt == "n":
                    print("COWARRD!")
                    print(options)
                    return choice_t
            elif choice_t == "2":
                if "beer" not in player.inventory:
                    print("\033[32mGrreat! In case yer blind, the barman sits right at dee south side of dis shithole. Hurrey up, comrade!\033[0m")
                    break
                else:
                    print("\033[32mOooh yeah! Cold as a frozen hell, just how i liek it! Now landlubber, let me tell you a storey about...\n\033[0m"
                          "As Jack begins to tell all his tales about distant lands and seas, your head starts to feel heavier and heavier\n"
                          "\033[32m...well, and that's how i became a pirate! You know... I like ya, stranger! You're one of the few guys\n"
                          "who don't interrupt my speech. Actually... Have this thing. Yeah, i'm giving it away, no joke. Let them know that\n"
                          "Jack's hell of a generrous arrsehole! ...I'm not sure where it fits though, but it must be some goddamn trreasure!")
                    player.inventory.append("key")

            elif choice_t == "3":
                print("\033[32mOh, another one... """"Just messin' arround"""", huh?!\033[0m")
                break

    def coin(self):
        import random, player
        toss = random.randint(1,2)
        choice = input("Choose your side (1 - heads/2 - tails")
        if choice == str(toss):
            print("\033[32mAm guess ye were lucky, landlubber! Come, take this as my bet.\033[0m")
            player.inventory.append("album")
            player.exp += 5
        else:
            print("\033[32mHah! Not this time, squeaky bastard!\033[0m")
            player.money -= 5
            player.exp += 2

class Bob(NPC):

    def __str__(self):
        return "Bob"

    def talk(self):
        super().talk(self)
        print("\033[32mHello stranger! My name's Bob, Bob Bieber to be precise. What brings you here?\033[0m")

        while True:
            print("""\n1 - I was lost in the wastelands, man named Randy brought me here.
2 - That's an interesting name you have, i think i've heard it somewhere...
3 - Oh, i'm sorry. I think i confused the tables. """)
            choice_t = input(">")
            if choice_t == "1":
                print("""\033[32mRandy!? I know this guy! We've been close friends for over 10 years. He often escorts me in the desert
and helps me find new customers and barters. 'Cause i'm a trader, you know.\033[0m""")
            elif choice_t == "2":
                print("""\033[32mWell, i've heard that my grandpa was a famous singer. I'd love to find out more about him, but it seems
that no one here knows about him. If you managed to give me some information about my grandfather, i'd
be very thankful.\033[0m""")
                print("""\n1 - Well, i've heard about your grandfather. From what i remember, he was named Rick and played some folk
and country songs in the local bars.
2 - I don't care about your grandpa! What i wanna know is some information about this place and people here.
3 - Okay, if i'll manage to find anything about your grandfather i'll share it with you straightaway!""")
                choice_t2 = input(">")
                if choice_t2 == "1":
                    print("""\033[32mYou must've confused him with someone then. My grandpa name was """"Justin"""" and i've heard that
he was something a lot bigger than just some noname playing few local gigs.\033[0m""")
                elif choice_t2 == "2":
                    print("""Hey, don't be so rude! If you want some updates on what's goin' on 'round the city, you should ask the barman.
He's the one, who's up to date with everything.""")
                    break
                elif choice_t2 == "3":
                    print("Thanks, hat means a lot to me. If you'll get to be on the trail of him, you know where to find me!")
                    print("""\n1 - Okay. I still wanna ask you some questions
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
        if "album" in player.inventory:
            print("""\033[32mOh, so that's how my grandpa looked! Great, can't wait to play it on the cd player i traded
few weeks ago for a pair of jeans. Thank you, that really means a lot to me.
Here, have this small gift as a proof of my gratitude.\033[0m""")
            player.money += 100
            player.exp += 15

class Barman(NPC):

    def __str__(self):
        return "Barman"

    def talk(self):
        print("\033[32mHello sir! You look like a newcomer. What do you want? A drink, company, information?\033[0m")

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
                self.sell(self)
            elif choice == "2":
                print("""\033[32mYou're new? Look... This town isn't anything nice, so if you just happened to think it's a 'cool place
to be around', i am sorry to break it down to you, but it's not!""")
                print("""1 - Umm... Why is that?
2 - Okay, how do i get out of here then?
3 - Okay, that's all i needed to know, thanks""")
                choice_i = input(">")
                if choice_i == "1":
                    print("""\033[32mIt's a boring ass village, with few drunkards siting right behind you, few silly vendors on the east
side of the city, and few, often severly handicapped, victims from wastelands lying in the hospital - that's in the north,
in case you haven't noticed yet. Being here for longer than a year will get you so bored, that you'll eventually turn
into a brainless zombie and just rot in here for the rest of your pointless existance. I mean...
These folks start to get crazy round here.\033[0m - he then point to a north-west corner - \033[32mSee? This guy, named Bob. He can't stop
talking about his grandpa being some kind of famous popstar. And he's probably the one who travels the most! The other guys will tell
you stories 'bout magic islands, unicorns, pirates, you name it! ... I mean it's a true nuthouse right in front of you.
Ekhem... But it's still better than dying in the wastelands, isn't it?\033[0m""")
                else:
                    print("Invalid input! Try again.")
                    return choice_i
            elif choice == "3":
                break
            elif choice == "4" and Bob.known == True:
                print("""\033[32mOh, i see you've talked to Bob, haha! He's being obsessed with his supposedly famous grandpa!
He tells this story every person he meets. Listen up, there was NEVER a famous singer named 'Bieber',
nor there ever will be. And stop believing what these maniacs tell you, or you'll start to be one of them. Frickin' popstar, hah!\033[0m""")
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

class Tradesman(NPC):

    def __str__(self):
        return "Tradesman"

    def sell(self):
        from game import player
        prices = {"club" : 20, "beer" : 3, "radio" : 15, "album" : 7}
        offer = {}
        x = 1
        for key in prices:
            if key in player.inventory:
                print(str(x) + " - " + key + ": " + str(prices[key]))
                offer.update({x : key})
                x += 1
        choice_s = input(">")
        if choice_s in offer:
            player.inventory.remove(offer[x])
            player.money += prices[offer[x]]
    def buy(self):
        from game import player
        prices = {"club" : 45, "radio" : 30, "first aid" : 10}
        offer = {}
        x = 1
        for key in prices:
            print(str(x) + " - " + key + " - " + str(prices[key]))
            offer.update({str(x): key})
            x += 1
        choice_b = input(">")
        if choice_b in offer:
            if player.money < prices[offer[choice_b]]:
                print("You don't have enough money!\n")
            else:
                player.inventory.append(offer[choice_b])
                player.money -= prices[choice_b]

    def talk(self):
        print("""\033[32mHey there, wanderer! Wanna buy something? I've got all sorts of goodies! Clubs, magazines, everything!"
I've even got a working radio!\033[0m\n""")
        while True:
            if Bob.known == False:
                print("""1 - Show me your stuff!
2 - I have some junk to spare, wanna take a look?
3 - Not really interested, bye.""")
            else:
                print("""1 - Show me your stuff!
2 - I have some junk to spare, wanna take a look?
3 - Not really interested, bye.
4 - Do you know anything about a singer named 'Bieber'?""")
            choice = input(">")
            if choice == "1":
                self.buy(self)
            elif choice == "2":
                self.sell(self)
            elif choice == "3":
                break
            elif choice == "4" and Bob.known == True:
                print("\033[32mOh, it seems like we have a Bob's friend over here! He still keeps asking everybody about his grandpa, hah!"
                  "By the way, when you see Bob, please tell him that i've got him a new jacket.\033[0m")
            else:
                print("Invalid input! Try again.")

class Doctor(NPC):
    def __str__(self):

        return "Doctor"

    def talk(self):
        print("\033[32mHello sir! How may i help you?\033[0m\n")
        while True:
            print("""1 - I need healing
2 - Can you guide me to Randy the Explorer?
3 - I was just looking around...""")
            choice = input(">")
            if choice == "1":
                print("\033[32mHere you go...\033[0m\n")
                self.heal(self)
            elif choice == "2":
                print("\033[32mYou mean the explorer? Why do you want to see him?\033[0m")
                print("""1 - He's my friend
2 - He rescued me from the wastelands few days ago
3 - I was just wondering if he's ok. He was severly wounded last time i saw him.
4 - Nevermind.""")
                choice_t = input(">")
                if choice_t == "1" or "2" or "3" or "4":
                    print("\03332mI'm sorry, but this is a DEMO VERSION. I can't let you see Randy unless you've bought the full game.\033[0m\n")
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
        hp_p = 3 * player.health + 2 * player.level






