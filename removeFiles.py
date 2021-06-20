import os 
import shutil
# Write the name of the directory here,
# that needs to get sorted
#path = "/Users/aryan/ARYAN/WHITEHAT/CLASS/PYTHON/test/"
path=input("Enter The Name Of The Directory To Be Sorted: ")
listOfFiles=os.listdir(path)
for file in listOfFiles:
    name,ext=os.path.splitext(file)
    # This is going to store the extension type
    ext=ext[1:]
    # This forces the next iteration,
 # if it is the directory
    if(ext==""):
        continue

    if(os.path.exists(path + "/" + ext)):
        shutil.move(path+'/'+file, path+'/'+ext+'/')
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/')