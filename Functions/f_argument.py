"""
You can call a function by using the following 
types of formal arguments −

 1.Required arguments
 2.Keyword arguments
 3.Default arguments
 4.Variable-length arguments
"""

print("\n")
print("--------Required arguments-------\n")

def me(st):
  print ("Print : ", st)
  return

me("MD. Golam Maulla Shaju")

print("\n")
print("--------Keyword arguments-------\n")

def me1(st):
  print ("Resulr print : ",st)
  return

me1(st = 'GM Shaju')

print("--------@nd-------\n")

def me2(name,institute):
  print ("print name : ",name)
  print("print institute : ",institute)
  return


me2('Shaju', 'Daffodil International Univercity')

print("\n")
print("--------Default arguments-------\n")

def meinfo(name, age = 22):
  print ("Name : ",name)
  print ("age : ",age)
  return

meinfo('shaju', 21)
meinfo('Rakib')

print("\n")
print("--------Variable length arguments-------\n")


def printinfo(arg, *vartuple):
  print("Output is : ")
  print(":>",arg,"\n")
  for var in vartuple:
    print(":>",var,"\n")
  return

printinfo('shaju')
printinfo('Raju', 'Rakib', 'Shovon', 'Janena')


















