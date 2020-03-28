"""
A Python program can handle date and time in several ways. 
Converting between date formats is a common chore for computers. 
Python's time and calendar modules help track dates and times.
"""

print ('---------Date & Time---------------\n')

import time

ticks = time.time()
print ("Number of ticks = ", ticks)

print ("LocaTime :>> ", time.localtime())
print ('\n')
local = time.localtime(time.time())
print ("Current :>>>  ", local) 


print ('---------Formated Time---------------\n')

locall = time.asctime()
print ("Current time : >>>  ", locall)


print ('\n')
print ('\n')
print ('---------Calender---------------\n')

import calendar

cal = calendar.month(2019,1)
print ("Here is the calender: \n")
print (cal)







