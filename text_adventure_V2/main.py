
import char_create as cc
import char_player as char_player
import data as data
import random

# Calls to create a character

name = "Daisy"
weapon = "Sword"
level = 1
hp = (level * 2)  +10 

#name, weapon, level, hp = cc.char_create()
player = char_player.Player(name, weapon, level, hp)
weapon = data.Weapon(weapon)

print("---------------")

def play_game():
    health = player.health()
    print(data.instructions)
    current_monster = data.Monster(data.monster_list[0])

    while health > 0:
        #print("---------------")
        text = input(data.what_next)

        if text.lower() == data.menu_info:
            player.info()

        elif text.lower() == data.menu_help:
            print(data.help_text)

        elif text.lower() == data.menu_quit:
            print(data.quit_text)
            return
        
        elif text.lower() == data.menu_weapons:
            # Can choose to change weapon
            print(data.blacksmith_welcome)
            print(data.blacksmith_options)
            x = ""
            while x != data.menu_quit:
                x = input().lower()
                if x == data.blacksmith_stats:
                    print(data.blacksmith_stats_text, player.weapon)
                    old_weapon = data.Weapon(player.weapon)
                    old_weapon.info()
                    # after printing info it takes you back to the blacksmith menu. Shoul we ask if you need anything else?
                elif x == data.blacksmith_change:
                    print(data.blacksmith_change_text)
                    if player.level < 3:
                        for i in range(3):
                            print(data.weapons_list[i])
                    elif player.level >= 3:
                        for i in range(5):
                            print(data.weapons_list[i])
                    #y = input().title()

                    pass
                elif x == data.blacksmith_upgrade:

                    pass
                elif x == data.menu_quit:
                    break
                elif x != "quit":
                    print("Please try again.")
                
            """
            print("The weapons you have available are: ")
            if player.level < 3:
                for i in range(3):
                    print(data.weapons_list[i])
            elif player.level >= 3:
                for i in range(5):
                    print(data.weapons_list[i])
            
            old_weapon = data.Weapon(player.weapon)
            old_weapon.info()
            print("Would you like to change your weapon from: " + str(player.weapon) + "?")
            x = ""
            while x != "quit":
                x = input().lower()
                if x == "y" or x == "yes":
                    
                    # change weapon
                    print("What weapon would you like to choose?")
                    select = input().title()
                    
                    y = int
                    if player.level >= 3:
                        y = 5
                    else:
                        y = 3

                    while select not in data.weapons_list[:y]:
                        if select == "Quit":
                            break
                        print("Sorry that weapon is not in the list. Please try again.")
                        select = input().title()

                    if select == "Quit":
                        break

                    if select == player.weapon:
                        print("You're already wielding this weapon, no change made.")
                        break

                    player.weapon = select
                    print(f"Weapon changed. You are now wielding {player.weapon}.")
                    #update player.weapon
                    new_weapon = data.Weapon(player.weapon)
                    new_weapon.info()
                    break
                    # when choosing then have to update player.weapon, and weapon.Weapon choice
                
                elif x == "n" or x == "no":
                    # print keeping weapon whatever
                    print("Weapon did not change.")
                    break

                elif x != "quit":
                    print("Please try again.")

            """    

        elif text.lower() == data.menu_fight:
            # Choose a monster to fight
            print(data.monster_intro)
            for i in range(len(data.monster_list)):
                print(data.monster_list[i])
                

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
                    #if you go back to the same monster, should keep it's HP
                    if mons == current_monster.name:
                        #if it's the same, use the same
                        monster = current_monster
                    else:
                        # if it's not the same, create the new object, and reassign global current_monster to compare to next time
                        monster = data.Monster(mons)
                        current_monster = monster

                    monster_weapon = data.Weapon(monster.weapon)
                    if monster.boss == True:
                        print(data.boss_fight)

                    print(data.monster_intro2 + str(monster.name) + ". ")
                    print(data.monster_help)
                    
                    monster_selected = True
                    while monster_selected == True:
                        turn = input().lower()
                        if turn == "attack":
                            # attack
                            print("Attacking...")
                            
                            #calculate player crit bonus
                            player_crit_roll = random.random()
                            if player_crit_roll >= (1 - player_weapon.crit_rate):
                                player_crit = player_weapon.bonus
                                print("Critical hit!")
                            else:
                                player_crit = 0

                            player_dmg = player_weapon.damage + player_crit
                            # deal total damage from player
                            monster.hit(player_dmg)

                            # if monster still alive
                            if monster._hp > 0:
                                
                                # calculate monster damage
                                monster_crit_roll = random.random()
                                if monster_crit_roll >= (1 - monster_weapon.crit_rate):
                                    monster_crit = monster_weapon.bonus
                                    print(f"The {monster.name} landed a critical hit!")
                                else:
                                    monster_crit = 0
                                monster_dmg = monster_weapon.damage + monster_crit

                                # deal total damage from monster
                                player.hit(monster_dmg)

                                # if player dies, end game
                                if player._hp <= 0: 
                                    print(monster.name + " killed you. Better luck next time.")
                                    return
                                
                            # if monster dies    
                            elif monster._hp <= 0:
                                print(data.monster_killed + monster.name + ".")
                                # if monster killed was boss, win screen, end game
                                if monster.boss == True:
                                    print(data.boss_win)
                                    print(data.winscreen)
                                    return
                                #level up
                                player.level += 1
                                #regain health to new max
                                player._hp = 10 + (player.level * 2)
                                
                                print("---------------")
                                print(data.level_up)
                                # If level 3, let player know access to weapons increased
                                if player.level == 3:
                                    print("You now have access to more weapons.")
                                print(data.hp_up)
                                print("---------------")
                                # Remove dead monster from list
                                data.monster_list.remove(monster.name)
                                # exit back to 'main menu'
                                fighting = False
                                break
                            
                        elif turn == "info":
                            # display both HP instead. preference choice on how it's displayed. chose to add current HP to attacks
                            #display = f"""
#---------------
#{player.name} health: {player._hp}
#{monster.name} health: {monster._hp}
#---------------"""
                            #print(display)
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
                                monster_selected = False
                                break
                                
                        else:
                            print("Sorry I don't understand that. Please try again.")
                    
                if turn == "run":
                    break
                    

        else:
            print(data.error_text)

    
play_game()


#text_var = """
#this is a tester
#unclear if i can format text to print like this
#    with a tab too
#"""
#print(text_var)