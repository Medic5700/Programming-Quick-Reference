#A module, all the functions and variables defined here would be acessable from the main program.

def fib (t1):
    if (t1==0):
        return 0
    elif (t1==1):
        return 1
    else:
        return fib(t1-1) + fib(t1-2)
    
def fib2 (t1):
    a = 0
    b = 1
    c = None
    if t1 == 0:
        return 0
    if t1 == 1:
        return 1
    for i in range(1, t1):
        c = a + b
        a = b
        b = c
    return c

print("fib.py has been loaded") #any code is run on the import statment (IE: a print)

if __name__ == "__main__": #this code will only run if this is the main program. If it's imported as a module, __name__ is not "__main__" and doesn't run.
    #this is done usually for module tests
    for i in range(0,11):
        print("fib(" + str(i) + ")\t= " + str(fib(i)))
    for i in range(0,11):
        print("fib2(" + str(i) + ")\t= " + str(fib2(i)))
