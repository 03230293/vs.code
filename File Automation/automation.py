import os
import shutil

path=input("Enter path: ")
files= os.listdir(path)

#Move files
for file in files:
    filename,extension=os.path.splitext(file)
    extension=extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file,path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file,path+'/'+extension)
    
    # https://youtu.be/VRzIyUrL63A?si=IjvS5QFkJ6SjOBE-