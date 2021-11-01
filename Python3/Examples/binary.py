"""
Author: Medic5700

An example of converting a number to a binary string and back
"""

def binary(t0 : int) -> str:
    """Takes in a number, returns a string representation of the number in binary (32-bit)"""
    assert(type(t0) == int)
    assert(t0 >= 0)

    t1 : str = ""
    for _ in range(0,32):
        if t0%2 == 0:
            t1 = "0" + t1
        else:
            t1 = "1" + t1
        t0 = t0//2.0
    return t1

def binary2(n : int) -> str:
    """Takes in a number, returns a string representation of the number in binary (32-bit)
    
    Uses bitwise operations"""
    assert(type(n) == int)
    assert(n >= 0)

    result : str = ""
    for _ in range(0,32):
        temp : str = "0" if (n & 1) == 0 else "1"
        result = temp + result
        n = n >> 1
    return result

def number(t0 : str) -> int:
    """Takes in a string representing a number in binary (32-bit), returns the number it represents"""
    assert(type(t0) == str)
    assert(len(t0) == 32)

    t1 : int = 0
    for i in range(0,32):
        t1 = t1*2
        if t0[i] == '1':
            t1 = t1 + 1
    return t1

def number2(binary : str) -> int:
    """Takes in a string representing a number in binary (arbitrary length), returns the number it represents
    
    Uses bitwise operations"""
    assert(type(binary) == str)
    assert(all([x in ['0','1'] for x in binary]))

    result : int = 0
    for i in binary:
        result = result << 1
        if i == '1':
            result = result | 1
    return result

if __name__ == "__main__":
    for i in range(0,256):
        print(str(i) + "\t=\t" + binary2(i) + "\t=\t" + str(number2(binary2(i))))
