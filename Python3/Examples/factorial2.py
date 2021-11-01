"""
Author: Medic5700

This is an example of generating a factorial.
"""

def factorial2(n : int) -> int:
	"""Takes in a number n, returns the factorial of n"""
	a : int = 1
	for i in range(1, n + 1):
		a = a * i
	return a

if __name__ == "__main__":
	for i in range(0,11):
		print(str(i) + "!\t= " + str(factorial2(i)))
