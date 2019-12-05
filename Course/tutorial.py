#
# author: F. Coppo
# decription: python fast basic course
#

"""
 VARIABLE TYPE
"""
print("***************")
print("VARIABLE TYPE")
print("***************")
a, b = 3 , 4 			# simultaneous assignment 
floatC = 7.0
print(a, b, floatC)
floatC = float(7) 		# floatC = 7.0
if isinstance(floatC, float) and floatC == 7.0 :  # check the variable type using isinstance method
	print("Float", floatC)

"""
 STRING
"""
print("***************")
print("STRING")
print("***************")
name = None
print("String:") 		# both single or double quotes is allowed
name = 'my name is '
name += 'FC'            # NOTE: operators between numbers and strings is not supported
print(name)
name = 'FC'
print("my name is %s" % name)
print("lengh of my name is %s" % len(name))
print("the index of surname is %d" % name.index('C'))

"""
	LIST: a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas;
	it can have any number of items and they may be of different types a list can even have another list as an item
"""
print("***************")
print("LIST")
print("***************")
mylist = []				# list declaration
mylist.append(9.2)		# 'append' is method to add single item to the endo of the list
mylist.append(3**2)		# 3^2
mylist.append("Third element")
print("length of mylist is %s" % len(mylist))
print(mylist[1]) 		# print first element
for x in mylist:		# list can be iterated
   	print(mylist*2)     # print the list using operator (duplication) with list
a = object()			# return an empty object
aList = [a] * 10 		# aList contains 10 instance of a 

"""
	LIST COMPREHENSIONS
	square braket with expression or loops
"""
print("***************")
print("LIST COMPREHENSIONS")
print("***************")
squareListComprehension = [n**2 for n in range(10)] # print n^2 0 to 9 
print(squareListComprehension)
num = [35.6, 23.4, -34.9, 58.3, 6, 18.6]
newlist = [n for n in num if n > 30]          # print only  number grater than 30 
print(newlist)

"""
	SETS
	list with no duplicate entries
"""
print("***************")
print("SETS")
print("***************")
a = set(["Jake", "John", "Jake"])
b = set(["John", "Jill"])
print(a)     					# {'John', 'Jake'}
print(a.intersection(b))		# {'John'}
print(a.symmetric_difference(b))# {'Jill', 'Jake'}
print(a.union(b))				# {'John', 'Jake', 'Jill'}

"""
	The "IN" operator: it should be used to check if a specified object exists within an iterable object container (i.e list)
"""
print("***************")
print("IN OPERATOR")
print("***************")
mylist.append("banana")
label = "banana"
if label in mylist:
    print("found %s in following list %s" % (label, mylist))

"""
	LOOPS
"""
print("***************")
print("LOOPS")
print("***************")
# for
for x in range(5, 7):
    print(x)  # 5 6
	
num = [1,2,5,6,89,7] 
for num in num:
    if num == 7:
        break

    if num % 2 == 1:
        continue
    print("num is %d" % num)
	
# while
end = False
cnt2 = 0
while end == False:
	print("I am into main loop!")
	while True:
		cnt2 += 1
		if (cnt2 >= 3):
			print("exit from second loop!")
			end = True
			break
else:                             # you can use else into while loop!
	print("exit from main loop!")			

"""
 FUNCTION 
 functions are the first class objects!
"""  
print("***************")
print("FUNCTION")
print("***************")
def summer(a, b):
    return a + b
print("sum result is %d" % summer(4,5))

# multiple function argument
def functionVariadic(a, b, * theRest):
	myList = [a + b, theRest[0] ]
	return myList
list  = functionVariadic(1,2, ["abc", 2], 4, 7)
print("variadic funct %s " % (list) )

"""
 PARTIAL FUNCTION 
"""  
print("***************")
print("PARTIAL FUNCTION")
print("***************")

from functools import partial
def operation(u,v,w):
    return u*4 + v*3 + w*2
# it allow one to derive a function with n parameters to a function with fewer parameters
partialOperation = partial(operation,1,1) # partial( function, param1,param2 ..)
print(partialOperation(2))

"""
 CLOSURE 
 A function object that remembers variable values in enclosing scopes even if they are not present in memory 
 The variable is  readonly unless using  "nonlocal" keyword
"""
print("***************")
print("CLOSURE")
print("***************")

def mainFunction(a, b):
    "This is the enclosing function"
    def nestedFunction():
        "The nested function"
        print("a = %d; b = %d" %(a, b))
    nestedFunction()
	
mainFunction(1, 2)

"""
 CLASSES AND OBJECT
"""     
print("***************")
print("CLASSES and OBJECT")
print("***************")
class Car:
	def __init__(car, license):       # car is like this pointer in C++
		car.__license_plate = license # ___ is for private, _ is for protected
		print("car with license plate: %s has been created" % car.__license_plate)
	__engineOn = False
	def runEngine(car, key):
		if (car.__engineOn != key):
			if (key == True):
				print("engine on!")
			else:
				print("engine off")
		car.__engineOn = key
	publicLabel = 2          # public member 
myCar = Car("NEW_YORK_1234") #  car instance
myCar.runEngine(True)        # obj method calling
myCar.runEngine(True)
myCar.runEngine(False)

"""
 DICTIONARY: key instead of index (can be of any type of object (a string, a number, a list);
 dictionary is collection of key-value pairs: is an associative array:

	d = {
    <key1>: <value1>,
      .
    <keyN>: <valueN>
}
"""
print("***************")
print("DICTIONARY")
print("***************")
myLeague = {
	# city ....team.......money [k]  trophy
	"Turin": ["Juventus", 		500,  13],
	"Madrid": ["Real Madrid", 	700,  15],
	"London": ["Totthenam", 	600,  12],
	"Monaco": ["Bayern", 		590,  11],
	"Paris": ["PSG", 			680,  10]
		   }

myLeague.update( {'Milano' : ["Milan",470,17]} ) # add a member
myLeague.pop("Monaco")						  # clear member
myLeague.update(Turin = ["Juventus FC", 501, 14]) # update member
for city, teamData in myLeague.items(): # iteration
    print("city %s has following team %s" % (city, teamData))

"""
	MODULE
	- modules are imported from other modules using the import command: import moduleName
	- to call function of that module: "moduleName.function()" 
	- to import an objects from a specific module: from moduleName import objName as ObjNameDesired
	- to import all objects from a specific module: from modulename import *
	- the module code is executed (only once) when is loaded by a running script
	- to explore build in modules: import(os) dir(os) to explore the module's function/ obj
	- to explore build in modules: help(os.link) for routine description
"""
print("***************")
print("MODULES")
print("***************")
import os
dir(os)
help(os.link)

"""
	CODE INTROSPECTION 
"""
print("***************")
print("CODE INTROSPECTION")
print("***************")
print(type(Car)) 					  # type is a class
print(help(Car))                      # help (class public member and method)
print(dir(Car))						  # list of all attributes
print(hasattr(myCar, 'engineOn'))     # false because is private member
print(hasattr(myCar, 'publicLabel'))  # true because is public member

"""
	PACKAGE: packages are namespaces which contain multiple packages and modules themselves
	- must contain a special file called __init__.py (it indicates that the directory it contains is a Python package)
	- if you create a directory called packageName, which marks the package name, we can then create a module inside that package called packageModule:
		import packageName.packageModule   			# you must use the packageName prefix whenever we access the module bar
		from packageName import packageModule 		# not needed to use packageName prefix because we import the module to script module's namespace
"""

"""
	NUMPY array:
	- are great alternatives to lists (faster, allow calculation within entire array)
"""
print("***************")
print("NUMPY ARRAY")
print("***************")
ski = ["K2", "Salomon", "Blizzard"] # 2 new lists ski and size
ski_size = [181.65, 197.52, 195.25]
print(type(ski))
import numpy as np  # Create 2 numpy arrays from this list
np_ski = np.array(ski)
np_ski_size = np.array(ski_size)
print("ski grater than 182 cm: %s " %  (np_ski_size[np_ski_size > 182]) )    

"""
	PANDAS dataframes
	- the key data structure is called the DataFrame and allow to store and manipulate tabular data in "observations" (row) and variables (columns).
	- dataframe can be created from dictionary, from csv ( dataframe = pd.read_csv('csvFile.csv') )
example:	
	                Turin       Madrid     London Paris Milano
TeamName  Juventus FC  Real Madrid  Totthenam   PSG  Milan
Money             501          700        600   680    470
"""
print("***************")
print("PANDAS DATAFRAME")
print("***************")
# one way way to create dataframe is to use a dictionary
import pandas as pd
dataframe = pd.DataFrame(myLeague) # Pandas has assigned a key for each dictionary field (0 and 1)
print(dataframe)
dataframe.index = ["TeamName", "Money", "Trophy"] # to change index values
print(dataframe)
print("dataframe indexing:") # indexing datatframe by square bracket notation
print (dataframe['Milano']) # single bracket is column as pandas series
print (dataframe[['Milano']]) # single bracket is column as pandas dataframe
print (dataframe[['Milano', 'Turin']])
print (dataframe[1:3])	# square brackets can also be used to access observations (rows) from a DataFrame (1 and 2 observ)
print(dataframe.iloc[1]) # iloc print out observation for money (print dataset raw)
print(dataframe.loc[['Trophy', 'Money']]) # loc print out observation trophy and for money

"""
	ITERATORS
	an object is called iterable if we can get an iterator from it, where iterator is an object that can be iterated upon
"""
print("***************")
print("ITERATOR")
print("***************")
list = [1, "secondElement", 3, 4]
iterator = iter(list) # get an iterator using iter() method
print(next(iterator))  # iterate through it using next() method: 1
print(iterator.__next__()) # "secondElement"

for element in list:# for iteration
	print(element)	# iterate over any object that can return an iterator (list, string, file)

"""
	GENERATOR
	- is a simple way of creating iterators, is a function that returns an object (iterable set of items/iterators) which we can iterate over (one value at a time)
	- it is as defining a normal function with yield statement instead of a return statement
	- yield statement pauses the function saving all its states and later continues from there on successive calls
	- iterators methods like __iter__(), __next__(), StopIteration() are implemented automatically
"""
print("***************")
print("GENERATOR")
print("***************")
# A simple generator function
def generatorFunction():
    n = 1                # the value of variable n is remembered between each call unlike normal function 
    print('first')
    yield n
	
    n += 1
    print('second')
    yield n

    n += 1
    print('last but not least')
    yield n
	
for item in generatorFunction():  # we can use generators with for loops directly
     print(item)  
 
a =  generatorFunction()          # To restart the process we need to create another generator object
next(a)
next(a)

"""
	EXCEPTION HANDLING
	to avoid stopping program when exception occurred (try/except block)
"""
print("***************")
print("EXCEPTION HANDLING")
print("***************")
def printChar(c):
    print(c)
	
def manageNumber():
    tuple = ('h','e', 'l', 'l', 'o')

    for i in range(8):
        try:
            printChar(tuple[i])
        except IndexError: 
            printChar('x')
			
manageNumber()

"""
	SERIALIZATION with Json
	two basic formats for JSON data: 
	- string: mainly used to pass the data into another program or load into a datastructure
	- the object datastructure (list and dictionaries nested inside) allow one to use python methods (for lists and dictionaries)
"""
print("***************")
print("SERIALIZATION with JSON")
print("***************")
import json

myLeague['Roma'] = ["Lazio",370,10] # update dictionary

# .LOADS -> from json to python
x =  '{ "team":"Barcellona", "foundation":1970, "nation":"Spain"}'
y = json.loads(x) # y is a dictionary
print(y["nation"])  

# .DUMPS -> from python to json
y = json.dumps(myLeague)  # convert into JSO string
print(y)
