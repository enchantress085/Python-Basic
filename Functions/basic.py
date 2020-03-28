"""
A function is a block of organized, reusable code that is used to 
perform a single, related action. Functions provide better 
modularity for your application and a high degree of code reusing.

 
These functions are called user-defined functions.

Defining a Function:
  
You can define functions to provide the required functionality. 
Here are simple rules to define a function in Python.

 1.Function blocks begin with the keyword def followed by the 
   function name and parentheses ( ( ) ).

 2.Any input parameters or arguments should be placed within 
   these parentheses. You can also define parameters inside these parentheses.

 3.The first statement of a function can be an optional 
   statement - the documentation string of the function or docstring.

 4.The code block within every function starts with 
   a colon (:) and is indented.

 5.The statement return [expression] exits a function, optionally 
   passing back an expression to the caller. A return statement with 
   no arguments is the same as return None.
"""


print("\n")
print ("------------Functions--------------\n")
#------ define function
def shaju(tut):
  ""
  print (tut)
  return

shaju("Shaju is a good boy. ")
shaju("Amk dea keccu hbe nah .........!!")


print("\n")
print ("----------Pass reference vs value-----------\n")

#------ define function
def me( mylist ):
  ""
  print("Values inside the functions before change : ", mylist)
  mylist[5]= 67
  print("Values inside the functions after change : ", mylist)
  return

#--------------- call me funtions 
  
mylist = [9, 8, 7, 6, 5, 4]
me(mylist)
print("Values outside the functions : ", mylist)

print("\n")
print ("----------another Pass reference vs value-----------\n")

def cngme(myl):
  ""
  myl = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print ("values inside the functions : ", myl)
  return

myl = [10,20,30,40,50,60,70,80,90]
cngme(myl)
print ("Values outside the functions : ", myl)




















