'''
Author: Medic5700

Math stuff
'''

# http://www.tutorialspoint.com/python/python_numbers.htm
# https://docs.python.org/3/tutorial/introduction.html#numbers
''' #basic Math
+   - addition
-   - subtraction
*   - multiplication
@   - matrix multiplication (currently not implimented) #TODO include version time stamp of when last checked
/   - division
//  - floor division
%   - modulus
**  - exponent
'''

print(pow(10, 2))                # output 100
print(min(10, 2))                # output 2
print(max(10, 2))                # output 10
print(round(10.123456789, 2))    # output 10.15
print("=======================================================================")

''' #bitwise operators
>>  - shift bits right
<<  - shift bits left
&   - bitwise and
|   - bitwise or
^   - bitwise xor
~   - returns complement of x, is unary oporator IE: ~x
'''

print(0b1111)   # output 15
print(0o17)     # output 15
print(0xF)      # output 15
print(bin(25))  # output 0b11001
print(oct(25))  # output 0o31
print(hex(25))  # output 0x19
print("=======================================================================")

# https://docs.python.org/3.2/library/math.html
import math
print(math.e)               # output 2.718281828459045
print(math.pi)              # output 3.141592653589793
print(math.ceil(5.5))       # output 6
print(math.floor(5.5))      # output 5
print(math.log(100, 10))    # output 2.0
print(math.pow(10, 2))      # output 100.0
print(math.sqrt(4))         # output 2.0
print("=======================================================================")

'''
Python3 also has support for Decimal, Fraction, and Complex Numbers #TODO
'''
print("=======================================================================")

'''
@   - used for matrix multiplication, but no default python objects support it (but the numpy module does)
'''
print("=======================================================================")
