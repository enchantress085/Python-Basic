"""
These functions are called anonymous because they are not declared 
in the standard manner by using the def keyword. You can use the lambda 
keyword to create small anonymous functions.

  1.Lambda forms can take any number of arguments but return just 
    one value in the form of an expression. They cannot contain commands 
    or multiple expressions.

  2.An anonymous function cannot be a direct call to print because 
    lambda requires an expression.

  3.Lambda functions have their own local namespace and cannot access 
    variables other than those in their parameter list and those in the 
    global namespace.

  4.Although it appears that lambdas are a one-line version of a 
    function, they are not equivalent to inline statements in C or C++, 
    whose purpose is to stack allocation by passing function, during 
    invocation for performance reasons.
    
"""
print("-----------Anonymous Functions----------")

#----Functions defination is here 
sum = lambda a1,a2,a3 : a1+a2+a3

#--------call sum as afunctions
print("Value of total :> ", sum(20,30,67))
print("")













