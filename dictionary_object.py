# hash map
# takes input (str or int) to perform some calculation using key as the input to 
#   retrieve the object we desire to pull out in memory 

d = {}
l = []

d[1] = "yes"
d['1'] = "no"
print(d[1])
# key transformed into number and used to 
print(d['1'])

# python treats str and int representations seperately 
#   store something at the integer of 1 that is different than at the str of 1
# for int - key is tranformed into number, then number is used to calculate the 
#   memory sddress of where the value is stored
#   1 will be a simple conversion to binary
# for str - key is converted to ascii format (or something like it) & that hex 
#   value will be used as input to the function to calc where to access the element 
#   in memory

d[2] = 9000
print(d[2])

class my_class:
    def __init__(self):
        self.data = "data"

instance = my_class()

d["object"] = instance
# can use that instance of a value in a key value pair
obj = d["object"].data
print(obj)

print(d.keys())
# keys() fxn returns all keys in a list assigned to dictionary
# iterate over the elements in a dictionary use .keys() or items()
print(d.items())
# items() will return a list of tuples, where each tuple is a key-value pair 

# iterate over the keys
for key in d.keys():
    print(key)

for key, value in d.items():
    print(key, value)

# dictionaries are unordered, calling them will show random ordering 