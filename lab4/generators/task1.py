def squares(n):
    for i in range(n):
        yield i**2
        
for i in squares(15):
    print(i)