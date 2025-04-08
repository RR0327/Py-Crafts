#File Handling 4 parts:     C        R       U       D
#                           Create   Read    Update  Delete
"""
Why file handling needed?
Ans: Due to file gives you the authority of CRUD.

File handling 2 types: 1. Txt 2. Bin

Mode:
4 types: 1. "r" stands for read, working for open a file, showing error if the file name not exited.
         2. "a" stands for append, working for appending(add whatever you at the end of your last string which you provided), showing error if the file name not exited.
         3. "w" stands for write, working for writing, showing error if the file name not exited.
         4. "x" stands for create, working for create specified file, showing error if the file name not exited.

Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)         

How to cretae a file?
Ans:f = open(filename,mode)
like example:f = open("demofile.txt","rt")  #Here "demofile.txt" is filename and "rt" are r for read and t for text 
open("demofile.txt") #by default read work 
f = open("demofile","w")
"""

f = open("demofile","r")
# a = f.read()
# print(a)
# f.write("\nItem List")
# f.write("\nProduct list")
# print(f.read(7))
print(f.readline())
print(f.readline())
for x in f:
    print(x)

#f = open("demofile_3","x")
# f = open("demofile_4","x")
import os
os.remove("demofile_3")
if os.path.exists("demofile_4"):
    os.remove("demofile_4")
else:
    print("The file doesnot exist")    
f.close()

#With statement 

with open("demofile_2.txt","a") as f: 
    f.write("\tHi")
    f.write("\nI am Rakib")