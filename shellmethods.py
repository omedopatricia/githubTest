import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

#make a duplicate of an existing file
if(path.exists("textfile.txt")):
#get path to the source file
    src = path.realpath("textfile.txt")
#make a backup copy
    dst = src + " .bak"
#copy permissions, modification time, other info
    #shutil.copy(src, dst)
    #shutil.copystat(src, dst)

#rename the original file
#os.rename("newfile.txt", "textfile.txt")

#now put things into a zip file
#root_dir, tail = path.split(src)
#shutil.make_archive("archive", "zip", root_dir)

#more fine grained control to the archive
with ZipFile("testzip.zip", "w") as newzip:
    newzip.write("textfile.txt")
    newzip.write("textfile.txt.bak")