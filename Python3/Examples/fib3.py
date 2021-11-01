"""
Author: Medic5700

This is an example of generating the fibonacci sequence using a generator function.
"""

def fib3() -> int:
    """A generator function that returns the next number in the fibonacci sequance every call"""
    
    a : int = 0
    yield a
    b : int = 1
    yield b
    while True:
        c : int = a + b
        yield c
        a = b
        b = c

if __name__ == "__main__":
    generator = fib3()
    for i in range(0,11):
        print("fib(" + str(i) + ")\t= " + str(next(generator)))
    generator.close()
