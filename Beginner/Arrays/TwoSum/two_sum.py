def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)


# Test
print(two_sum([1, 2, 3], 4))  # (0, 2)
print(two_sum([3, 2, 4], 6))  # (1, 2)
