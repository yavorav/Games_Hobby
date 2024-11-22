# this file will contain all of the weapon data and monster data
# defined static info, but also class structure bc all weapons and monsters will have similar attributes to each other

instructions = "Welcome to the game, your keyboard commands are 'weapons', 'fight', 'help', 'info', 'quit'. Good luck!"
help_text = "Your keyboard commands are:\nweapons - allows you to change weapons\nfight - takes you to the monsters\nhelp - will remind you of the commands\ninfo - will show you your character stats\nquit - will exit the game"
error_text = "Sorry, I don't understand that command. Try typing 'help' if you don't remember the commands available."
monster_intro = "You head out to slay monsters. Before you are several monsters, please choose which you'd like to fight first: "
boss_fight = "---------------\nBOSS FIGHT\n---------------"
boss_run = "There's no running from a boss fight! Get in there and fight!"
monster_intro2 = "You approach the "
monster_help = "Commands for combat are 'attack' or 'run.' You can check your HP with 'info' and the monsters HP with 'monster'."
monster_killed = "Congrats, you killed the monster."
level_up = "You leveled up."
hp_up = "Your max HP increased by 2 and you healed to full."
boss_win = "You successfully killed the boss "
winscreen = "---------------\nThank you for playing The Best Game Ever!!\nI hope you enjoyed it\n\nCreated by Yavora, 2024\n---------------"


# monster dictionary, name:[description, weapon, Boss? Boolean, HP]
monsters = {
    "Troll" : ["A large hairy monster often found under bridges.", "Club", False, 2], # changed to 2HP for faster debugging. Change back to 8!! 
    "Zombie" : ["A putrid undead creature.", "Claws", False, 10], 
    "Vampire" : ["An undead that only comes out at night", "Fangs", False, 12], 
    "Chthulu" : ["An unspeakable nightmare.", "Unknown", True, 4] # changed HP for debugging, should be 20 !!
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
    "Claws" : ["Yikes those don't look clean.", 1, 0, 0],
    "Fangs" : ["Please don't come that close to me.", 1, 0, 0],
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
        print(f"You hit the monster for {dmg}HP")
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
        print("Crit Chance: " + str(self.crit_rate) + "%")
        print("Crit Bonus Damage: " + str(self.bonus))


#print(monsters.keys())