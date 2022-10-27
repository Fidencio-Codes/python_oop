# class Player:
#     max_hp = 4000

# player1 = Player()
# print(player1.max_hp)

# player2 = Player()
# print(player2.max_hp)

# Player.max_hp = 5000
# print(player1.max_hp)
# print(player2.max_hp)
# # change the value of the attribute on the class itself, like a variable


# # two attributes you can define in classes
# # class attributes (all of the above)- max_hp
#     # change attributes and instances of class
#     # created two objects from the player class
# #############################################################
# # instance attributes - stored per instance rather than on class
# #   (most commonly used attributes)

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0
player1 = Player("Juan", 1800)
player2 = Player("Marta", 2300)

print("P1:", player1.name, " -- HP:", player1.hp, " -- SCORE:", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, " -- SCORE:", player2.score)

player1.hp += 500
player1.score += 10
# print("P1:", player1.name, " -- HP:", player1.hp, " -- SCORE:", player1.score)
# print("P2:", player2.name, " -- HP:", player2.hp, " -- SCORE:", player2.score)

# constructor method, includes parameter list 
#   first parameter will always be the object
#   following parameters are attributes

