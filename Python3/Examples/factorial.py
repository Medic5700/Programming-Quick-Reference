def factorial (t1 : int) -> int:
    if (t1 > 1):
        return t1 * factorial (t1-1)
    else:
        return 1

if __name__ == "__main__":
    for i in range(0,11):
        print(str(i) + "!\t= " + str(factorial(i)))
