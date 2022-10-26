# PERFORMANCE BENCHMARK TEST
class_names = [
    "fidencio", "genesis", "bob", "mary", "xiomara", "jeff", "lucio", "damon", 
    "iman", "pharah", "regina", "leandro", "winston", "brian", "snoop", "zarya",]

def create_dataset():
    import random
    num_entries = 5000000
    f = open("data.txt", "w")
    for i in range(num_entries):
        current = random.choice(class_names)
        f.write(current+"\n")
    f.close()

# ^^^^Creating a dataset using function open() ^^^^
#   by opening file called data.tx and randomly assigning class_names iterated by
#   the amount in num_entries - five million 
#  each line in the file will have one of the names randomly selected from names

def read_dataset_list():
    class_counts = []
    for c in class_names:
        class_counts.append(0)
    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line!="": #checking if it's on the last line of the file
                class_counts[class_names.index(line)]+=1
    print(class_counts)
# Creating list by the same length as class_names

def read_dataset_dict():
    class_counts = {}
    for c in class_names:
        class_counts[c] = 0
    with open("data.txt") as f:
        for line in f:
            line = line.strip()
            if line!="":
                class_counts[line]+=1
    print(class_counts)  
# creating dictionary from class_names and assigining value to 0, key is names

# comparing dict vs list by opening data.txt file in both cases 
# should be able to see that dictionaries are are significantly faster 

import time

t0 = time.time()
create_dataset()
t1 = time.time()
total = t1-t0
print(f"Database creation took: {total} \n")

t0 = time.time()
read_dataset_list()
t1 = time.time()
total = t1-t0
print(f"List took: {total}\n")

t0 = time.time()
read_dataset_dict()
t1 = time.time()
total = t1-t0
print(f"Dictionary took: {total} \n")

