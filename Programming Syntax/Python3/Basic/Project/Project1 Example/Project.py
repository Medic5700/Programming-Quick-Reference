#to show the basics of linking multiple modules together
import factorial #allows access to all functions, etc... in file factorial.py
from fib import fib2 #allows access to a specific function (fib) in file fib.py without referencing fib.py as a whole (IE: fib(x) instead of fib.fib(x))
from factorial import * #allows importing of all functions in factorial that don't start with a '_' (IE: factorial._fac will not be available)
import moreStuff.subdirectoryFib #notice that accessing modules in subdirectories uses a '.' instead of a '/' for navagating through directories

print("8! = " + str(factorial.factorial_1(8)))
print("fib(8)= " + str(fib2(8)))
print("8! = " + str(factorial_1(8)))
print("fib(8)= " + str(moreStuff.subdirectoryFib.fib(8)))
