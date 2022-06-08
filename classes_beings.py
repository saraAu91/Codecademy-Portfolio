#define classes 
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

        def __init__(self, strength = 3, speed = 5, agility = 5, intelligence = 5, magic = 3):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic 
        
        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power

    
class Dwarf(Beings):

        def __init__(self, strength = 4, speed = 3, agility = 2, intelligence = 5, magic = 1):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic 
        
        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power
    
class Human(Beings):

        def __init__(self, strength = 4, speed = 3, agility = 2, intelligence = 5, magic = 1):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic 
        
        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power
    
class Hobbit(Beings):
        def __init__(self, strength = 2, speed = 2, agility = 2, intelligence = 4, magic = 1):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic 

        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power
    
class Wizards (Beings):
        def __init__(self, strength = 2, speed = 2, agility = 2, intelligence = 5, magic = 5):
            self.strength = strength
            self.speed = speed
            self.agility = agility
            self.intelligence = intelligence 
            self.magic = magic
        
        def attack_power(self):
                self.attack_power = super().attack_power()
                return self.attack_power










