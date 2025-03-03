import os

def task6():
    
    from string import ascii_uppercase
    for letter in ascii_uppercase:
        with open(f'/PydirandF/files/{letter}.txt', 'w'):
            pass

   #  for letter in ascii_uppercase:
   #      os.remove(f'/./home/user/PP2_Spring/{letter}.txt')
        
task6()