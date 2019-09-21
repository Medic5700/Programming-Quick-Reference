def factorial2(t1):
	a = 1
	for i in range(1,t1 + 1):
		a = a * i
	return a

if __name__ == "__main__":
	for i in range(0,11):
		print(str(i) + "!\t= " + str(factorial2(i)))
