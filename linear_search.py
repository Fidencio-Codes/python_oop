# searching for an item one by one 
# ex of linear search is like looking for a book in a library, one by one 
# benefit: will always work, no matter is items are sorted or not sorted. 
# disadvantages, increase in list items will increase amount os time it takes 


def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index ", x)
            return x
    print("Target is not in the list")
    return -1 #index for list must always be 0 or highter, used for target values outside the list amounts

my_list = [6,9,8,7,9,1,5,6,8,4,2]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 7)

