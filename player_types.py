import random as r
import graphics as g


buff = 25
stamina_buff = 5

randomness = 10
atkdef_divider = 5

full_health = 100
full_strength = 100
full_stamina = 20
full_defense = 100



player_names = [  # randomly selected

    ['Sol', 'Apollo', 'Anwar', 'Luz'],  # Alchemist
    ['Mare', 'Bahari', 'Cascade', 'Mai'],  # Azure Archer
    ['Ash', 'Azar', 'Pele', 'Hestia'],  # Incendiary Warrior
    ['Lune', 'Jaci', 'Amaris', 'Aku']  # Starry Knight

    ]

enemy_names = [
    
    ['Σολ', 'Απολλο', 'Ανωαρ', 'Λυζ'],  # Alchemist
    ['Μαρε', 'βανηαρι', 'Ξασξαδε', 'Μαι'],  # Azure Archer
    ['Αση', 'Αζαρ', 'Πελε', 'Ηεστια'],  # Incendiary Warrior
    ['Λυνε', 'Γαξι', 'Αμαρισ', 'Ακυ']  # Starry Knight
        
    ]




class Player():
    def __init__(self, name):
        self.name = str(name)
        self.buff_status_time = 0
        
        self.health = full_health
        self.strength = full_strength
        self.stamina = full_stamina
        self.defense = full_defense
        
        self.full_health = full_health
        self.full_strength = full_strength
        self.full_stamina = full_stamina
        self.full_defense = full_defense


    def begin_turn(self):
        self.stamina += 2

    
    def end_turn(self):
        self.buff_status_time -= 1


    def attack(self, target, atk_name, multiplier = 1):
        damage = (self.strength // atkdef_divider) \
                 * multiplier + (r.randint(0, randomness))

        print(self.name, "has attacked", target.name, "with", atk_name + ",")

        if multiplier * 4 <= self.stamina:
            target.take_damage(self, damage)
            self.stamina -= multiplier * 4
        else:
            print("but they didn't have enough stamina.")
            
        self.end_turn()

        
    def take_damage(self, attacker, damage):
        damage -= self.defense // atkdef_divider \
                  + r.randint(-randomness, 0)
        self.health -= damage
        
        print(self.name, "has taken", damage, "points of damage from", \
              attacker.name + "'s attack.")
        
        self.begin_turn()


    def heal(self, heal_name):
        heal = (self.full_health // 4) + r.randint(0, randomness)
        
        if self.health + heal > self.full_health:
            maxim = True
            heal = self.full_health - self.health
            
        self.health += heal
        print(self.name, "has healed", heal, "health points with a", heal_name + ".")

        if maxim == True:
            print(self.name, "is at full health!")






class Alchemist(Player): #Light
    def __init__(self, name, enemy_t_or_f):
        super().__init__(name)
        self.actNames = [
            "Acidic Solution",
            "Blinding Barrage",
            "Splash Poison",
            "Healing Medley"
            ]
        if enemy_t_or_f == True:
            self.visual = g.visualFigure("mehcla")
        else:
            self.visual = g.visualFigure("alchem")

        self.full_health += buff
        self.health += buff

        


    def act1(self, target):
        self.attack(target, self.actNames[0])


    def act2(self, target):
        self.attack(target, self.actNames[1], 3)


    def act3(self, target):
        self.attack(target, self.actNames[2], 5)


    def act4(self, target):
        self.heal(self.actNames[3])






class AzureArcher(Player): #Water
    def __init__(self, name):
        super().__init__(name)

        self.actNames = [

            "Triple Arrow",
            "Sea Strike",
            "Arrow Tsunami",
            "Bandage"

            ]
        
        self.full_stamina += stamina_buff
        self.stamina += stamina_buff


    def act1(self, target):
        self.attack(target, self.actNames[0])


    def act2(self, target):
        self.attack(target, self.actNames[1], 3)


    def act3(self, target):
        self.attack(target, self.actNames[2], 5)


    def act4(self, target):
        self.heal(self.actNames[3])






class IncendiaryWarrior(Player): #Fire
    def __init__(self, name):
        super().__init__(name)
        
        self.actNames = [

            "Fiery Slice",
            "Burning Blade",
            "Blind Rage",
            "Healing Stew"

            ]

        self.full_strength += buff
        self.strength += buff


    def act1(self, target):
        self.attack(target, self.actNames[0])


    def act2(self, target):
        self.attack(target, self.actNames[1], 3)


    def act3(self, target):
        self.attack(target, self.actNames[2], 5)


    def act4(self, target):
        self.heal(self.actNames[3])





class StarryKnight(Player): #Darkness
    def __init__(self, name):
        super().__init__(name)
        
        self.actNames = [
            
            "Twilit Hammer",
            "Ground Slam",
            "Shadow Swing",
            "Medical Break"
            
            ]

        self.full_defense += buff
        self.defense += buff


    def act1(self, target):
        self.attack(target, self.actNames[0])


    def act2(self, target):
        self.attack(target, self.actNames[1], 3)


    def act3(self, target):
        self.attack(target, self.actNames[2], 5)


    def act4(self, target):
        self.heal(self.actNames[3])




player_types = [
    
    Alchemist,
    AzureArcher,
    IncendiaryWarrior,
    StarryKnight

    ]
