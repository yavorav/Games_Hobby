# this file contains all of the weapon data and monster data
# defined static info, but also class structure bc all weapons and monsters will have similar attributes to each other

# Character creation text
welcome = "Welcome! Thank you for deciding to play The Best Game Ever. Let's get you started with a character."
name_prompt = "Please choose a character name: "
weapon_prompt = "Please choose a weapon from the following:\nFists\nAxe\nSword\n"
weapon_unlock = 3
weapon_reminder = "Reminder, your weapon choices are: Fists, Axe, and Sword"
weapon_error = "Sorry, the weapon you chose is not an option. Please try again."
character_success = "You've successfully created a character!"


# Main game text
"""
What if the 'main menu' area is like a city? and you have the options of 
tavern, weapons shop/blacksmith, inn to rest. Still have options for help and quit obviously
And obviously the go fight monsters option.

>> could be like the 'dating sim' in that fighting monsters gains you honour and depending on how
much honour you have people might interact with you differently?
depends if i want to lean into the dialogue tree thing and give options for dialogue, or if more
honour would just unlock more menu options, like how I unlocked more weapons at level 3 style of thing

>> should levels be XP based...? that different monsters give different amounts of XP to level up, or keep it milestone
based and level with each monster??
OMG what if after killing Chthulu it unlocks the next area of the game and now you're a 'mighty adventurer' that
shows up to town and it turns into a dating sim game lmao, partially based on how you killed the boss ie. what weapon and level you were at

"""


# welcome to Summerstorm City, Steelcrest City, Riverfair City, The City of Coldburn
# The Copper Triangle Tavern

# menu options
menu_info = "info"
menu_help = "help"
menu_quit = "quit"
menu_weapons = "blacksmith" # weapons menus
menu_fight = "fight" # still option to go fight monsters
menu_tavern = "tavern" # place to heal? or just eat and chat? buy stuff

instructions = "Welcome to Summerstorm City! Your keyboard commands are", menu_info, menu_help, menu_weapons, menu_tavern, menu_fight, "and", menu_quit, ". Good luck!"
what_next = "\nWhat would you like to do now?\n"


help_text = "Your keyboard commands are:\nweapons - allows you to change weapons\nfight - takes you to the monsters\nhelp - will remind you of the commands\ninfo - will show you your character stats\nquit - will exit the game"
error_text = "Sorry, I don't understand that command. Try typing 'help' if you don't remember the commands available."
quit_text = "Bye bye, thanks for playing!"

# Blacksmith text
blacksmith_welcome = "Welcome to Belly Fires smithy! Name's Oryk, what can I do for you?"
blacksmith_options = "Weapon Stats      Change Weapon       Upgrade Weapon"
blacksmith_stats = "stats"
blacksmith_stats_text = "Let's see here, looks like you've got a"
blacksmith_change = "change"
blacksmith_change_text = "Sure, let's see what else we got for ya."
blacksmith_upgrade = "upgrade"
blacksmith_upgrade_text = ""

# Tavern text

monster_intro = "You head out to slay monsters. Before you are several monsters, please choose which you'd like to fight first: "
boss_fight = "---------------\nBOSS FIGHT\n---------------"
boss_run = "There's no running from a boss fight! Get in there and fight!"
monster_intro2 = "You approach the "
monster_help = "Commands for combat are 'attack' or 'run.' You can check your HP with 'info' and the monsters HP with 'monster'."
monster_killed = "Congrats, you killed the "
level_up = "You leveled up."
hp_up = "Your max HP increased by 2 and you healed to full."
boss_win = "You successfully killed the boss and beat the game!"
winscreen = "---------------\nThank you for playing The Best Game Ever!!\nI hope you enjoyed it.\n\nCreated by Yavora, 2024\n---------------"


# monster dictionary, name:[description, weapon, Boss? Boolean, HP]
# assign levels to monsters, create list of monsters equal to and below your level
# When you go to fight monsters it randomly selects one of your level or lower
# Will need a much larger selection of monsters, or different levels of each monster,
# could randomize both the level they appear at and which monster you get
monsters = {
    "Troll" : ["A large hairy monster often found under bridges.", "Club", False, 8],
    "Zombie" : ["A putrid undead creature.", "Claws", False, 10], 
    "Vampire" : ["An undead that only comes out at night", "Fangs", False, 12], 
    "Chthulu" : ["An unspeakable nightmare.", "Unknown", True, 20]
    }
monster_list = list(monsters.keys())

# weapon dictionary, name: [description, damage, crit rate, crit bonus]
weapons = {
    "Fists" : ["I think I came underprepared...", 1, 0.1, 1],
    "Axe" : ["Am I cutting wood or fighting bad guys?", 1, 0.2, 1],
    "Sword" : ["A trusty classic weapon.", 1, 0.25, 1],
    "Great Axe" : ["Okay this is definitely a weapon.", 1.5, 0.45, 1],
    "Greatsword" : ["Wow, now this is a real sword.", 1.5, 0.5, 1],
    "Club" : ["A big hunk of wood.", 1, 0, 0],
    "Claws" : ["Yikes those don't look clean.", 1, 0.1, 0.5],
    "Fangs" : ["Please don't come that close to me.", 1, 0.1, 0.5],
    "Unknown" : ["I'm... I'm not sure how to describe what I'm looking at...", 1, 0.25, 2]
    }
weapons_list = list(weapons.keys())

class Monster:
    def __init__(self, name):
        self.name = name
        stats = monsters[self.name]
        self.description = stats[0]
        self.weapon = stats[1]
        self.boss = stats[2]
        self._hp = stats[3]


    # weapon from library based on name
    # HP from library based on name

    def hit(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
        print(f"You hit the monster for {dmg}HP, it has {self._hp}HP remaining")
        if self._hp == 0:
            print("Monster killed!")

    def info(self):
        print("Monster information for: " + str(self.name))
        print("---------------")
        print(self.description)
        print("Current HP: " + str(self._hp))
        print("---------------")

#[description, damage, crit rate, crit bonus]
class Weapon:
    def __init__(self, name):
        self.name = name
        stats = weapons[self.name]
        self.description = stats[0]
        self.damage = stats[1]
        self.crit_rate = stats[2]
        self.bonus = stats[3]

    def info(self):
        print("Weapon information for: " + str(self.name))
        print("---------------")
        print(self.description)
        print("Damage: " + str(self.damage))
        print("Crit Chance: " + str(self.crit_rate * 100) + "%")
        print("Crit Bonus Damage: " + str(self.bonus))


