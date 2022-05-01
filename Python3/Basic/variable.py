#basic variable types and respective casting
varInt = int(5)
varInt = int('5a', 16) # converts hex string into a number
varInt = 0xA # Hex notation for a number
varInt = 0b1010 # Binary notation for a number
varInt = 0o10 # Octal notation for a number

varReal = float(5.0)

varString = 'hello' # single quotes and double quotes can be used interchangeably, *AS LONG AS* you use the same type of quotes to open and close the string
varString = "hello"
varString = str("hello") # note: strings are not mutable
varChr = chr(65) # char doesn't exist in python, they are just a standard string of len 1

varBool = bool(True)

varBytes = b"test" # this creates a byte array, note: byte arrays are not mutable
varBytes = bytes(5) # this will actually create a byte array 5 bytes long all initalized to zero
varBytes = bytes('test', 'utf-8') # this will cast a string to a byte array with a specific encoding


varList = [] # an empty list
varList = [1, 2, 3, 4, 5] # arrays are zero indexed
varList = [(i) for i in range(8)] # a way to generate and initialize an array (see list comprehensions https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions )
varList = [i for i in range(8) if (i%2 == 0)] # a conditional list comprehension, will only include elements that satisfy the condition
varList = list([1, 2, 3, 4])
print(varList[0])

varTuple = (1, 2, 3) # tuples are like an array, elements in a tuple are nonmutable, but they can contain elements that are mutable (lists)
varTuple = 1, 2, 3 # another way to initialize a tuple
varTuple = (1) # for the single element case, this doesn't work to create a tuple
varTuple = (1,) # following the element with a comma does create a single element tuple
varTuple = tuple((1,))
print(varTuple[0])

varDic = {} # an empty dictionary
varDic = {1:'s', 3:'4', 't':'a'} # a dictionary
varDic = {i : chr(65 + i) for i in range(10)} # list comprehensions also works with dictionaries
varDic = dict({1:'s', 3:'4', 't':'a'})
print(varDic['t'])

#TODO add in some unicode stuff
print("=======================================================================")

'''
#TODO
Random stuff that needs organizing
'''
varInt, varReal = 6, 6.0 # python supports multivariable assignments

_ = 'test' # this is a valid variable name, and the convention is to use it as null assignment. IE: assign a value to variable '_' to discard that value
a, _, c = [1,2,3] # an example of a good use, discarding the second list element
print(a, c)

print("=======================================================================")

#Variable Annotations https://www.python.org/dev/peps/pep-0526/
#variable typing, python allows typing hints that IDEs and type-checkers can enforce, BUT it is not enforced at runtime
varInt : int = 5
varInt = 'notInt' # IDEs and type-checkers can enforce typing and throw an error, but this line will not throw an error during runtime
varStr : str # can work for uninitialized variables
varList : list = [1, 2, 3, 4]
varDic : dict = {}
varDic : 'random' = {} # can also use strings for annotations, but will show up as a warning in a type-checker and IDE

#for more advanced annotating, requires importing the 'typing' module
# https://www.pythonsheets.com/notes/python-typing.html
from typing import List, Tuple
varList : List[int] = [1, 2, 3, 4]
varList : Tuple[int, ...] = [1, 2, 3, 4] # Note: the ellipsis only works for Tuple, not for List

#TODO creating types
# https://docs.python.org/3/library/typing.html#typing.Generic
# https://docs.python.org/3/library/typing.html#typing.TypeVar
print("=======================================================================")

# https://docs.python.org/3/tutorial/datastructures.html#sets
#more examples below of how to use sets
varSet = set() # an empty set
varSet = set('abcdddde') # a set, holds an unordered set of unique elements (no duplicates)
varSet = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6}
#print(varSet[0]) # you can't access sets like this
print(varSet) # note the duplicate elements are not printed
print("=======================================================================")

#multidimensional arrays aren't exactly standard in python, but can be made using an array of an array
# Note: add-ons for python (numpy) allows support for large multidimensional arrays
varArray2D = [[None for j in range(8)] for i in range(8)] # an example of making a two dimensional with all elements initilized to None, using 'list comprehensions'
print(varArray2D[0][0])
print("=======================================================================")

import copy
varArray2Db = copy.deepcopy(varArray2D) # instead of copying the reference of varArray2D, deepcopy(x) makes a complete element by element copy of x, etc...
print("=======================================================================")

#list slices
varList = [1, 2, 3, 4, 5]
print(varList[:2]) # starts from the begining of the list to element 2
print(varList[-2:]) # starts from seconds last element of list to last element
print(varList[2:]) # starts from element 2 to end of list

print(varList + [6, 7, 8, 9]) # can concatinate lists
varList.append(6)

# some useful list methods
varList = [1, 2, 3, 4, 5]
varList.append(6) # appends something to the end of the list
varList.insert(0, 0) # at xth index, insert y
print(varList.pop()) # removes and returns last element of list
print(varList.pop(0)) # removes and returns xth element of list
print(varList.index(5)) # searches for x in list, returns index. Raises error if x isn't in list
del varList[0] # 'del' can be used to delete a single element
del varList # 'del' can also be used to delete an entire variable
print("=======================================================================")

#list comprehensions example from https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
example1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y] #this is equivalent to the below example2
print(example1)
example2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            example2.append((x, y))
print(example2)

print([i for i in range(8) if (i%2 == 0)]) # a conditional list comprehension, will only include elements that satisfy the condition
# both 'example1' and 'example2' are identicle
print("=======================================================================")

#sets 
# https://docs.python.org/3/tutorial/datastructures.html#sets
set1 = {1, 2, 3, 4, 4, 4, 3, 3, 2, 1, 1}
set2 = {0, 1, 8, 9}
# some set operations
print(set1 - set2) # lists stuff in set1 that is NOT in set2
print(set1 | set2) # or
print(set1 & set2) # and
print(set1 ^ set2) # xor
for i in sorted(set1): # a way to loop over a set, note: sorted returns a lists containing elements in the set, but leaves set unchanged
    print(str(i))
print("=======================================================================")

#dictionaries
dic1 = {1:"test", 2:"ing", 3:"over"}
print(dic1.keys()) # returns the keys, but is unsorted/indexing not supported (not a list) (but you can still iterate over it in a for loop)
print(list(dic1.keys()))
print(sorted(dic1.keys()))
for i,j in dic1.items(): # when looping over a dictionary, can use this to get both the key and data at the same time
    print("dic key '" + str(i) + "' contains data '" + str(j) + "'")
print("=======================================================================")
    
#some stuff on bytes
import sys
print((5).to_bytes(2,sys.byteorder)) # can convert an int to n many byte
print(bytes([10])) # alternativly, you can use this, since 'bytes' is supposed to work on iterables
print(bytes([10, 20, 30, 40]))
print(bytes(10)) # be carefull, this will actually make an array n bytes long instead of converting it
print((bytes([2, 4, 6, 8, 10, 12, 14, 16])).hex()) # convert byte array to hex string
print("=======================================================================")

#Python Dataclasses using Dataclass decorator #TODO
# https://www.youtube.com/watch?v=vRVVyl9uaZc (If you're not using Python DATA CLASSES yet, you should 🚀)
