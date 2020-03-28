# -*- coding: utf-8 -*-
"""
In Python, function is a group of related 
statements that perform a specific task.

Functions help break our program into smaller and modular chunks. 
As our program grows larger and larger, functions make it more 
organized and manageable.Furthermore, it avoids repetition 
and makes code reusable.
"""
def greet():
    name = (input('Enter your name: '))
    print(f'Hello, {name}')
    
print('Before the function. ')

greet() # call the function.
print('Hello')

# ==========>>>


def check_fun(limit):       
    for n in range(2, limit):   #-- n is called argument 
        check_if_prime(n)
        

def check_if_prime(number):   #--- number is called parameter  
    for x in range(2, number):
        if number % x == 0:
            print(number, 'Equals', x, '*', number//x)
            break
        else:
            print(number, 'is a prime number')
            
            
check_fun(10)











