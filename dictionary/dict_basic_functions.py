"""
The method cmp() compares two dictionaries based on key and values.

Syntax

cmp(dict1, dict2)

Parameters
dict1 − This is the first dictionary to be compared with dict2.

dict2 − This is the second dictionary to be compared with dict1.

Return Value
This method returns 0 if both dictionaries are equal, 
-1 if dict1 < dict2 and 1 if dict1 > dic2.
"""
print ("-----------Dictionary cmp ---------\n") # ---- Problem this functions
"""
dict1 = {'Name': 'shaju', 'Age': 7};
dict2 = {'Name': 'swikat', 'Age': 27};
dict3 = {'Name': 'Raju', 'Age': 27};
dict4 = {'Name': 'shaju', 'Age': 7};

print ("return value : %d" %d cmp(dict1, dict2))
"""



"""
The method len() gives the total length of the dictionary. 
This would be equal to the number of items in the dictionary.
"""

print ("-----------Dictionary length ---------\n")
di = {'shaju': 'Golam Maulla', 'rakib': 'Rakib Hasan', 'raju': 'Lutfar Rahman Razu', 'swikat': 'Mahamudul Hasan Swikat' };
print ("Length : %d" % len(di))

print ("-----------Dictionary String str() ---------\n")

print ("Equivalent String : %s" % str(di))
print ("Type of Dictionary : %s" % type(di))













