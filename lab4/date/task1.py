from datetime import date, timedelta
date = date.today() - timedelta(days=5)
print('Current Date :',date.today())
print('5 days before Current Date :',date)
def x(n):
    for i in range(n):
        yield i**2
    
x = (i**2 for i in range(n))