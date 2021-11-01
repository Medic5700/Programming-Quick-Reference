"""
Author: Medic5700

This is an example of generating a factorial using recursion.
"""

def factorial (n : int) -> int:
    """Takes in a number n, returns the factorial of n using recursion"""
    if (n > 1):
        return n * factorial (n - 1)
    else:
        return 1

if __name__ == "__main__":
    for i in range(0,11):
        print(str(i) + "!\t= " + str(factorial(i)))
