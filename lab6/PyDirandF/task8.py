import os
if os.access('myfile.txt', os.F_OK):
    print("existance:",True)
os.remove('./myfile.txt')