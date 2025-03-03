# import shutil 

# shutil.copy('task4.txt', 'task7.txt')

with open('task4.txt', 'r') as f1:
    with open('task7.txt', 'w') as f2:
        f2.write(f1.read())
        # for i in f1: f2.write(i)