# -*- coding: utf-8 -*-
"""
An object has two characteristics:
  
 1. attributes
 2. behavior
Let's take an example:
  Parrot is an object,

  1. name, age, color are attributes
  2. singing, dancing are behavior
  
 ## -------Class ---------
 A class is a blueprint for the object.
 
  ## -------Object ---------
  An object (instance) is an instantiation of a class. 
  When class is defined, only the description for the object is defined. 
  Therefore, no memory or storage is allocated.
  
"""

my_student = {
    'name' : 'Golam Maulla',
    'grades' : [50, 60, 88, 99]
    
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])
    
 ##print(average_grade(my_student))

class Student: ##'Class' keyword /// class name start first word upper case
    def __init__(self, new_name, new_grade):  ## -- donder function 3 parameter
        self.name = new_name ## -- Self is enpty object
        self.grades = new_grade ## self.grade is not veriable it's property of self
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Golam Mauulla', [50, 60, 88, 99])
student_two = Student('keya', [55, 77, 88, 99])

print(student_one.__class__)
print(student_one.name)
print(student_two.name)

print(student_one.average())
print(student_two.average())

print(Student.average(student_one))


"""
---------Parameter Naming --------
"""

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
matrix = Movie('Matrix', 1994)

print(matrix.year)

"""
--------- Magic Method in python -------
"""

class Garage:
    def __init__(self):
        self.cars = []
      
    def __len__(self):
        return len(self.cars)

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.Garage('Focus')

print(len(ford))






