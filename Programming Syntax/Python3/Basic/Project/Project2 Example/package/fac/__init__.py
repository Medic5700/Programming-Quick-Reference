#this __init__.py file allows this to be loaded, and specific modules in this subfolder to be loaded as well
from . import factorial #this is using Intra-package References https://docs.python.org/3/tutorial/modules.html#intra-package-references
#you can also use modules in parent directories etc...
from .. import fib
print("package/fac/__init__.py has access to fib => fib(8) = " + str(fib.fib(8)))
