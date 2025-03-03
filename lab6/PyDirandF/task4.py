import os

path = r'C:\Users\H.GULNAFIS\OneDrive\Рабочий стол\пп2\lab6\PydirandF\task4.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))