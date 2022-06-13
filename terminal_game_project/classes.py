#IMPORT FUNCTIONS 
import inspect

#DEFINE CLASSES 
#define Beings 
class Beings:   

    def __init__(self, strength, speed, agility, intelligence, magic, stamina):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 
        self.stamina = stamina 
        self.health = 5
        self.max_health = 5
        self.is_knocked_out = False
        self.attack_power 
    
    def knock_out(self):
        if self.health == 0:
            self.is_knocked_out = True
            print("{name} was knocked out!".format(name = self))

    def lose_health(self):
        if self.stamina == 0:
            self.health -= 1
            if self.health <= 0:
                self.health = 0
                self.knock_out()
            else:
                print("{name} now has {health} health.".format(name = self, health = self.health))
        else: 
            print("Stamina: {stamina}, Health:{health}". format(stamina = self.stamina, health = self.health))
    def gain_health(self, amount):
        if self.health == 0:
            print("{name} is knocked out".format(name = self))
        
        self.health += amount

        if self.health >= self.max_health:
            self.health = self.max_health
        print("{name} now has {health} health.".format(name = self.name, health = self.health))

    def attack_points (self):
        self.attack_power = self.strength + self.agility + self.intelligence + self.magic
        return self.attack_power
   
    def attack(self, other_being):
        if self.attack_power > other_being.attack_power: 
            other_being.stamina -= 1 
        if self.attack_power < other_being.attack_power:
            self.stamina -= 1 
        else:
            print({"No damage from Being attack power"})
 



     
class Elf(Beings):
    def __init__(self, strength = 3, speed = 5, agility = 5, intelligence = 5, magic = 3, stamina = 4):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 
        self.stamina = stamina
        
    def attack_power(self):
        self.attack_power = super().attack_power()
        return self.attack_power

class Dwarf(Beings):

    def __init__(self, strength = 4, speed = 3, agility = 2, intelligence = 5, magic = 1, stamina = 5):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 
        self.stamina = stamina
        
    def attack_power(self):
        self.attack_power = super().attack_power()
        return self.attack_power
    
class Human(Beings):

     def __init__(self, strength = 4, speed = 3, agility = 2, intelligence = 5, magic = 1, stamina = 3):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 
        self.stamina = stamina
        
     def attack_power(self):
        self.attack_power = super().attack_power()
        return self.attack_power
    
class Hobbit(Beings):
    def __init__(self, strength = 2, speed = 2, agility = 2, intelligence = 4, magic = 1, stamina = 4):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 
        self.stamina = stamina

        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power
    
class Wizard (Beings):
        def __init__(self, strength = 2, speed = 2, agility = 2, intelligence = 5, magic = 5, stamina = 3):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic
            self.stamina = stamina
        
        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power


#Define Arms 
class Arms: 
    def __init__(self):
        self.resistance 
        self.attack 
    
class Blades (Arms):
    def __init__(self):
        self.resistance 
        self.being
        self.attack
    
    def resistance_points(self, being, resistance = 2):
        self.being = being
        self.resistance = resistance
        if isinstance (self.being, Human) == True:
            self.resistance = self.resistance + 3
        if isinstance (self.being, Elf) == True:
            self.resistance = self.resistance + 2
        if isinstance (self.being, Dwarf) == True:
            self.resistance = self.resistance - 1
        else:
            return 

    def attack_power (self, being):
        self.being = being 
        
        if isinstance (self.being, Elf)== True:
            self.attack = 3
        elif isinstance (self.being, Dwarf) == True: 
            self.attack = 2
        elif isinstance (self.being, Human) == True:
            self.attack = 5
        elif isinstance (self.being, Hobbit)== True:
            self.attack = 2
        elif isinstance (self.being, Wizard) == True:
            self.attack = 1
        else:
            self.attack = False
            print("The being entered does not belong to an acceptable class")

        

class Axes (Arms):

    def __init__(self):
        self.resistance 
        self.being
        self.attack

    def resistance_points(self, being, resistance = 5):
        self.being = being
        self.resistance = resistance
        if isinstance (self.being, Elf) == True:
            self.resistance = self.resistance - 1 
        else:
            return 

    def attack_power (self, being):
        self.being = being 

        if isinstance (self.being, Elf)== True:
            self.attack = 2
        elif isinstance (self.being, Dwarf) == True: 
            self.attack = 5
        elif isinstance (self.being, Human) == True:
            self.attack = 4
        elif isinstance (self.being, Hobbit)== True:
            self.attack = 3
        elif isinstance (self.being, Wizard) == True:
            self.attack = 2
        else:
            self.attack = False
            print("The being entered does not belong to an acceptable class")

        
class Bows(Arms):
    def __init__(self):
        self.resistance 
        self.being
        self.attack


    def resistance_points(self, being, resistance = 2):
            self.being = being
            self.resistance = resistance
            if isinstance (self.being, Elf) == True:
                self.resistance = self.resistance + 3
            elif isinstance (self.being, Dwarf) == True:
                self.resistance = self.resistance - 1
            else:
                return 
        

    def attack_power (self, being):
        self.being = being 

        if isinstance (self.being, Elf)== True:
            self.attack = 5
        elif isinstance (self.being, Dwarf) == True: 
            self.attack = 2
        elif isinstance (self.being, Human) == True:
            self.attack = 4
        elif isinstance (self.being, Hobbit)== True:
            self.attack = 3
        elif isinstance (self.being, Wizard) == True:
            self.attack = 1
        else:
            self.attack = False
            print("The being entered does not belong to an acceptable class")

class Wizard_Staff(Arms):
    def __init__(self):
        self.resistance 
        self.being
        self.attack

    def resistance_points(self, being, resistance = 2):
        self.being = being
        self.resistance = resistance
        if isinstance (self.being, Wizard) == True:
            self.resistance = self.resistance + 3
        else:
            return 
    

    def attack_power (self, being):
        self.being = being 

        if isinstance (self.being, Elf)== True:
            self.attack = 5
        elif isinstance (self.being, Dwarf) == True: 
            self.attack = 2
        elif isinstance (self.being, Human) == True:
            self.attack = 4
        elif isinstance (self.being, Hobbit)== True:
            self.attack = 3
        elif isinstance (self.being, Wizard) == True:
            self.attack = 1
        else:
            self.attack = False
            print("The being entered does not belong to an acceptable class")


# Define Enchantments 


elf1 = Elf()
human1 = Human()
dwarf1 = Dwarf()
hobbit1 = Hobbit()
wizard1 = Wizard()
gollum = "Gollum"


