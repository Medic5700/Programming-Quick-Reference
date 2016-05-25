#packages allow you to use a collection of modules
import package #this will not automatically allow access to all submodules (depending on the package)(see package/fac/__init__.py)
try:
    print(package.fib.fib(8))
except:
    print("package.fib.fib(8) did not work")

import package.fib #this allows you to load a specific module from the package
print(package.fib.fib(8))

import package.fac #see the file package/fac/__init__.py for why this works
#some packages are specifically configured to allow an importing of all (or some) modules
#in this example, importing the fac allows access to factorial.py in the folder fac because package/fac/__init__.py is specifically to import factorial.py
print(package.fac.factorial.factorial_1(8))
# http://stackoverflow.com/questions/9048518/importing-packages-in-python