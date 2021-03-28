from zipfile import ZipFile
from os import listdir
import os
import pdb
filename="chromedriver_win32.zip"
filename_folder=(filename.replace(".zip",""))
print(type(filename_folder))
print(os.getcwd())
os.chdir("C:/autofil/insta")
print(os.getcwd())
os.chdir("C:/autofil")
print(os.getcwd())
pdb.set_trace()
w= open(os.path.join('D:/insta', 'did_not_unfollowed2020-08-06.txt'),'w')
print(os.getcwd())
print(w.write("hatt"))
w.close()
# dirr = os.path.join('C:/','/Users/Deepak/Downloads')
# os.chdir(dirr)
# print(os.getcwd())
# # Create a ZipFile Object and load sample.zip in it
# with ZipFile(filename, 'r') as zipObj:
#     os.mkdir(filename_folder)
#     zipObj.extractall(filename_folder)
# zipObj.close()



# def adda(a,b=10,d=20):
#     c= a+b
#     print(c)
#
# adda(10)