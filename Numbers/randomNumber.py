"""
Random numbers are used for games, simulations, testing, security, 
and privacy applications.
Python includes the following functions that are commonly used.
"""

print ("----------choice()-----------\n")
# ---The choice() method returns a random item from a list, tuple, or string.---

"""
Parameters
seq − This could be a list, tuple, or string.

Return Value
This method returns a random item.
"""

import random # --- import the random module ---
li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
st = 'I love my family'

print ("Returns a random number from range(200) =", random.choice(range(200)))
print ("Returns a element from list             = ", random.choice(li))
print ("Returns random character from string    = ", random.choice(st))


print ("----------randRange()-----------\n")

#The randrange() method returns a randomly 
#selected element from range(start, stop, step).

"""
Parameters

 1.start − Start point of the range. This would be included in the range. 
   Default is 0

 2.stop − Stop point of the range. This would be included in the range.
   Default is 1

 3.step − Step point of the range. This would be excluded from the range.

Return Value
This method returns a random item from the given range.

"""
# randomly select an odd number between 1-200
print ("randrange (1, 200, 2) = ", random.randrange(1,200, 2))

# randomly select a number between 0-99
print ("randrange (200)       = ", random.randrange(200))

print ("----------random()-----------\n")

#----- The random() method returns a random floating point 
#----- number in the range [0.0, 1.0].
"""
Parameters
NA

Return Value
This method returns a random float r, such that 0.0 <= r <= 1.0

"""

print ("first random()  = ", random.random())

print ("Second random() = ", random.random())

print ("----------Number seed()-----------\n")

"""
The seed() method initializes the basic random number generator. 
Call this function before calling any other random module function.

Parameters
x − This is the seed for the next random number. If omitted, 
then it takes system time to generate the next random number. 
If x is an int, it is used directly.

y − This is version number (default is 2). 
str, byte or byte array object gets converted in int. 
Version 1 used hash() of x.

Return Value
This method does not return any value.

Syntex

seed ([x], [y])

"""
random.seed()
print ("random number with default seed = ", random.random())

random.seed(5)
print("random number with int seed = ", random.random())

random.seed("hello",2)
print ("random number with string seed", random.random())

#--- output number change where change upper or lower case 
random.seed("Shaju",5)
print ("random number with string seed", random.random())

#--- output number change where change upper or lower case 
random.seed("shaju",3)
print ("random number with string seed", random.random())

print ("----------Shuffle()-----------\n")

"""
The shuffle() method randomizes the items of a list in place.

Syntax:
  
shuffle (lst,[random])
Note − This function is not accessible directly, 
so we need to import shuffle module and then we need to 
call this function using random static object.

Parameters
 1.lst − This could be a list or tuple.

 2.random − This is an optional 0 argument function returning 
   float between 0.0 - 1.0. 
   Default is None

Return Value
This method returns reshuffled list.

"""

l1 = [90, 80, 70, 60, 50, 40, 30, 20, 10, 00]
l2 = ['shaju', 'Rakib', 'Swikat', 'Raju', 'Shovon']
random.shuffle(l1)
print("Reshuffled list = ", l1)

random.shuffle(l2)
print("Reshuffled list = ", l2)

print ("----------uniform()-----------\n")

"""
The uniform() method returns a random float r, 
such that x is less than or equal to r and r is less than y.

Syntax

uniform(x, y)
Note − This function is not accessible directly, 
so we need to import uniform module and then we need to 
call this function using random static object.

Parameters
x − Sets the lower limit of the random float.

y − Sets the upper limit of the random float.

Return Value
This method returns a floating point number r such that x <= r < y.

"""
print ("Random float uniform(5, 10)", random.uniform(5, 10))
print ("Random float uniform(10, 10)", random.uniform(7, 140))



