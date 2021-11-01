"""
Author: Medic5700

This is an example of generating the fibonacci sequence.
"""

def fib2 (n : int) -> int:
	"""Takes in a number n, returns the nth number of the fibonacci sequance"""
	
	if n == 0:
		return 0
	if n == 1:
		return 1
	a : int = 0
	b : int = 1
	c : int = 1
	for _ in range(1, n):
		c = a + b
		a = b
		b = c
	return c

if __name__ == "__main__":
	for i in range(0,11):
		print("fib(" + str(i) + ")\t= " + str(fib2(i)))
