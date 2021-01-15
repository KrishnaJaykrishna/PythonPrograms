import os
import shutil
path = input('Enter The Name Of The Directory To Be Sorted ')
listOfFiles = os.listdir(path)
for file in listOfFiles:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file,path + '/'  + ext + '/' + file)
