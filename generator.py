def count():
    print("One")
    yield 1

    print("Two")
    yield 2

    print("Three")
    yield 3


g = count()
print(next(g))
print(next(g))




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print([x*x for x in numbers if x*x <=50])

print((x*x for x in numbers if x*x <=50)) #generator

squares = (x*x for x in numbers if x*x <= 50) #generator

print(type(squares))
for x in squares :
    print(x, type(x)) 