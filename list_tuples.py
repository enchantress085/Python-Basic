"""
List Tuples 

List = [] insert another list value  using .append
tuple = () Insert another tuple value using +tuple_value
set = {} Unordered and also removing duplicate .add
"""
list_variables = ['Hello', 'Hi', 'Nice to meet you']
tuple_variables = ('Hello', 'Shaju', 'Raju')
set_variables = {'Hello', 'HI', 'Nice o meet you'}

print(list_variables) 
print(tuple_variables) 
print(set_variables) 

print(list_variables[1]) # called a subscript
print(tuple_variables[2])


list_variables.append('Golam Maulla')
print(list_variables)

tuple_variables = tuple_variables + ('Golam Maulla',)
print(tuple_variables)

set_variables.add('Golam Maulla')
print(set_variables)













