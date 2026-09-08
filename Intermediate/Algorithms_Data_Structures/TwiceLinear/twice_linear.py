def dbl_linear(n):
    u = [1]
    i = j = 0

    for _ in range(n):
        next_2 = 2 * u[i] + 1
        next_3 = 3 * u[j] + 1

        next_value = min(next_2, next_3)
        u.append(next_value)

        if next_value == next_2:
            i += 1

        if next_value == next_3:
            j += 1

    return u[n]


# Test
print(dbl_linear(10))  # 22
print(dbl_linear(20))  # 57
