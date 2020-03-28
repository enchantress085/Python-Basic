"""
There is a popular time module available in Python, 
which provides functions for working with times and for 
converting between representations. Here is the list of all 
available methods

Functions :>>> altzone(), asctime([tupletime]), clock(secs), ctime(secs), 
gmtime([secs]),

localtime([secs]), mktime([tupletime]), #-- Practise korte hbe 
sleep([secs]), strftime(fmt[,tupletime]), #-- Practise korte hbe
strptime(str,fmt = '%a %b %d %H:%M:%S %Y'),time(),tzset() #--Practise korte hbe

"""
print("\n")
print("---------altzone()-------------")

"""
The method altzone() is the attribute of the time module. 
This returns the offset of the local DST timezone, in seconds
west of UTC, if one is defined. This is negative if the local 
DST timezone is east of UTC (as in Western Europe, including the UK). 
Only use this if daylight is nonzero.
"""
import time

print ("time.altzone() : ", time.altzone)

print("\n")
print("---------clock()-------------\n")

"""
The method clock() returns the current processor time as a 
floating point number expressed in seconds on Unix. The precision 
depends on that of the C function of the same name, but in any case, 
this is the function to use for benchmarking Python or timing algorithms.

On Windows, this function returns wall-clock seconds elapsed 
since the first call to this function, as a floating point number, 
based on the Win32 function QueryPerformanceCounter.

Syntax

time.clock()

Parameters
NA

Return Value
This method returns the current processor time as a floating 
point number expressed in seconds on Unix and in Windows it 
returns wall-clock seconds elapsed since the first call to this 
function, as a floating point number.
"""

def procedure():
  time.sleep(2.5)
  #------- Measure process time
t1 = time.clock()
procedure()
print (time.clock() - t1, "second process time")

t1 = time.time()
procedure()
print (time.time() - t1,"second wall time")


print("\n")
print("---------ctime()-------------\n")

"""
The method ctime() converts a time expressed in seconds since 
the epoch to a string representing local time. If secs is not 
provided or None, the current time as returned by time() is used. 
This function is equivalent to asctime(localtime(secs)). 
Locale information is not used by ctime()
"""

print ("ctime : ", time.ctime())

print("\n")
print("---------gmtime()-------------\n")

"""
The method gmtime() converts a time expressed in seconds 
since the epoch to a struct_time in UTC in which the dst 
flag is always zero. If secs is not provided or None, 
the current time as returned by time() is used.
"""
#sec − These are the number of seconds to be converted 
#into structure struct_time representation .<1455508609.34375>

print ("gmtime : ", time.gmtime(1455508.343757457457))













