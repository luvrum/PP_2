import task9, task10, task11, task13

#Volume
r = int(input("Radius of sphere - "))
print(f'Volume of sphere = {task9.v(r)}')


#Uniques
l = list(map(int, input("write a list - ").split()))
print(f'Uniques = {task10.unique(l)}')


#Palindrom
s = input("Write a sectence to check palindrom - ")
if task11.palindrome(s):
    print("It's a palindrom")
else:
    print("Nope, it isn't palindrom")


#Play a game
print("\nPlay a game, guess number 1:30")
from random import randint
mynum = randint(1, 30)
att = task13.guess(mynum)
print(f"You're right, {att} - attemps needed")