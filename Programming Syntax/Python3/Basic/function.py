def func0(a,b,c):
    """This is a docstring, used to tell what a function/class/module does""" #it's good practice to use this
    #it is good practice for a docstring to be in the format of 'input reults in output' IE:"""Do X and return a list."""
    #can be multi-lined, first line should be a one liner discription (IE:"""Do X and return a list"""), then an empty line, then as much detail as needed
    
    global t1 #you must EXPLICITLY state global variables that can be used/modified
    print("Function 0: " + str(t1))
    return #this is valid, will return None (which is usually silently ignored)
    #functions don't need to have a return statment... but all functions return "None" if there is no return statment (which is usually silently ignored)
    
t1 = 10
func0(1,2,3)
print("=======================================================================")

def func1(a=10): #default values for arguments
    print("Function 1: " + str(a))
    
func1()
print("=======================================================================")

def func2(a,b=2,c=3,d=4):
    print("Function 2: a,b,c,d = " + str(a) + "," + str(b) + "," + str(c) + "," + str(d))
    
#you call functions using 'keyword arguments'
func2(1)
func2(1, d=5)
func2(a=2,c=10)
try: #these function calls don't work
    func2() #function needed one argument
    func2(2, a=2) #duplicate value for same argument
    func2(e=3) #keyword unknown
except:
    print("these fucntions fail")
print("=======================================================================")

def func3(a, *b): #functions can accept variable numbers of arguments
    #the '*b' allows for multiple arguments to be specified
    output = str(a)
    for i in b:
        output = output + "," + str(i)
    print("Function 3: arguments are = " + output)

func3(1)
func3(1,2,3,4,5,6,7,8,9,10)
print("=======================================================================")

def func4(a,b,c,d):
    print("Function 4: a,b,c,d = " + str(a) + "," + str(b) + "," + str(c) + "," + str(d))

t2 = range(1,5)
func4(*t2) #you can 'unpack' arguments stored in a list to use when calling a function (remember this is with a single '*')
t2 = [1,2,3,4]
func4(*t2)
t2 = {'a':1,'b':2,'c':3,'d':4}
func4(**t2) #dictionaries use a '**' instead
print("=======================================================================")

def func5(t1):
    """Takes a number, returns a lambda function"""
    print("Function 5 creating Function 6")
    return lambda x:x+t1 #lambda functions created without a name on the fly
    
func6 = func5(10) #here is a function being assigned to a variable
print("Function 6 in use " + str(func6(20))) #and here it is being used
print("=======================================================================")

#some stuff using partial functions
import functools #allows for fancier manipulation of functions

def funcSum(a,b,c,d):
    """sums a,b,c,d"""
    return a+b+c+d

partialFunction = functools.partial(funcSum)
for i in [0,1,2,3]:
    partial = functools.partial(partialFunction,i)
print("partial functions: " + str(partialFunction(1,2,3,4)))
print(funcSum.__doc__) #a functions docstring can be accessed with this
print("=======================================================================")
