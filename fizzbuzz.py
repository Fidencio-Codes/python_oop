def fizzbuzz(num):
    for x in list(range(1, num+1)):
        if x%3 == 0 and x%5 == 0:
            print("Fizzbuzz")
        elif x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print(x)

num = int(input("How big do you want your FizzBuzz list? Enter numbers: "))
fizzbuzz(num)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
