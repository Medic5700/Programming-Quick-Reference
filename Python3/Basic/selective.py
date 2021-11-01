'''Boolean operators
<    - less then
<=   - less then or equal
>    - greater then
>=   - greater then or equal
==   - equal
!=   - not equal
and  - and
or   - or
not  - not

all(list)- applies AND to a list of booleans, returns a single boolean
any(list)- applies OR to a list of booleans, returns a single boolean

in       - used to see if something is 'in' another array/object
not in   - 
is       - used to see if something is the same as another object
is not   - 
'''

for i in range(10):
    if i==0: #basic if/else
        print("if statement 0 option 0")
    elif i==1:
        print("if statement 0 option 1")
    else:
        print("if statement 0 option 2")
print("=======================================================================")

#some stuff with sets
if 1 in [1,2,3,4,5]: #tests if an element is in a container object
    print("if statement 1 = true, the element is in the container object")
else:
    print("if statement 1 = false, the element is not in the container object")
    
if [1,2,3] is [1,2,3]: #tests if an object is the same object (IE: those are two DIFFERENT arrays that just happen to contain the same data, hence, false)
    print("if statement 2 = true, they are the same object")
else:
    print("if statement 2 = false, they are not the same object")
    
if [1,2,3] == [1,2,3]:
    print("if statement 3 = true, container objects contian the same data")
else:
    print("if statement 3 = false, the container objects do NOT contain the same data")
print("=======================================================================")

#a one line if statment, usefull for list comprehensions
print("if statement 4 = true") if (1 in [1,2,3]) else print("if statment 4 = false") #this is equivilent to the below
'''
if (1 in [1,2,3]):
    print("if statement 4 = true") 
else:
    print("if statement 4 = false")
'''

''' #the 'if' AND 'else' are required for this to work, the below statement will not work and throw a parsing error
print("if statement 4 = true") if (1 in [1,2,3])
'''

#for variable assignment
temp = "if statement 5 = true" if False else "if statement 5 = false"
''' #the below will not work
temp = "if statement 5 = true" if False else temp = "if statement 5 = false"
'''
print(temp)

print("=======================================================================")

temp = [True, True, False, True]
if all(temp) == True:
    print("if statement 6A = true")
if any(temp) == True:
    print("if statement 6B = true")
else:
    print("if statement 6 = false")

print("=======================================================================")
#switch/cases statement (New in Python 3.10) #TODO
# https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
