# class User:
#     pass
# # pass does nothing, need to have something in line after calling class

# user1 = User()
# user1.first_name = "Dave"
# user1.last_name = "Bowman"

# print(user1.first_name)
# print(user1.last_name)

# first_name = "Arthur"
# last_name = "Turner"

# user2 = User()
# user2.first_name = "Sonya"
# user2.last_name = "Trucha"

# # even if using same variable name, the values are 
#     # kept separated cuz of the class 
# # each object/instance has different values for the same variable names 
# print(first_name, last_name)
# print(user1.first_name, user1.last_name)
# print(user2.first_name, user2.last_name)

# user1.age = 37
# user2.favorite_book = "Frankenstein"
# # adding different attributes attached 

# print(user1.age)
# # print(user2.age)
# # trying to use an attribute that is not assigned to your class will return
#     # an AttributeError  so be careful about it 

# #######################################################################
# why create a Class? a dictionary could do the above
    # cuz classes are OP 

# functions inside classes are called methods 
# __init__() method is called every time you create a new instance a class

from datetime import datetime

class User:
    """Create docstring to explain what your class is doing/how it works.
    In this case, we are storing the name and birthday of every instance 
    in the class User. splitting full name into first and last"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        #Retrieve first and last name from full_name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1] #-1 is last item in array, 1 works too in this case

    def age(self):
        """Returns the age of the user in years"""
        today = datetime.date(2022, 5, 16)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) 
        age_in_days = (today) - int(dob)
        age_in_yrs = age_in_days/365 
        return(age_in_yrs)

user = User("David Bowie", "19671012")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())

# help(User) - used to read the explanation of the class and what it does, little sparksnotes 

# in this case self object is not assigned to variable last_name making you
# unable to print user's last name, AttributeError occurs
