#to show the basics of linking multiple files together
import factorial #allows access to all functions, etc... in file factorial.py
from fib import fib #allos access to a spicific function (fib) in file fib.py without referencing fib.py as a whole (IE: fib(x) instead of fib.fib(x))

print("8! = " + str(factorial.factorial(5)))
print("fib(8)= " + str(fib(5)))
