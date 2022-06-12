#define classes 
import inspect
class Beings:   

    def __init__(self, strength, speed, agility, intelligence, magic):
        self.strength = strength
        self.speed = speed
        self.agility = agility
        self.intelligence = intelligence 
        self.magic = magic 

    def attack_power (self):
        self.attack_power = self.strength + self.agility + self.intelligence + self.magic
        return self.attack_power
     
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



class Arms: 
    def __init__(self, attack, resistance):
        self.attack = attack
        self.resistance = resistance
    
class Blades (Arms):
    def __init__(self, attack, resistance = 3):
        self.attack = attack
        self.resistance = resistance

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

    def __init__(self, attack, resistance = 5):
        self.attack = attack
        self.resistance = resistance

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
    def __init__(self, resistance = 2):
        self.resistance = resistance

    def being_resistance_check(self, being, resistance):
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
    def __init__(self, resistance = 2):
        self.resistance = resistance

    def being_resistance_check(self, being, resistance = 2):
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

elf1 = Elf()
human1 = Human()
dwarf1 = Dwarf()
hobbit1 = Hobbit()
wizard1 = Wizard()
gollum = "Gollum"

bow1 = Bows()
wizard_staff1 = Wizard_Staff()

bow1.attack_power (being = elf1)
#print(bow1.attack)

bow1.attack_power (being = human1)
#print(bow1.attack)

bow1.attack_power (being = dwarf1)
#print(bow1.attack)

bow1.attack_power (being = hobbit1)
#print(bow1.attack)
#print(bow1.resistance) 
#print("bow resistance:{resist}".format(resist = bow1.resistance))

bow1.attack_power (being = wizard1)
#print(bow1.attack)
#print("bow resistance:{resist}".format(resist = bow1.resistance))

bow1.attack_power (being = gollum)
#print(bow1.attack)

wizard_staff1.being_resistance_check(being = wizard1)
#print(wizard_staff1.resistance)

wizard_staff1.being_resistance_check(being = hobbit1)
#print(wizard_staff1.resistance)

bow1.being_resistance_check(being = elf1)
print(bow1.resistance)

bow1.being_resistance_check(being = dwarf1)
print(bow1.resistance)

bow1.being_resistance_check(being = hobbit1)
print(bow1.resistance)

