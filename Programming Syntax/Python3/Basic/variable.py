varInt = 5
varReal = 5.0
varString = "Test"
varBool = True
#char doesn't exist in python, they are just a standard string of len 1

varInt,varReal = 6,6.0 #python supports multivariable assignments

varList = [1,2,3,4,5] #arrays are zero indexed
varList = [(i) for i in range(8)] #a way to generate and initialize an array
varTuple = (1,2,3) #just like an array, elements in a tuple are nonmutable
varDic = {1:'s',3:'4','t':'a'} #a dictionary
print(varList[0])
print(varTuple[0])
print(varDic['t'])

#multidimensional arrays aren't exactly standard in python, but can be made using an array of an array
#Note: add-ons for python (numpy) allows support for large multidimensional arrays
varArray2D = [[None for i in range(8)] for i in range(8)] #an example of making a two dimensional with all elements initilized to None
print(varArray2D[0][0])

import copy
varArray2Db = copy.deepcopy(varArray2D) #instead of copying the reference of varArray2D, deepcopy(x) makes a complete element by element copy of x, etc...

#list slices
varList = [1,2,3,4,5]
print(varList[:2]) #starts from the begining of the list to element 2
print(varList[-2:]) #starts from seconds last element of list to last element
print(varList[2:]) #starts from element 2 to end of list

print(varList + [6,7,8,9]) #can concatinate lists
varList.append(6)
