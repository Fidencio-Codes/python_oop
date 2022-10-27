# if you're looking for a topic in a textbook, you wouldnt go pg to pg
# until you found the topic. You would find what the section it is in 
# and start looking there
 
# binary search uses the same concept 
#  sorted data sets allows the use of binary search 

# divide and conquer strategy #
# binary searches repeatedly divide search interval in half 
    # until the target value is found

## Steps to creating a binary search ##
# find lower bound, upper bound, and the pivot(middle index)
# comapre target value with Pivot value:
    # if the target value is higher than Pivot val, discard all lower values
    # if the target value is lower than pivot val, disacrd all higher vals
# repeat steps 1 and 2 till you find target
