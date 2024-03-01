import timeit

def fib_doubling(n):
    if n < 2:
        return n
    elif n > 100000001:
        raise ValueError("n is too large for this implementation.")
    return _fib_doubling(n)[0]

def _fib_doubling(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)

if __name__ == "__main__":
    print("fib_doubling 4500:", timeit.timeit('fib_doubling(4500)', globals=globals(), number=1))
    print("fib_doubling 4500000:", timeit.timeit('fib_doubling(4500000)', globals=globals(), number=1))
    print("fib_doubling 45000000:", timeit.timeit('fib_doubling(45000000)', globals=globals(), number=1))
    # The following line is commented out due to the boundary condition we added:
    # print("fib_doubling 450000000:", timeit.timeit('fib_doubling(450000000)', globals=globals(), number=1))
