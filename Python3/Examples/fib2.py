def fib2 (t1 : int) -> int:
	if t1 == 0:
		return 0
	if t1 == 1:
		return 1
	a = 0
	b = 1
	c = 1
	for i in range(1, t1):
		c = a + b
		a = b
		b = c
	return c

if __name__ == "__main__":
	for i in range(0,11):
		print("fib(" + str(i) + ")\t= " + str(fib2(i)))
