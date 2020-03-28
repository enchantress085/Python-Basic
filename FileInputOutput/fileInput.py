# -*- coding: utf-8 -*-

#-----s = input("Something :")
#-----print(s)

# The open functions --------
"""
Before you can read or write a file, 
you have to open it using Python's built-in open() function.
This function creates a file object,

  1.file_name − The file_name argument is a 
    string value that contains the name of the file 
    that you want to access.
    
  2.access_mode − The access_mode determines the 
    mode in which the file has to be opened, i.e., read, 
    write, append, etc. A complete list of possible 
    values is given below in the table. This is an 
    optional parameter and the default file access 
    mode is read (r).
    
  3.buffering − If the buffering value is set to 0, 
    no buffering takes place. If the buffering value is 1, 
    line buffering is performed while accessing a file. 
    If you specify the buffering value as an integer 
    greater than 1, then buffering action is performed 
    with the indicated buffer size. If negative, 
    the buffer size is the system default(default behavior).
"""

"""
=======  File opening and writing Modes

------ wb -----
Opens a file for writing only in binary format. 
Overwrites the file if the file exists. 
If the file does not exist, creates a new file for writing.
"""
fi = open("shaju.txt", "wb")
print("Name of the file: ", fi.name)
print("Close or not: ", fi.closed)
print("Openinf file: ", fi.mode)
fi.close()

"""
----------close---------
Python automatically closes a file when the reference 
object of a file is reassigned to another file. 
It is a good 
practice to use the close() method to close a file.
"""
print("------- The write() method -----------")
"""
The write() method writes any string to an open file. 
It is important to note that Python strings can have 
binary data and not just text.

The write() method does not add a newline character 
('\n') to the end of the string
"""

"""
-------- w ------------
Opens a file for writing only. Overwrites the file 
if the file exists. If the file does not exist, 
creates a new file for writing.
"""

fw = open("write.txt", "w")
fw.write( "Python is a great language.\n it's really great\n" )

fw.close() #-----close the file 


"""
The read() method reads a string from an open file. 
It is important to note that Python strings can have 
binary data. apart from text data.
"""
print("----------- The read() Method -----------\n")

fw = open("write.txt", "r+")
str = fw.read(20)
print("Read string is : ", str)

fw.close()


"""
------------ File Positions -----------

  1.The tell() method tells you the current position 
  within the file; in other words, the next read or 
  write will occur at that many bytes from the beginning 
  of the file.

  2.The seek(offset[, from]) method changes the current 
    file position. The offset argument indicates the 
    number of bytes to be moved. The from argument 
    specifies the reference position from where the 
    bytes are to be moved.

  3.If from is set to 0, the beginning of the file 
    is used as the reference position. If it is set to 1, 
    the current position is used as the reference position. If it is set to 2 then the end of the file would be taken as the reference position.
"""
print("------------ File Positions -----------\n")

# ------- Open a file 
fw = open("write.txt", "r+")
str = fw.read(20)
print("Read strinf is : ", str)

#-----Check current position
position = fw.tell()
print("Current file position : ", position)

#----------Reposition pointer at the beginning once again
position = fw.seek(0, 0)
str = fw.read(20)
print("Again Read string is : ", str)

fw.close()

print("-----------------\n")
print("--------- rename  -----------\n")
import os

os.rename("shaju.txt", "golam.txt")


print("--------- remove -----------\n")
os.remove("golam.txt")

os.mkdir("test")












