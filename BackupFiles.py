import os
import shutil
source = input('Enter Source Folder Name')
Dest = input('Enter Destination Folder Name')
listOfFiles = os.listdir(source)

for file in listOfFiles :
    shutil.copy((source + file),Dest)
    
