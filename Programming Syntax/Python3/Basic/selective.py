'''
<    - less then
<=   - less then or equal
>    - greater then
==   - equal
!=   - not equal
and  - and
or   - or
not  - not
'''
'''
in   - used to see if something is 'in' another array/object
is   - used to see if something is the same as another object
'''

for i in range(10):
    if i==0: #basic if/else
        print("if statment 0 option 0")
    elif i==1:
        print("if statment 0 option 1")
    else:
        print("if statment 0 option 2")

#some stuff with sets
if 1 in [1,2,3,4,5]: #tests if an element is in a container object
    print("if statment 1 = true, the element is in the container object")
else:
    print("if statment 1 = false, the element is not in the container object")
    
if [1,2,3] is [1,2,3]: #tests if an object is the same object (IE: those are two DIFFERENT arrays that just happen to contain the same data, hence, false)
    print("if statment 2 = true, they are the same object")
else:
    print("if statment 2 = false, they are not the same object")
    
if [1,2,3] == [1,2,3]:
    print("if statment 3 = true, container objects contian the same data")
else:
    print("if statment 3 = false, the container objects do NOT contain the same data")

#a one line if statment, usefull for list comprehensions
print("if statment 4 = true") if (1 in [1,2,3]) else print("if statment 4 = false") #this is equivilent to the below
'''
if (1 in [1,2,3]):
    print("if statment 4 = true") 
else:
    print("if statment 4 = false")
'''
