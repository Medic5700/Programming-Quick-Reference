"""
Author: Medic5700

This is an example of the function caching decorator via generating the fibonacci sequence using recursion.
"""

import sys
version = sys.version_info
assert version[0] == 3 and version[1] >= 9 #asserts that the python version is 3.9 or higher

from functools import cache #The cache decorator is new in python 3.9

@cache #The cache decorator takes the function and caches the results
def fib (n : int) -> int:
    """Takes in a number n, returns the nth number of the fionacci sequence using recursion"""

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for i in range(11):
        print("fib(" + str(i) + ")\t= " + str(fib(i)))
