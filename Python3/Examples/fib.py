"""
Author: Medic5700

This is an example of generating the fibonacci sequence using recursion.
"""

def fib (n : int) -> int:
    """Takes in a number n, returns the nth number of the fionacci sequence using recursion"""

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for i in range(0,11):
        print("fib(" + str(i) + ")\t= " + str(fib(i)))
