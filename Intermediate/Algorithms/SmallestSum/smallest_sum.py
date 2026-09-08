def solution(lst):
    numbers = lst[:]

    while len(set(numbers)) > 1:
        largest = max(numbers)
        smallest = min(numbers)

        index = numbers.index(largest)
        numbers[index] = largest - smallest

    return sum(numbers)


# Test
print(solution([6, 9, 21]))  # 9
print(solution([3, 3, 3]))   # 9
print(solution([10, 15, 25]))  # 15
