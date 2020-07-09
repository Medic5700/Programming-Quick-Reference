def fib (t1 : int) -> int:
    if (t1==0):
        return 0
    elif (t1==1):
        return 1
    else:
        return fib(t1-1) + fib(t1-2)

if __name__ == "__main__":
    for i in range(0,11):
        print("fib(" + str(i) + ")\t= " + str(fib(i)))
