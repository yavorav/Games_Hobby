
import char_create as cc
import char_player as char_player
import data as data
import random

# Calls to create a character
"""
name = "Daisy"
weapon = "Sword"
level = 1
hp = 10 + (level * 2)
"""
name, weapon, level, hp = cc.char_create()
player = char_player.Player(name, weapon, level, hp)
weapon = data.Weapon(weapon)

print("---------------")

def play_game():
    health = player.health()
    print(data.instructions)

    while health > 0:
        print("you are playing the game")
        text = input("What would you like to do now?\n")

        if text.lower() == "info":
            player.info()
        elif text.lower() == "help":
            print(data.help_text)
        elif text.lower() == "quit":
            print("Bye bye, thanks for playing!")
            return
        elif text.lower() == "weapons":
            # Can choose to change weapon
            # weapons[0,2] => weapons[0,4] inclusive
            # if level >= 3 then has access to Great weapons (needed for boss fight)
            print("The weapons you have available are: ")
            if player.level < 3:
                for i in range(3):
                    print(data.weapons_list[i])
            elif player.level >= 3:
                for i in range(5):
                    print(data.weapons_list[i])
            print("Would you like to change your weapon from: " + str(player.weapon) + "?")
            x = input()
            if x.lower() == "y":
                # change weapon
                print("Weapon changed.")
                # when choosing then have to update player.weapon, and weapon.Weapon choice, to have correct weapon damage data...


            elif x.lower() == "n":
                # print keeping weapon whatever
                print("Weapon did not change.")


            else:
                print("Please try again.")

        elif text.lower() == "fight":
            # Choose a monster to fight
            print(data.monster_intro)
            for i in range(len(data.monster_list)):
                print(data.monster_list[i])
            mons = input().capitalize()
            
            while True: # while in the fight menu
                turn = ""
                if mons == "Run":
                    print("Coward...")
                    break
                elif mons not in data.monster_list:
                    print("Sorry, that's not one of the monsters in front of you. Please try again.")
                    mons = input().capitalize()
                else:
                    monster = data.Monster(mons)
                    print(data.monster_intro2 + str(monster.name) + ". ")
                    print(data.monster_help)
                    
                    while turn != "run":
                        turn = input().lower()
                        if turn == "attack":
                            # attack
                            print("Attacking...")
                            monster.hit()
                            if monster._hp > 0:
                                player.hit()
                                if player._hp <= 0: 
                                    print(monster.name + " killed you. Better luck next time.")
                                    return
                            elif monster._hp <= 0:
                                print(data.monster_killed)
                                #level up
                                #regain health to new max
                                # exit back to 'main menu', breaking these two while loops?
                            #break
                        #break

                        elif turn == "info":
                            player.info()
                        elif turn == "monster":
                            monster.info()
                        elif turn == "help":
                            print(data.monster_help)
                        elif turn == "run":
                            print("Running...")
                            break
                        else:
                            print("Sorry I don't understand that. Please try again.")
                    
                if turn == "run":
                    break
                    

            # turn based fight mechanics....

            # if not dead, heal back to full
                # only if you win the fight

        else:
            print(data.error_text)

    

    

#player.info()

"""
q = random.random()
print(q)
if q >= 0.75:
    print("Critical Hit!")
else:
    print("Hit!")
"""
play_game()
