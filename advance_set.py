"""
A set is an unordered collection of items. 
Every element is unique (no duplicates) and 
must be immutable (which cannot be changed).
However, the set itself is mutable. 
We can add or remove items from it.
Sets can be used to perform mathematical set 
operations like union, intersection, 
symmetric difference etc.
"""


# ----- Empty set

a = {}
print(type(a))

a = set()
print(type(a))

# -- change a set
my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

# Multiple elements add
my_set.update([4,5,6])
print(my_set)

# -- add list and set
my_set.update([7,8], {9,10})
print(my_set)

"""
Set Union, Intersection , Difference, Symmetric Difference


"""
# --- set union
set_one = {1,2,3,4,5}
set_two = {1,3,5,7,9,11}

#print(set_one.union(set_two))
print(set_one | set_two)
# -- set intersection
#print(set_one.intersection(set_two))
print(set_one & set_two)

#-- set difference
#print(set_one.difference(set_two))
print(set_one - set_two)




















