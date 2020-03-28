"""

Each key is separated from its value by a colon (:), 
the items are separated by commas, and the whole thing is enclosed 
in curly braces. An empty dictionary 
without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. 
The values of a dictionary can be of any type, but the keys must 
be of an immutable data type such as strings, numbers, or tuples.

"""

print ("-----------------Dictionary------------- \n")

di = {'shaju': 'Golam Maulla', 'rakib': 'Rakib Hasan', 'raju': 'Lutfar Rahman Razu', 'swikat': 'Mahamudul Hasan Swikat' };
print ("Dictionary['shaju'] = ", di['shaju'])
print ("Dictionary['rakib'] = ", di['rakib'])


print ("--------------Updating Dictionary------------- \n")

di['shaju'] = 'MD. Golam Maulla Shaju'
di['shovon'] = 'Ashiqur Rahman Shovon'

print ('Updating Result = ', di['shaju']) # ------ update existing entry
print ("\n")
print ('Add new data Full dictionary = ', di) #-------Add new entry

print ("--------------Delete Dictionary------------- \n")

del di['shaju'] #remove entry with key 'shaju'
print ("Dictionary :> ", di)

di.clear() #--------- remove all entries in dictionary
print ("Dictionary clear :> ", di)

#del di
#print ("Dictionary delete :> ", di) #dictionary delete

print ("-----Exceptional Dictionary use ---------")



"""
More than one entry per key is not allowed. This means no duplicate 
key is allowed. When duplicate 
keys are encountered during assignment, the last assignment wins.
"""

#dic = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
#print ("di['name'] = ", dic['Name'])









