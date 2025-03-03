import os 

path = r'C:\Users\H.GULNAFIS\OneDrive\Рабочий стол\пп2\lab6'

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')