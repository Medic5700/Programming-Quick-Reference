def binary(t1):
    t2 = ""
    for i in range(0,33):
        if t1%2==1:
            t2 = "1" + t2
        else:
            t2 = "0" + t2
        t1 = t1//2
    return t2

def number(t1):
    t2 = 0
    for i in range(0,33):
        t2=t2*2
        if t1[i] == '1':
            t2 = t2 + 1
    return t2

if __name__ == "__main__":
    for i in range(0,256):
        print i, "\t=\t", binary(i), "\t=\t", number(binary(i))