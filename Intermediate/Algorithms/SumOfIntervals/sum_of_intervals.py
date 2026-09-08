def sum_intervals(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals)
    total = 0
    start, end = intervals[0]

    for current_start, current_end in intervals[1:]:
        if current_start <= end:
            end = max(end, current_end)
        else:
            total += end - start
            start, end = current_start, current_end

    total += end - start

    return total


# Test
print(sum_intervals([
    [1, 2],
    [6, 10],
    [11, 15]
]))  # 9

print(sum_intervals([
    [1, 4],
    [7, 10],
    [3, 5]
]))  # 7

print(sum_intervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
]))  # 19

print(sum_intervals([
    [0, 20],
    [-100000000, 10],
    [30, 40]
]))  # 100000030
