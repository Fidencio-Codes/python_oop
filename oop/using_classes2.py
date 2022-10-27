class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

user1 = User("Jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_password("bestpassword")


# remember this is the constructor method when using __ini__
# defining an instance method on a class


# What is the purpose of the __init__ method in a class? When does it execute? 
    # init method allows class to set up the objects attributes(parameters) and is always executed when classes are initialized
# What is the purpose of the self parameter in a method? 
    # the self parameter is the first parameter in the __init__ method and the object which you assign attributes to
# What is an instance?
    # the object that belongs to your class 
# How do you define a subclass from a superclass?
    # subclass the class that inherits from superclass
# What is the use of the super() function?
    # super() function allows for other attributes to be added to your subclass without overriding the parent attributes