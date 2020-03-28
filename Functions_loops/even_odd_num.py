# -*- coding: utf-8 -*-
"""
Odd or even Number using for loops 
"""
for n in range(1, 20): #-- [2,3,4,5,6,7,8,9.....]
    for x in range(2,n):#-- [],[2],[2,3],[2,3,4]....
        if n % x == 0:
            print(f'{n} Equals {x} * {n//x}  >')
            break
    else:
        print(f"{n} is a prime Number  >")





#-- Even Number 
        
for num in range(1, 30):
    if num % 2 == 0:
        print(f"Found an even number, {num} ")
        continue
    print(f"Found a number, {num}")
    
    
    
    
    

"""

#-- IF statement Even or odd using format 
format() method returns the formatted string.

  format() method takes any number of parameters. 
  But, is divided into two types of parameters:

Positional parameters - list of parameters that can 
                        be accessed with index of 
                        parameter inside 
                        curly braces {index}
Keyword parameters - list of parameters of type 
                      key=value, that can be accessed 
                      with key of parameter inside curly 
                      braces {key}
                      
                      
"""

num = int(input("Enter a number: "))
if num %2 == 0:
    print("{0} is even ".format(num))
else:
    print("{0} is Odd".format(num))






