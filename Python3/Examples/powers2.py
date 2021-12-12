'''
Author: Medic5700

A simple program that displays the powers of 2.
An example with a focus on f-strings.

reference:
    https://realpython.com/python-f-strings/#arbitrary-expressions
'''

for i in range(21):
    print(f"2^{i}\t=\t{2**i}") #note: expressions inside the brackets implicitly call str()
