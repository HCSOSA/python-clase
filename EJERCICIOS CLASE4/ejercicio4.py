import os

ruta = os.getcwd()

file_path = os.path.join(ruta,'src','texto.txt')
print(file_path)

""" with open(file_path,mode='r') as f:
    data = f.readlines()
    
    print(data)
    pass """