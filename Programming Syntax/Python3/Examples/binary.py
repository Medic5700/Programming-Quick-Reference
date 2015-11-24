def binary(t0):
    t1 = ""
    for i in range(0,32):
        if t0%2 == 0:
            t1 = "0" + t1
        else:
            t1 = "1" + t1
        t0 = t0//2.0
    return t1

def number(t0):
    t1 = 0
    for i in range(0,32):
        t1 = t1*2
        if t0[i] == '1':
            t1 = t1 + 1
    return t1

if __name__ == "__main__":
    for i in range(0,256):
        print(str(i) + "\t=\t" + binary(i) + "\t=\t" + str(number(binary(i))))
