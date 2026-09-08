def gap(g, m, n):
    def is_prime(num):
        if num < 2:
            return False

        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 1

        return True

    previous = None

    for number in range(m, n + 1):
        if is_prime(number):
            if previous is not None and number - previous == g:
                return [previous, number]

            previous = number

    return None


# Test
print(gap(2, 3, 50))      # [3, 5]
print(gap(2, 5, 7))       # [5, 7]
print(gap(2, 5, 5))       # None
print(gap(4, 130, 200))   # [163, 167]
print(gap(6, 100, 110))   # None
