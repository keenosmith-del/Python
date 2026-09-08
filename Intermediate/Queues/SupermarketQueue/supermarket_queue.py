def queue_time(customers, n):
    tills = [0] * n

    for customer in customers:
        shortest = tills.index(min(tills))
        tills[shortest] += customer

    return max(tills)


# Test
print(queue_time([5, 3, 4], 1))       # 12
print(queue_time([10, 2, 3, 3], 2))   # 10
print(queue_time([2, 3, 10], 2))      # 12
print(queue_time([], 1))              # 0
