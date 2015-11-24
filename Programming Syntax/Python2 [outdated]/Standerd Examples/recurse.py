'''
    Author: 
    demostrates recursion type functions: fibbinacie, factorial
'''

def factorial (i):
    if i>1:
        return i*factorial(i-1)
    else:
        return i

def fib (i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fib(i-1) + fib(i-2)
    
if __name__ == "__main__":
    for i in range(0,11): #[0,21)
        print str(i) + "!\t= " + str(factorial(i)) + "\t\tfib(" + str(i) + ")\t= " + str(fib(i))