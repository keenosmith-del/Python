from bisect import bisect_right


class Solution:
    def maximumWeight(
        self,
        intervals: list[list[int]]
    ) -> list[int]:
        n = len(intervals)

        indexed = [
            (left, right, weight, index)
            for index, (left, right, weight) in enumerate(intervals)
        ]

        indexed.sort()

        starts = [interval[0] for interval in indexed]

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        # using at most k intervals from i onward.
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            left, right, weight, original_index = indexed[i]

            next_index = bisect_right(starts, right)

            for k in range(1, 5):
                # Skip this interval.
                best_score, best_indices = dp[i + 1][k]

                # Take this interval.
                next_score, next_indices = dp[next_index][k - 1]

                take_score = weight + next_score
                take_indices = tuple(
                    sorted((original_index,) + next_indices)
                )

                if take_score > best_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < best_score:
                    dp[i][k] = (best_score, best_indices)
                else:
                    dp[i][k] = (
                        best_score,
                        min(best_indices, take_indices)
                    )

        return list(dp[0][4][1])


# Test
solution = Solution()

intervals = [
    [1, 3, 2],
    [4, 5, 2],
    [1, 5, 5],
    [6, 9, 3],
    [6, 7, 1],
    [8, 9, 1]
]

print(solution.maximumWeight(intervals))
# [2, 3]


intervals = [
    [5, 8, 1],
    [6, 7, 7],
    [4, 7, 3],
    [9, 10, 6],
    [7, 8, 2],
    [11, 14, 3],
    [3, 5, 5]
]

print(solution.maximumWeight(intervals))
# [1, 3, 5, 6]
