import functools #allows for fancyer manipulation of functions

def func0(a,b,c):
    """This is a docstring, used to tell what a function/class/module does"""
    global t1 #you must EXPLICITLY state global variables that can be used
    print("Function 0: " + str(t1))

def func1(a=10): #default values for variables
    print("Function 1: " + str(a))
    
def func2(t1):
    """Takes a number, returns a function"""
    print("Function 2 creating Function 3")
    return lambda x:x+t1 #lambda functions created without a name on the fly
    
t1 = 10
func0(1,2,3)
func1()
func3 = func2(10) #here is a function being assigned to a variable
print("Function 3 in use " + str(func3(20)))

#some stuff using partial functions
def sum(a,b,c,d):
    return a+b+c+d
partialFunction = functools.partial(sum)
for i in [0,1,2,3]:
    partial = functools.partial(partialFunction,i)
print("partial functions: " + str(partialFunction()))
