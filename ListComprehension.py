numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print([x*x for x in numbers if x*x <=50])

print((x*x for x in numbers if x*x <=50)) #generator

squares = (x*x for x in numbers if x*x <= 50) #generator

print(type(squares))
for x in squares :
    print(x, type(x)) 

