def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) -1 #find upperbound index so - 1 
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound)//2
        if the_list[pivot] == target:
            return pivot # returns the index where the target is
        if the_list[pivot] > target: # if the value of the list[pivot] > target
            upper_bound = pivot -1 # than upperbound is not where target is, and you assign new upperbound index at the pivot -1. dividing the list in half
        else: # final option means the target is in the lower half of list
            lower_bound = pivot + 1 
            # if the value of target is not = list[pivot]
            # and the target is not higher than list[pivot] 
    return -1 # returns -1 for any target values that are not within the list

my_list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 3))
print(binary_search(my_list, 97)) #returns -1