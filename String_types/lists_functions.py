# -*- Built-in List Functions


"""
If elements are of the same type, perform the compare and return the result. 
If elements are different types, check to see if they are numbers.

  1. If numbers, perform numeric coercion if necessary and compare.

  2. If either element is a number, then the other element is "larger" 
  (numbers are "smallest").
  3. Otherwise, types are sorted alphabetically by name.
  
  If we reached the end of one of the lists, the longer list is "larger."
  If we exhaust both lists and share the same data, the result is a tie,
  meaning that 0 is returned
"""
print ("----------------------------------")




list1 = ['shaju', 'raju', 'swikat', 'rakib']
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
 

print ("---------List append method -------------")

"""
The method append() appends a passed obj into the existing list
"""

list1.append(list2) 
print(list1)

print ("----------------------------------")


""" ---- insert functions two values
1st index number 
2nd values 
""" 

list1.insert(1, 'vong')
print (list1)

print ("----------------------------------")

""" ==================
   extend functions for lists 
   extend another list values added values sequentialy
=================="""

list3 = ['shaju', 'raju', 'swikat', 'rakib']
list4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list3.extend(list4)
print (list3)

print ("----------------------------------")

"""===================================
      remove and pop function for lists 
================================"""


list5 = ['huu', 'math', 'physics', 'compc']
list5.remove('physics') #---- remove values in lists 
print (list5)

print ("----------------------------------")

sss = list5.pop() # --- lists last value remove the list
print (sss)

print ("----------------------------------")

list5 = ['huu', 'math', 'physics', 'compc']
list5.reverse() # -----lists reverse function

print ("----------------------------------")

list4.sort() #---- Any list assiending orderd shorted  
list4.sort(reverse=True) #---- Any list desending orderd shorted 
print (list4)

print ("----------------------------------")

list5.sort(reverse=True)
print (list5)

print ("----------------------------------")

print (min(list4))
print (max(list4))

print ("----------------------------------")

"""
    list.index(x[, start[, end]])
    Return zero-based index in the list of the first item whose value is x.
    Raises a ValueError if there is no such item.
"""
print (list5.index('math'))

print ("----------------------------------")
 
print ('shaju' in list3) #--- search a value in list and result boolean type (true or false)

print ("----------------------------------")












 