def fib3() -> int:
    a = 0
    yield a
    b = 1
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c

if __name__ == "__main__":
    generator = fib3()
    for i in range(0,11):
        print("fib(" + str(i) + ")\t= " + str(next(generator)))
    generator.close()
