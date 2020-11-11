'''
# https://docs.python.org/3/tutorial/errors.html
'''

#basic try/except
temp = 0
try:
    temp = 2/0
except: #this will execute when ANY error comes up in the above try statment
    print("Error 0: attempt to divide by zero")
else: #optional
    #will execute iff no exceptions are raised in the try clause
    temp = 2
finally: #optional
    #will always execute after everything even if any exceptions are raised, 'finally' will run, and the exception will be re-raised
    print("Error 0 => temp = " + str(temp))
print("=======================================================================")

try:
    temp = 2/0
except NameError: #this allows the catching and handling of muletiple differet errors
    print("Error 1: NameError")
except ZeroDivisionError:
    print("Error 1: ZeroDicisionError")
except (IndexError, SyntaxError, ValueError): #you can handle multiple errors at the same time like this
    print("Error 1: Multiple Errors") 
except: #the all case, will catch any remaining error
    print("Error 1: SomeError")
''' (some common) built in exceptions, see link for full list
https://docs.python.org/3/library/exceptions.html#bltin-exceptions
 exception IndexError - Raised when a sequence subscript is out of range
 exception KeyError - Raised when a mapping (dictionary) key is not found in the set of existing keys
 exception NameError - Raised when a local or global name is not found
 exception RecursionError - It is raised when the interpreter detects that the maximum recursion depth (see sys.getrecursionlimit()) is exceeded
 exception SyntaxError - Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions exec() or eval(), or when reading the initial script or standard input (also interactively)
 exception TypeError - Raised when an operation or function is applied to an object of inappropriate type
 exception ZeroDivisionError - Raised when the second argument of a division or modulo operation is zero
 exception ValueError - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
OS Errors
 exception FileExistsError - Raised when trying to create a file or directory which already exists
 exception FileNotFoundError - Raised when a file or directory is requested but doesn’t exist
 exception PermissionError - Raised when trying to run an operation without the adequate access rights 
'''
print("=======================================================================")

#this one allows you to see what error information is given
try:
    temp = 2/0
except Exception as inst:
    print("Error 2: " + str(inst))

#raising an error
try:
    raise ZeroDivisionError
except:
    print("Error 3: Raised a ZeroDivisionError")

#raising an error with information
try:
    raise ZeroDivisionError("Information for Error 4")
except Exception as i:
    print("Error 4: Raised a ZeroDivisionError with information")
    print(i)
print("=======================================================================")

#creating an error class and raising it
class myError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "This is myError"
try:
    raise myError(5,6)
except myError as e:
    print("Error 5: raised an error = " + str(e.x))
    print(e)
print("=======================================================================")
