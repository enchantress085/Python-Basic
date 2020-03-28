# -*- coding: utf-8 -*-





"""
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1

The left edge of the first character numbered 0. 
Then the right edge of the last character of a 
string of n characters has index n.

>>> p = ['P','y','t','h','o','n']
>>> p[2:4] = ['x','y'] # Assigned list is same length as slice
>>> p
 ['P','y','x','y','o','n'] # Result is same length
 
 -----------------
 
>>> p = ['P','y','t','h','o','n']
>>> p[3:4] = ['x','y'] # Assigned list is longer than slice
>>> p
 ['P','y','t','x','y','o','n'] # The result is longer
 
 ----------------------
 
>>> p = ['P','y','t','h','o','n']
>>> p[4:4] = ['x','y']
>>> p
 ['P','y','t','h','x','y','o','n'] # The result is longer still

"""
# p3 
friends = ['Raju', 'swikat', 'Sakib', 'Anwar', 'Abir']

print("List Slicing [1:4] => ",friends[1:4])

print("List Slicing [:-4] => ", friends[:-4])

print("List Slicing [-3:-1] => ", friends[-4:-1])

print("List Slicing [-3:] => ", friends[-3:])

print("List Slicing [:-3] => ", friends[:-3])

print("List Slicing [:2] => ", friends[:2])

print("List Slicing [2:] => ", friends[2:])


"""

List Comprehension 

"""

##-- Conditional list comprehension ============

numbers = list(range(20))
even_number = [n for n in numbers if n%2 ==0 ]
print(even_number)

#===============================


##-- String list comprehension ============

friends = ['saju', 'raju', 'Abir']
guest = ['Josh', 'Raju', 'abir', 'Michael', 'Saju']

lower_friend = [n.lower() for n in friends]

present_frnd = [name.capitalize() for name in guest if name.lower() in lower_friend]
print(present_frnd)

"""

In [26]:
present_frnd = [name.capitalize() for name in guest if name.lower() in friends]
print(present_frnd)

['Raju', 'Saju']


In [27]:
lower_friend = [n.lower() for n in friends]

present_frnd = [name.capitalize() for name in guest if name.lower() in lower_friend]
print(present_frnd)
['Raju', 'Abir', 'Saju']
"""


"""
<<<==========

Set Comprehension 

==========>>>
"""

frnd = {'Josh', 'rolf', 'Charlie' }
gust = {'anna', 'Rolf', 'josh', 'pue'}

prsent_frnd = {name.capitalize() for name in frnd & gust}
print(prsent_frnd)

"""
<<<==========

List Comprehension 
Marge to list dictionary 

==========>>>
"""
nam = ['saju', 'raju', 'swikat']
age = [23, 22, 21]

# -- t_frnd = {nam[i]: age[i] for i in range(len(nam))} # both are same 

f_frnd = dict(zip(nam, age)) # ---- both are same
print(f_frnd)



