# -------For Loops

"""
-----------Syntex --------
for <variable> in <sequence>:
	<statements>
else:
	<statements>

"""

print ("---------For Loop---------")

flist = ["Shaju", "Rakib", "Shovon", "Ryhan"]
for p in flist:
  print (p)
  
print ("---------Break loop---------")

"""
If we call the following script, we get the following result: 
--------- 

Great, delicious ham
No more spam please!
Finally, I finished stuffing myself

----------

Removing "spam" from our list of edibles, we will gain the following output:
  
----------- 
Great, delicious ham
Great, delicious eggs
Great, delicious nuts
I am so glad: No spam!
Finally, I finished stuffing myself
-----------

"""





fl = ["Luduls", "egg", "coffe", "humba"]
for food in fl:
  if food == "egg":
    print ("No more spam pls!")
    break
  print ("Great " + food)
else:
  print ("I am so glad :> no spam")
print ('Finally i finished')

print ("--------------------------------")
#fl = ["Luduls", "egg", "coffe", "humba"]
for food in fl:
  if food == "egg":
    print ("No more this food", food)
    continue
  print ("Great", food)
else:
  print("i am so glad ")
print ("finally")
  
  
  
  
  
  


#print ("---------Break loop---------")



