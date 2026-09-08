def fib(n):
    """Calculates the nth Fibonacci number"""
    def fast_doubling(n):
        if n == 0:
            return 0, 1

        a, b = fast_doubling(n // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return c, d
        else:
            return d, c + d

    if n >= 0:
        return fast_doubling(n)[0]

    result = fast_doubling(-n)[0]

    return -result if (-n) % 2 == 0 else result


# Test
print(fib(0))       # 0
print(fib(1))       # 1
print(fib(2))       # 1
print(fib(10))      # 55
print(fib(20))      # 6765
print(fib(-10))     # -55
print(fib(-11))     # 89
print(fib(100))     # 354224848179261915075
