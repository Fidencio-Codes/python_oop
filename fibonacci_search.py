# Fibonacci search algorithm is another divide and conquer algorithm. 
#  It uses fibonacci seq to calculate the size of the block it will search in each step
# 
# fibM = fibM_minus_1 + fibM_minus_2
# fibM_minus_1 and fibM_minus_2 are the 2 numbers right before fibM
#  0, 1, 1, 2, 3, 5, 8, 13, 21...


def fib_search(lys, target):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2 
    while (fibM < len(lys)): #while the array has elements remaining
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1 
    while (fibM > 1): #while fibM is greater than 1
        i = min(index + fibM_minus_2, (len(lys)- 1)) #determines the smallest fib index that is >= len(lys) -1 (fibM) ??? lol
        if (lys[i] > target):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_1 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > target):
            fibM = fibM_minus_2
            fibM_minus_1 -= fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else: 
            return i
    if (fibM_minus_1 and index < (len(lys) -1) and lys[index+1] == target):
        return index + 1
    return -1

print(fib_search([1,2,3,4,5,6,7,8,9,10,11], 11))