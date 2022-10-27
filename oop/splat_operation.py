### splat operators has two types 1 and 2 stars * **

def f(x, y, z):
    print(x,y,z)

# f(1, 2, 3)
list = [1, 2, 3,]
f(*list)

f(*[], *list)
f(*[], *list, *[],)

dict = {"x":1, "y":2, "z":3,}
f(*dict)
f(**dict)