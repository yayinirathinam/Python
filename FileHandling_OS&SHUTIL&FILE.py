#!/usr/bin/env python
# coding: utf-8

# In[38]:


import shutil as util
import os as o

##assign Paths
directory_path = "C:\\Users\\yayin\\OneDrive\\Resume\\Folder1"
print("Dir1:",directory_path)
directory_path2 = "C:\\Users\\yayin\\OneDrive\\Resume\\Folder2"
print("Dir2:",directory_path2)
directory_path3 = "C:\\Users\\yayin\\OneDrive\\Resume\\Folder3"
print("Dir3:",directory_path3)

##If not exist, then create directory

if not o.path.exists(directory_path):
    M1 = o.mkdir(directory_path)
     
if not o.path.exists(directory_path2):
    M2 = o.mkdir(directory_path2)
    
##Copy Directory SHUTIL functions

if not o.path.exists(directory_path3):
    util.copytree(directory_path,directory_path3)    
    print("Folder3 - Copy Dir:",directory_path3, "Contents:", o.listdir(directory_path3))
    
file_path = o.path.join(directory,"File1.txt")
print("Folder1-File_Path1:", file_path)
file_path2 = o.path.join(directory,"File2.txt")
print("Folder1-File_Path2:", file_path2)

## create file and Write
if not o.path.exists(file_path):
    file= open(file_path,'w')
    file.close()
    file = open(file_path,'w')
    file.write("This is File1")
    file.close()

if not o.path.exists(file_path2):

    file= open(file_path2,'w')
    file.close()
    file = open(file_path2,'w')
    file.write("This is File2")
    file.close()


##Move and Copy Files SHUTIL functions
    
file_path3 = o.path.join(directory_path2,"File1.txt")
if not o.path.exists(file_path3):
    util.copy(file_path, directory_path2)
else:
    print("Folder2-File_path3:",file_path3)
    print(o.listdir(directory_path2))
    
file_path4 = o.path.join(directory_path2,"File2.txt")
if not o.path.exists(file_path4):
    util.move(file_path2, directory_path2)
    print("Folder2-File_path4:",file_path4)
    
else:
    print("Folder2-File_path4:",file_path4)
    print(o.listdir(directory_path2))
    
    file = open(file_path4,'r')
    print("File 2 Contents:",file.read())
    file.close




# In[ ]:





# In[ ]:




