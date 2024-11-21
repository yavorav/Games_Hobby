# Defining all aspects of character creation

"""
name
select weapon type, list options
start at level 1
display character stats once created
"""

welcome = "Welcome! Thank you for deciding to play The Best Game Ever. Let's get you started with a character."
name_prompt = "Please choose a character name: "
#ty = print("Great!")
weapon_prompt = "Please choose a weapon from the following:\nSword\nAxe\nFists\n"
weapon_list = ["Sword", "Axe", "Fists"]
reminder = "Reminder, your weapon choices are: Sword, Axe, and Fists"

###########################
def char_create(level=1):
    print(welcome)
    name = input(name_prompt + "\n")
    print("Great!")
    weapon = input(weapon_prompt)
    ct = 0
    while weapon.capitalize() not in weapon_list:
        print("Sorry, the weapon you chose is not an option. Please try again.")
        if ct == 3:
            print(reminder)
            ct = 0
        weapon = input()
        ct += 1
        
    weapon = weapon.capitalize()

    #if weapon.lower() not in weapon_list:
    #    print("Sorry, the weapon you chose is not an option. Please try again.")
    #    return
    #else:

    print("Great!")
    hp = 10 + (level * 2)

    print("You've successfully created a character!")
    print("Name: " + name)
    print("Weapon: " + weapon)
    print("Level: " + str(level))
    #print("Health: " + str(hp) + "HP")
    #print("\n")
    # create method within the player class to give info and that will display HP, because at the start you don't know
    print("Get ready for your adventure, " + name + "!")
    
    return(name, weapon, level, hp)


#char_create()