def gen(n):
    for i in range(0,n):
        if i%3==0 and i%4==0:
            yield i
        i+=1
        
n=int(input())
for i in gen(n):
    print(i)