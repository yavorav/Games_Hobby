# Defining all aspects of character creation

import data
"""
name
select weapon type, list options
start at level 1
display character stats once created
"""


###########################
def char_create(level=1):
    print(data.welcome)
    name = input(data.name_prompt + "\n")
    print("Great!")
    weapon = input(data.weapon_prompt)
    ct = 0
    while weapon.title() not in data.weapons_list[:data.weapon_unlock]:
        print(data.weapon_error)
        if ct == 3:
            print(data.weapon_reminder)
            ct = 0
        weapon = input()
        ct += 1
        
    weapon = weapon.capitalize()

    print("Great!")
    hp = 10 + (level * 2)

    print(data.character_success)
    print("Name: " + name)
    print("Weapon: " + weapon)
    print("Level: " + str(level))
    print("Get ready for your adventure, " + name + "!")
    
    return(name, weapon, level, hp)


#char_create()