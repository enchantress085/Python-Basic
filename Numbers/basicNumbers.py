"""
Python converts numbers internally in an expression containing mixed 
types to a common type for evaluation.
Sometimes, you need to coerce a number explicitly from one type 
to another to satisfy the requirements of an 
operator or function parameter.

Type int(x) to convert x to a plain integer.

Type float(x) to convert x to a floating-point number.

Type complex(x) to convert x to a complex number with real 
part x and imaginary part zero.

Type complex(x, y) to convert x and y to a complex number with 
real part x and imaginary part y. x and y are numeric expressions.

"""


print ('Mathematical Functions : >>')
# --- The abs() method returns the absolute value of x. 
# --- the positive distance between x and zero
"""

Parameters
x − This is a numeric expression.

Return Value

This method returns the absolute value of x
"""
print ('---------abs-----------')

print ("abs (-45) = ", abs(-45))
print ("abs (100.46) =  ", abs(100.46))
#print ("abs (math.pi)= ", abs(math.pi)) ---- Problem

print ('=============================')

print ('---------Ceil-----------')

#The ceil() method returns the ceiling value of x .
#the smallest integer not less than x
"""
Note − This function is not accessible directly, 
so we need to import math module and then we need to call this function using 
the math static object.

Parameters
x − This is a numeric expression.

Return Value
This method returns the smallest integer not less than x.
"""

import math

print ("math.ceil (-45.17) = ", math.ceil(-45.17))
print ("math.ceil (100.12) = ", math.ceil(100.12))
print ("math.ceil (100.79) = ", math.ceil(100.79))
print ("math.ceil (math.pi)= ", math.ceil(math.pi))

print ('=============================')

"""
The exp() method returns exponential of x: e^x.

Note − This function is not accessible directly. 
Therefore, we need to import the math module and then we 
need to call this function using the math static object.

Parameters
x − This is a numeric expression.

Return Value
This method returns exponential of x: e^x.
"""


print ('---------exp()-----------')

print ("math.exp (-45.14)", math.exp(-45.14))
print ("math.exp (100.15)", math.exp(100.15))
print ("math.exp (math.pi)",math.exp(math.pi))

print ('=============================')
print ('---------fabs()-----------')
"""
The fabs() method returns the absolute value of x.
Although similar to the abs() function, 
there are differences between the two functions. They are −

 1.abs() is a built in function whereas fabs() is defined in math module.

 2.fabs() function works only on float and integer whereas abs() 
works with complex number also.
"""

print ("math.fabs (-45.17) =", math.fabs(-45.17))
print ("math.fabs (100.12) =", math.fabs(100.12))
print ("math.fabs (math.pi)=", math.fabs(math.pi))


print ('=============================')
print ("to be continue some functions do not practise .........")



