def factorial_1 (t1):
    if (t1 > 1):
        return t1 * factorial_1 (t1-1)
    else:
        return 1
    
def _fac (t1):
    a = 1
    for i in range(1,t1+1):
        a = a*i
    return a

if __name__ == "__main__":
    for i in range(0,11):
        print(str(i) + "!\t= " + str(factorial_1(i)))
    for i in range(0,11):
        print(str(i) + "!\t= " + str(_fac(i)))
