"""
Author: Medic5700

Math stuff

Reference
    https://docs.python.org/3/tutorial/introduction.html#numbers
"""

#TODO add stuff about useing the '@' as a math operator for matrix multiplication ( https://www.askpython.com/python/oops/at-symbol-in-python )
#TODO number types IE: int, float, complex
''' 
#Basic Math
    +                                   - addition
    -                                   - subtraction
    *                                   - multiplication
    /                                   - division
    //                                  - int division (IE: floor division result)
    %                                   - modulus
    **                                  - exponent

    abs(x)                              - returns absolute value of x
    divmod(x,y)                         - returns both the quotient and remainder of a division
    pow(base,exp, mod=None)             - returns base ** exp % mod
    min(x)                              - minimum
    max(x)                              - maximum
    round(x, y=0)                       - round x to y digits after decimal point

Reference
    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
'''

print(2 + 5)                            # output 7
print(2 - 5)                            # output -3
print(2 * 5)                            # output 10
print(2 / 5)                            # output 0.4
print(2 // 5)                           # output 0
print(2 % 5)                            # output 2
print(2 ** 5)                           # output 32

print(abs(-2))                          # output 2
print(divmod(2, 5))                     # output (0, 2)
print(pow(2, 5))                        # output 32
print(min(2, 5))                        # output 2
print(max(2, 5))                        # output 5
print(round(10.123456789))              # output 10
print(round(10.123456789, 2))           # output 10.12
print("=======================================================================")

''' 
#Bitwise operators

>>  - shift bits right
<<  - shift bits left
&   - bitwise and
|   - bitwise or
^   - bitwise xor
~   - returns not, ones complement of x, is unary oporator IE: ~x

Reference
    https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
'''
print(bin(0b10 >> 2))                   # output 0b0
print(bin(0b10 << 2))                   # output 0b1000
print(bin(0b10 & 0b10))                 # output 0b10
print(bin(0b10 | 0b10))                 # output 0b10
print(bin(0b10 ^ 0b10))                 # output 0b0

print(bin(~0b10))                       # output -0b11
'''
Note: the output here is strange, that is because the output is being displayed 
as a negative binary number... which isn't quite the correct way to display it.
If you do binary operations on the number, it will be correct, it's the display
of the number that is unitutitive in python.
There is also some weirdness from the fact that numbers in python are arbitrary 
length.
'''
x : int = 10
print(f" {x} = {[1 if (2**i & x) else 0 for i in range(7, -1, -1)]} -> bin({x}) = {bin(x)}")
print(f"~{x} = {[1 if (2**i & ~x) else 0 for i in range(7, -1, -1)]} -> bin(~{x}) = {bin(~x)}")
print("=======================================================================")

'''
#Different number notations
    0b...                               - binary
    0o...                               - octal
    0x...                               - hexidecimal
    aeb                                 - e-notation, a is int or real, b is int, 'e' is the notation
    a+bj                                - complex number, a is int or real (can be omitted along with plus sign), b is int or real, 'j' is the notation
'''

print(0b1111)                           # output 15
print(bin(25))                          # output 0b11001
print(0o17)                             # output 15
print(oct(25))                          # output 0o31
print(0xF)                              # output 15
print(hex(25))                          # output 0x19

print(0e0)                              # output 0.0
print(1e0)                              # output 1.0
print(1.5e1)                            # output 15.0
print(1.5e+1)                           # output 15.0
print(1.5e-1)                           # output 0.15
print(-1.5e-1)                          # output -0.15

print(5j)                               # output 5j
print(5.5j)                             # output 5.5j
print(2+5j)                             # output (2+5j)

# Note: can include underscores in numbers to imrpove readability, the underscores are ignored
print(1_000)                            # output 1000
print(0b0000_0000_0000_1111)            # output 15
print("=======================================================================")

'''
Note: python has a limit on converting large numbers (4300 digits) to strings 
and vice versa
Note: this limit only effects the conversion from strings to ints and vice 
versa, it does not effect the underlying math, or the arbitrary length of 
python numbers

Reference
    https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation
'''
try:
    print(10**4300)
except Exception as e:
    print(e)
    # Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print("=======================================================================")

'''
#Python3 math module

Reference
    https://docs.python.org/3/library/math.html
'''

import math

print(math.e)                           # output 2.718281828459045
print(math.pi)                          # output 3.141592653589793
print(math.inf)                         # output inf # IE: positive infinity
print(math.nan)                         # output nan # IE: not a number

print(math.ceil(5.5))                   # output 6
print(math.floor(5.5))                  # output 5
print(math.log(100, 10))                # output 2.0
print(math.pow(10, 2))                  # output 100.0
print(math.sqrt(4))                     # output 2.0
print(math.isqrt(4))                    # output 2

print(math.cos(math.pi))                # output -1.0
print(math.sin(math.pi / 2))            # output 1.0
print(math.tan(math.pi / 4))            # output 0.9999999999999999
print("=======================================================================")

'''
Python3 also has support for Decimal, Fraction, and Complex Numbers #TODO ( https://docs.python.org/3/library/decimal.html#decimal.Decimal )
'''
print("=======================================================================")

'''
@   - used for matrix multiplication, but no default python objects support it (but the numpy module does)
'''
print("=======================================================================")
