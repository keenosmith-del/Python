import math


def list_squared(m, n):
    result = []

    for number in range(m, n + 1):
        total = 0

        for divisor in range(1, math.isqrt(number) + 1):
            if number % divisor == 0:
                total += divisor ** 2

                pair = number // divisor

                if pair != divisor:
                    total += pair ** 2

        root = math.isqrt(total)

        if root * root == total:
            result.append([number, total])

    return result
