from itertools import combinations


def choose_best_sum(t, k, ls):
    sums = [sum(distances) for distances in combinations(ls, k)]
    valid_sums = [total for total in sums if total <= t]

    return max(valid_sums) if valid_sums else None


# Test
print(choose_best_sum(163, 3, [50, 55, 56, 57, 58]))  # 163
print(choose_best_sum(163, 3, [50]))                   # None
print(choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87]))  # 228
print(choose_best_sum(174, 3, [50, 55, 57, 58, 60]))  # 173
