"""
Dictionary Different type method :>>> clear(), copy(), fromkeys(),
get(key, default=none), has_key(), items(), keys(), 
setdefault(key, default=none), udate(), values()


The method fromkeys() creates a new dictionary with keys from seq 
and values set to value.

Syntax

dict.fromkeys(seq[, value]))

Parameters
 1.seq − This is the list of values which would be used for 
   dictionary keys preparation.

 2.value − This is optional, if provided then value would be set to this value

Return Value
This method returns the list.

"""

print ("---------- fromkeys()--------- \n")

se = {'shaju', 'age', 'gender'}
di = dict.fromkeys(se)
print ("New Dictionary : %s" % str(di))

di = dict.fromkeys(di, 21) # ---- Interger value pass
print ("New Dictionary : %s" % str(di))

di = dict.fromkeys(di, 'Ahhhh') # ---- String value pass
print ("New Dictionary : %s" % str(di))


print ("---------- get()--------- \n")
"""
The method get() returns a value for the given key. 
If key is not available then 
returns default value None.

Syntax

dict.get(key, default=None)

Parameters
key − This is the Key to be searched in the dictionary.

default − This is the Value to be returned in case key does not exist.

Return Value
This method return a value for the given key. If key is not available, then returns default value None.
"""

print ("Value : %s" % di.get('shaju'))
print ("Value : %s" % di.get('Rakib'))


print ("---------- has_key()--------- \n")
#The method has_key() returns true if a given key is 
#available in the dictionary, 
#otherwise it returns a false.

#dict = {'s': 'p', 'w': 'q'}
#print ("Values : %s" % dict.has_key('s')) #----------Problem



