# Making a basic turn based combat game
# This file should contain all the class definitions?

class Player:
    def __init__(self, name, weapon, level, hp):
        self.name = name
        self.weapon = weapon
        self.level = level
        self._hp = hp

    def health(self):
        return int(self._hp)


    def hit(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
        print(f"You were hit for {dmg}HP, you have {self._hp}HP remaining")
        if self._hp == 0:
            print("Game over.")
    
    def heal(self):
        # if it takes a variable heal, will need to calculate to max...
        # max = 10 + level*2 HP, so starting at 12 HP
        max = 10 + (self.level * 2)

        if self._hp != max:
            self._hp += 1
            print("Healed")
        elif self._hp ==max:
            print("Life at maximum, cannot heal")
        
    def info(self):
        print("Character Info")
        print("---------------")
        print("Name: " + self.name)
        print("Weapon: " + self.weapon)
        print("Level: " + str(self.level))
        print("Health: " + str(self._hp) + "HP")
        print("---------------")

def healed(name):
    name.heal()
    
'======================================'

#p = Player("Cyberpunk77", "Sword", 3, 10)
#p.info()


"""
p.hit()
p.hit()

p.heal()
healed(p)

p.hit()
p.hit()
"""