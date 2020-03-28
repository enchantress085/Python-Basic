"""
The built-in function range() is the right function to iterate over a 
sequence of numbers.
It generates an iterator of arithmetic progressions: 

--------------
range(10)
range(0, 10)
list(range(10))
-------------------

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

-------------------------------
range(n) generates an iterator to progress the integer numbers starting 
with 0 and ending with (n -1). To produce the list with these numbers, 
we have to cast range() with the list(), 
as we did in the previous example. 
range() can also be called with two arguments:
----------------
range(begin,end)
----------------
The above call produces the list iterator of numbers starting with begin 
(inclusive) and ending with one less than the number "end". 

-----------------
range(4,10)
range(4, 10)
list(range(4,10))
-------------------

[4, 5, 6, 7, 8, 9]
--------------------


So far the increment of range() has been 1. We can specify a different
increment with a third argument. The increment is called the "step".
It can be both negative and positive, but not zero:
----------------------
range(begin,end, step)
-----------------------

list(range(4,50,5))
[4, 9, 14, 19, 24, 29, 34, 39, 44, 49]
---------------------------


It can be done backwards as well:
--------------------
list(range(42,-12,-7))
[42, 35, 28, 21, 14, 7, 0, -7]
------------------------
The range() function is especially useful in combination with the for loop,
as we can see in the following example. The range() function 
supplies the numbers from 1 to 100 for the for loop to calculate the 
sum of these numbers:
n = 100

sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print("Sum of 1 until %d: %d" % (n,sum))

"""

from math import sqrt

print ("============ Range Function =============")


b = list(range(0,50,5))
print ("  ", b)

# ---- Range backward work 

c = list(range(0,-12,-3))
print(c)


print ("============ Range calculations===========")

n = 100

sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print("Sum of 1 until %d: %d"%(n,sum))


print ("============= problem math calculation =========")

n = int (input ("Maximal number :"))
for a in range(1, n+1):
  for b in range(a,n):
    csqure = a**2 + b**2
    c = int(sqrt(csqure))
    if ((csqure - c**2)==0):
      print (a,b,c)

print("=========================")

fi = [1, 2, 3, 4,20, 6, 7, 80, 99,98,23,65]
for i in range(len(fi)):
  print(i,fi[i])
print("-----------")


print("=========================")

color = ["Blue"]
for i in color:
  if i == "Blue":
    color += ["Black"]
  if i == "Black":
    color += ["White"]
print(color)









