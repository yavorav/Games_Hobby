
import char_create as cc
import char_player as char_player
import data as data
import random

# Calls to create a character

name = "Daisy"
weapon = "Sword"
level = 1
hp = (level * 2) # +10  ---removed to speed up debugging. whole line removed when running

#name, weapon, level, hp = cc.char_create()
player = char_player.Player(name, weapon, level, hp)
weapon = data.Weapon(weapon)

print("---------------")

def play_game():
    health = player.health()
    print(data.instructions)

    while health > 0:
        #print("---------------")
        text = input("\nWhat would you like to do now?\n")

        if text.lower() == "info":
            player.info()

        elif text.lower() == "help":
            print(data.help_text)

        elif text.lower() == "quit":
            print("Bye bye, thanks for playing!")
            return
        
        elif text.lower() == "weapons":
            # Can choose to change weapon
            print("The weapons you have available are: ")
            if player.level < 3:
                for i in range(3):
                    print(data.weapons_list[i])
            elif player.level >= 3:
                for i in range(5):
                    print(data.weapons_list[i])
            print("Would you like to change your weapon from: " + str(player.weapon) + "?")
            x = ""
            while x != "quit":
                x = input().lower()
                if x == "y" or x == "yes":
                    
                    # change weapon
                    print("What weapon would you like to choose?")
                    select = input().capitalize()
                    
                    y = int
                    if player.level >= 3:
                        y = 5
                    else:
                        y = 3

                    while select not in data.weapons_list[:y]:
                        if select == "Quit":
                            break
                        print("Sorry that weapon is not in the list. Please try again.")
                        select = input().capitalize()

                    if select == "Quit":
                        break

                    if select == player.weapon:
                        print("You're already wielding this weapon, no change made.")
                        break

                    player.weapon = select
                    print(f"Weapon changed. You are now wielding {player.weapon}.")
                    new_weapon = data.Weapon(player.weapon)
                    new_weapon.info()
                    break
                    # when choosing then have to update player.weapon, and weapon.Weapon choice, to have correct weapon damage data...
                
                elif x == "n" or x == "no":
                    # print keeping weapon whatever
                    print("Weapon did not change.")
                    break

                elif x != "quit":
                    print("Please try again.")

        elif text.lower() == "fight":
            # Choose a monster to fight
            print(data.monster_intro)
            for i in range(len(data.monster_list)):
                print(data.monster_list[i])
                #can i remove the monsters that you've fought already? forcing you to fight each of the monsters?

            mons = input().capitalize()
            
            fighting = True
            while fighting == True: # while in the fight menu
                turn = ""
                player_weapon = data.Weapon(player.weapon)
                
            
                if mons == "Run":
                    print("Coward...")
                    break
                elif mons not in data.monster_list:
                    print("Sorry, that's not one of the monsters in front of you. Please try again.")
                    mons = input().capitalize()
                else:
                    monster = data.Monster(mons)
                    monster_weapon = data.Weapon(monster.weapon)
                    if monster.boss == True:
                        print(data.boss_fight)

                    print(data.monster_intro2 + str(monster.name) + ". ")
                    print(data.monster_help)
                    
                    while turn != "quit":
                        turn = input().lower()
                        if turn == "attack":
                            # attack
                            print("Attacking...")
                            monster.hit(player_weapon.damage)
                            if monster._hp > 0:
                                player.hit(monster_weapon.damage)
                                if player._hp <= 0: 
                                    print(monster.name + " killed you. Better luck next time.")
                                    return
                            elif monster._hp <= 0:
                                print(data.monster_killed)
                                if monster.boss == True:
                                    print(data.boss_win + monster.name + "!")
                                    print(data.winscreen)
                                    return
                                #level up
                                player.level += 1
                                #regain health to new max
                                player._hp = 10 + (player.level * 2)
                                # exit back to 'main menu'
                                print("---------------")
                                print(data.level_up)
                                print(data.hp_up)
                                print("---------------")
                                fighting = False
                                break
                            
                        elif turn == "info":
                            player.info()
                        elif turn == "monster":
                            monster.info()
                        elif turn == "help":
                            print(data.monster_help)
                        elif turn == "run":
                            if monster.boss == True:
                                print(data.boss_run)
                            else:
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
