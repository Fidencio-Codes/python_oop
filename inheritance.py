class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self, direction):
        print(self.name, "walks to the", direction)
    def talk(self, speech):
        print(self.name, "says:", speech)

class Wizard(Human):
    def __init__(self, name, age, spell_points):
        super().__init__(name, age)
        self.spell_points = spell_points

    def cast_spell(self, spell):
        print(self.name, "casts", spell)
        

# wizard class inherited Human super class' attributes
# you can use __init__ fxn to add attributes to Wizard child class 
    # But this will override the init fxn of the parent class
    # use super().__init__() so that Wizard class can add attributes
        # without interupting the parent attributes