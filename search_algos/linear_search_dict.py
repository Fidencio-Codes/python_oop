def linear_search_dictionary(my_dictionary, target):
    for key in my_dictionary:
        if my_dictionary[key] == target:
            print("Found at key", key) 
            return key
    print("Not found in the dictionary")
    return -1 

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)