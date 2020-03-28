"""
The list is a most versatile datatype available in Python 
which can be written as a list of comma-separated values (items)
between square brackets. Important thing about a list is that items in
a list need not be of the same type
"""


list1 = ['shaju', 'rakib', 'shovon']
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print ("list value 1 : ", list1[1])
print (list2[2:5])


print("""=============updating lists values================
===================""")


print ("lists 1 available value indes 0:")
print (list1[0])

list1[0] = "Golam Maulla"
print (list1)
print (list1[0])


print("""=============Delete lists values================
===================""")

print (list1)

del list1[2]
print ("After deleting list value index 2 :")
print (list1)


