def func0(a : int, b : int, c : int) -> None: #function decliration, with full annotations
    """This is a docstring, used to tell what a function/class/module does""" #it's good practice to use this
    #it is good practice for a docstring to be in the format of 'input reults in output' IE:"""Do X and return a list."""
    #can be multi-lined, first line should be a one liner discription (IE:"""Do X and return a list"""), then an empty line, then as much detail as needed
    #the docstring will be used by python's help function to list what it does when queried
    
    global t1 #you must EXPLICITLY state global variables that can be used/modified
    t2 : int  = 5#by annoatating a varable like this, the interpriter is explicidly creating a local variable in the function memory scope
    print("Function 0: " + str(t1))
    return #this is valid, will return None (which is usually silently ignored)
    #functions don't need to have a return statment, but all functions return "None" if there is no return statment (which is usually silently ignored)
    
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
    output = str(a) + ","
    for i in b:
        output += output + "," + str(i)
    print("Function 3: arguments are = " + output)

func3(1)
func3(1,2,3,4,5,6,7,8,9,10)
print("=======================================================================")

# https://www.python.org/dev/peps/pep-0448/
def func4(a,b,c,d):
    print("Function 4: a,b,c,d = " + str(a) + "," + str(b) + "," + str(c) + "," + str(d))

t2 = range(1,5)
func4(*t2) #you can 'unpack' arguments stored in a list to use when calling a function (remember this is with a single '*')
t2 = [1,2,3,4]
func4(*t2)
t2 = {'a':1,'b':2,'c':3,'d':4}
func4(**t2) #dictionaries use a '**' instead
#this kind of unpacking only works for function definitions and function calls
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

#some stuff on generators
#https://realpython.com/introduction-to-python-generators/
def generator1():
    """produces the fibonacci sequence"""
    a = 0
    yield a #yield is life return, only instead of exiting the function, it pauses the function at the line, and reterns there when called
    b = 1
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c
        
gen1 = generator1()
for i in range(0,10):
    print("Generator1: " + str(next(gen1))) #next calls the generator to run until the next yeild
print("=======================================================================")
    
def generator2():
    """counts by 8 until 100"""
    i = 0
    while True:
        yield i
        i += 8
        if i > 100: 
            break
    #notice that when the generator ends without calling yeild (by breaking out the loop in this case), the generator stops interating
    #the generator will return the "StopIteration" exception in this case, and is what the for loop looks for to stop iterating

for i in generator2(): #another way to call/use a generator
    print("Generator2: " + str(i))
print("=======================================================================")
        
def generator3():
    """Takes in a number, and returns the rolling sum"""
    t = 0
    while True:
        i = (yield t) #here, yield can also take in a value
        if i != None:
            t += i

gen3 = generator3()
next(gen3) #sends a None to the generator to get it started?
for i in range(0,11):
    print("Gnerator3: " + str(gen3.send(i))) #gen3.send() sends a value to the generator
gen3.close() #closes the generator
print("=======================================================================")

#this is just like a list comprehension, only it's a generator and thus takes less memory
#note: generators take less memory, but are slower then list comprehensions
generater4 = (i**2 for i in range(10)) 
for i in generater4:
    print("Generator4: " + str(i))
print("=======================================================================")
