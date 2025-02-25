import os
print(os.access("./lab2",os.F_OK))# объект существует
print(os.access("./lab2",os.R_OK))#доступен на чтение
print(os.access("./lab2",os.W_OK))#доступен на запись
print(os.access("./lab2",os.X_OK))#доступен на исполнение