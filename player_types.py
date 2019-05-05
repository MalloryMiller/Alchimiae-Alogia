import random as r
import battle_graphics as g


buff = 25
stamina_buff = 5

randomness = 15
atkdef_divider = 5

full_health = 100
full_strength = 50
full_stamina = 20
full_defense = 50

heal_rate = 40

stamina_cutoffs = [3, 6, 12, 2]



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
        
        self.health = full_health
        self.strength = full_strength
        self.stamina = full_stamina
        self.defense = full_defense
        
        self.text = g.flavorText('left')

        self.act_names = ['', '', '', '']
        
        self.full_health = full_health
        self.full_strength = full_strength
        self.full_stamina = full_stamina
        self.full_defense = full_defense


        
    def check_lost(self):

        if self.health <= 0:
            self.visual.lose()
            return True
        else:
            return False
    


    
    def end_turn(self, enemy):
        enemy.begin_turn()






    def begin_turn(self):

        if self.health <= 0:
            return
        
        elif self.stamina + 2 >= self.full_stamina:
            self.stamina = self.full_stamina
            
        else:
            self.stamina += 2
        self.stamina_bar.change_value(self.stamina)






    def attack(self, target, atk_name, multiplier = 1):
        damage = ((self.strength // atkdef_divider) \
                 * multiplier) + (r.randint(0, randomness))
        self.enemy = target
        
        if multiplier * 3 <= self.stamina:

            self.text.change_text(str(
                self.name + " has attacked " + target.name +
                " with " + atk_name + ".")
                                  )
            
            self.stamina -= multiplier * 3
            self.stamina_bar.change_value(self.stamina)
            
            self.visual.attacking()
            
            if target.take_damage(self, damage):
                g.game_over(self, target, atk_name)
                return True
                
            
        else:
            self.text.change_text(str(
                self.name + " tried to attack " + target.name +
                " with " + atk_name + ", " + "but they didn't have enough stamina.")
                                      )
            self.stamina_bar.not_enough_stam()
            
        self.end_turn(target)





        
    def take_damage(self, attacker, damage):
        damage -= self.defense // atkdef_divider \
                  + r.randint(-randomness, 0)
        self.health -= damage

        self.health_bar.change_value(self.health)
        
        self.text.change_text(str(
            self.name + " has taken " + str(damage) + " points of damage from " + \
              attacker.name + "'s attack.")
                              )
        self.visual.take_damage()

        if self.check_lost():
            return True






    def heal(self, enemy, heal_name):
        heal = heal_rate + r.randint(0, randomness)
        maxim = False
        
        if self.health + heal > self.full_health:
            maxim = True
            heal = self.full_health - self.health



        if self.stamina >= 2:
            
            self.health += heal

            self.health_bar.change_value(self.health)
            
            self.text.change_text(str(
                self.name + " has healed " + str(heal) +
                " health points with a " + heal_name + ".")
                              )
            self.stamina -= 2
            self.visual.healing()
            self.stamina_bar.change_value(self.stamina)

        else:
                self.text.change_text(str(
                    self.name + " was too tired to heal with " + heal_name + ".")
                                      )



        if maxim == True:
            self.text.change_text(str(
                self.name + " is at full health!")
                                  )


        self.end_turn(enemy)






    def act1(self, target):
        self.attack(target, self.actNames[0])

    def act2(self, target):
        self.attack(target, self.actNames[1], 2)


    def act3(self, target):
        self.attack(target, self.actNames[2], 4)


    def act4(self, target):
        self.heal(target, self.actNames[3])






class Alchemist(Player): # Light
    def __init__(self, name, enemy_t_or_f):
        super().__init__(name)
        self.enemy = enemy_t_or_f

        if self.enemy:
            self.t = 'The Enemy has'
        else:
            self.t = 'You have'
        
        self.actNames = [
            "Blinding Barrage",
            "Splash Poison",
            "Acidic Solution",
            "Healing Medley"
            ]

        self.full_health += buff
        self.health += buff
        
        if enemy_t_or_f == True:
            self.visual = g.visualFigure("mehcla")
            self.health_bar = g.health_bar(self.full_health, 'right')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'right')
            self.text = g.flavorText('right')
        else:
            self.visual = g.visualFigure("alchem")
            self.health_bar = g.health_bar(self.full_health, 'left')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'left')








class AzureArcher(Player): # Water
    def __init__(self, name, enemy_t_or_f):
        super().__init__(name)
        
        self.enemy = enemy_t_or_f
        
        if self.enemy:
            self.t = 'The Enemy has'
        else:
            self.t = 'You have'
        
        self.actNames = [

            "Triple Arrow",
            "Sea Strike",
            "Arrow Tsunami",
            "Bandage"

            ]
        
        self.full_stamina += stamina_buff
        self.stamina += stamina_buff
        
        if enemy_t_or_f == True:
            self.visual = g.visualFigure("aeruza")
            self.health_bar = g.health_bar(self.full_health, 'right')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'right')
            self.text = g.flavorText('right')

        else:
            self.visual = g.visualFigure("azurea")
            self.health_bar = g.health_bar(self.full_health, 'left')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'left')








class IncendiaryWarrior(Player): # Fire
    def __init__(self, name, enemy_t_or_f):
        super().__init__(name)
        
        self.enemy = enemy_t_or_f

        if self.enemy:
            self.t = 'The Enemy has'
        else:
            self.t = 'You have'
        
        self.actNames = [

            "Fiery Slice",
            "Burning Blade",
            "Blind Rage",
            "Healing Stew"

            ]

        self.full_strength += buff
        self.strength += buff
        
        if enemy_t_or_f == True:
            self.visual = g.visualFigure("rawcni")
            self.health_bar = g.health_bar(self.full_health, 'right')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'right')
            self.text = g.flavorText('right')

        else:
            self.visual = g.visualFigure("incwar")
            self.health_bar = g.health_bar(self.full_health, 'left')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'left')






class StarryKnight(Player): # Darkness
    def __init__(self, name, enemy_t_or_f):
        super().__init__(name)
        
        self.enemy = enemy_t_or_f
        
        if self.enemy:
            self.t = 'The Enemy has'
        else:
            self.t = 'You have'
        
        self.actNames = [
            
            "Twilit Hammer",
            "Ground Slam",
            "Shadow Swing",
            "Medical Break"
            
            ]

        self.full_defense += buff
        self.defense += buff
        
        if enemy_t_or_f == True:
            self.visual = g.visualFigure("nkrats")
            self.health_bar = g.health_bar(self.full_health, 'right')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'right')
            self.text = g.flavorText('right')

        else:
            self.visual = g.visualFigure("starkn")
            self.health_bar = g.health_bar(self.full_health, 'left')
            self.stamina_bar = g.stamina_bar(self.full_stamina, 'left')
        




player_types = [
    
    Alchemist,
    AzureArcher,
    IncendiaryWarrior,
    StarryKnight

    ]

