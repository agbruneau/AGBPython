import timeit


def fib_doubling(n):
    if (n < 2) or (n > 100000001):
        return n
    """ Calculate the Nth Fibonacci number using the doubling method. """
    return _fib_doubling(n)[0]


def _fib_doubling(n):
    """ Calculate Nth Fibonacci number using the doubling method. Return the
    tuple (F(n), F(n+1))."""
    if n == 0:
        return 0, 1
    else:
        a, b = _fib_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return d, c + d
        else:
            return c, d


if __name__ == "__main__":

    
    # Compute parameters
    print("fib_doubling 4 500 :", timeit.timeit(
        'fib_doubling(4500)', globals=globals(), number=1))
    print("fib_doubling 4 500 000 :", timeit.timeit(
        'fib_doubling(4500000)', globals=globals(), number=1))
    print("fib_doubling 45 000 000 :", timeit.timeit(
        'fib_doubling(45000000)', globals=globals(), number=1))
#    print("fib_doubling 450 000 000 :", timeit.timeit(
#        'fib_doubling(450000000)', globals=globals(), number=1))
