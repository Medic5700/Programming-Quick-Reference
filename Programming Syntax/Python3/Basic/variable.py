import copy

varInt = 5
varReal = 5.0
varString = "Test"
varBool = True

#arrays are zero indexed
varArray = [1,2,3,4,5]
varArray = [(i) for i in range(8)] #a way to generate and initialize an array
varTuple = (1,2,3) #just like an array, elements in a tuple are not changable
varDic = {1:'s',3:'4','t':'a'} #a dictionary
print(varArray[0])
print(varTuple[0])
print(varDic['t'])

#multidimensional arrays aren't exactly standard in python, but can be made using an array of an array
#Note: add-ons for python (numpy) allows support for large multidimensional arrays
varArray2D = [[None for i in range(8)] for i in range(8)] #an example of making a two dimensional with all elements initilized to None
print(varArray2D[0][0])

varArray2Db = copy.deepcopy(varArray2D) #instead of copying the reference of varArray2D, deepcopy(x) makes a complete element by element copy of x, etc...
