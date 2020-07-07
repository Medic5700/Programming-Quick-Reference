#basic variable types and respective casting
varInt = int(5)
varInt = 0xA #Hex notation for a number
varReal = float(5.0)
varString = str("Test")
varBool = bool(True)
#char doesn't exist in python, they are just a standard string of len 1
#TPDP add in some unicode stuff

varList = [] #an empty list
varList = [1,2,3,4,5] #arrays are zero indexed
varList = [(i) for i in range(8)] #a way to generate and initialize an array (see list comprehensions https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions )
varList = list([1,2,3,4])

varTuple = (1,2,3) #tuples are like an array, elements in a tuple are nonmutable, but they can contain elements that are mutable (lists)
varTuple = 1,2,3 #another way to initialize a tuple
varTuple = (1) #for the single element case, this doesn't work to create a tuple
varTuple = (1,) #following the element with a comma does create a single element tuple
varTuple = tuple((1,))

varDic = {} #an empty dictionary
varDic = {1:'s',3:'4','t':'a'} #a dictionary
varDic = dict({1:'s',3:'4','t':'a'})

print(varList[0])
print(varTuple[0])
print(varDic['t'])
print("=======================================================================")

varInt, varReal = 6, 6.0 #python supports multivariable assignments
print("=======================================================================")

# https://docs.python.org/3/tutorial/datastructures.html#sets
#more examples below of how to use sets
varSet = set() #an empty set
varSet = set('abcdddde') #a set, holds an unordered set of unique elements (no duplicates
varSet = {1,2,3,4,5,5,5,5,5,5,6}
#print(varSet[0]) #you can't access sets like this
print(varSet) #note the duplicate elements are not printed
print("=======================================================================")

#multidimensional arrays aren't exactly standard in python, but can be made using an array of an array
#Note: add-ons for python (numpy) allows support for large multidimensional arrays
varArray2D = [[None for i in range(8)] for i in range(8)] #an example of making a two dimensional with all elements initilized to None, using 'list comprehensions'
print(varArray2D[0][0])
print("=======================================================================")

import copy
varArray2Db = copy.deepcopy(varArray2D) #instead of copying the reference of varArray2D, deepcopy(x) makes a complete element by element copy of x, etc...
print("=======================================================================")

#list slices
varList = [1,2,3,4,5]
print(varList[:2]) #starts from the begining of the list to element 2
print(varList[-2:]) #starts from seconds last element of list to last element
print(varList[2:]) #starts from element 2 to end of list

print(varList + [6,7,8,9]) #can concatinate lists
varList.append(6)

#some useful list methods
varList = [1,2,3,4,5]
varList.append(6) #appends something to the end of the list
varList.insert(0, 0) #at xth index, insert y
print(varList.pop()) #removes and returns last element of list
print(varList.pop(0)) #removes and returns xth element of list
print(varList.index(5)) #searches for x in list, returns index. Raises error if x isn't in list
del varList[0] #'del' can be used to delete a single element
del varList #'del' can also be used to delete an entire variable
print("=======================================================================")

#list comprehensions example from https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
example1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] #this is equivalent to the below example2
print(example1)
example2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            example2.append((x,y))
print(example2)
#both 'example1' and 'example2' are identicle
print("=======================================================================")

#sets 
# https://docs.python.org/3/tutorial/datastructures.html#sets
set1 = {1,2,3,4,4,4,3,3,2,1,1}
set2 = {0,1,8,9}
#some set operations
print(set1 - set2) #lists stuff in set1 that is NOT in set2
print(set1 | set2) #or
print(set1 & set2) #and
print(set1 ^ set2) #xor
for i in sorted(set1): #a way to loop over a set, note: sorted returns a lists containing elements in the set, but leaves set unchanged
    print(str(i))
print("=======================================================================")

#dictionaries
dic1 = {1:"test",2:"ing",3:"over"}
print(dic1.keys()) #returns the keys, but is unsorted/indexing not supported (not a list) (but you can still iterate over it in a for loop)
print(list(dic1.keys()))
print(sorted(dic1.keys()))
for i,j in dic1.items(): #when looping over a dictionary, can use this to get both the key and data at the same time
    print("dic key '" + str(i) + "' contains data '" + str(j) + "'")
print("=======================================================================")
    
#some stuff on bytes
import sys
print((5).to_bytes(2,sys.byteorder)) #can convert an int to n many byte
print(bytes([10])) #alternativly, you can use this, since 'bytes' is supposed to work on iterables
print(bytes([10,20,30,40]))
print(bytes(10)) #be carefull, this will actually make an array n bytes long instead of converting it
print((bytes([2,4,6,8,10,12,14,16])).hex()) #convert byte array to hex string
print("=======================================================================")

#some usefull casting stuff
temp = int("5A", 16) #convert hex string into int
