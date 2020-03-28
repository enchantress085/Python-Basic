# -*- coding: utf-8 -*-
"""
A while loop statement in Python programming language repeatedly executes a target statement as 
long as a given condition is true.
"""

print ("--- While Loop ---")
condition = 1
while condition <= 10:
  print(condition)
  condition += 1
  
  
#print ("--- While infinity Loop ---") 
#while True:
  #print ('doing stuff')
  
#var = 1
#while var == 1:
  #num = input('Enter a number:')
  #print ('You entered num: ', num)
  

count = 10
while count >= 0:
  if count == 0:
    print ('Booom !!!')
  else:
    print ('Count:',count)
  count -= 1
  
