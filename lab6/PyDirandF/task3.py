import os
path="C:/Users/H.GULNAFIS/OneDrive/Рабочий стол/пп2/lab6/PyDirandF/task5.py"
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("path doesn't exists")