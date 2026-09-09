class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)

        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        distances = [-1] * n

        for indices in positions.values():
            if len(indices) == 1:
                continue

            length = len(indices)

            for j, index in enumerate(indices):
                prev_index = indices[j - 1]
                next_index = indices[(j + 1) % length]

                prev_distance = (index - prev_index) % n
                next_distance = (next_index - index) % n

                distances[index] = min(prev_distance, next_distance)

        return [distances[i] for i in queries]

solution = Solution()

print(solution.solveQueries(
    [1, 3, 1, 4, 1, 3, 2],
    [0, 3, 5]
))
# [2, -1, 3]

print(solution.solveQueries(
    [1, 2, 3, 4],
    [0, 1, 2, 3]
))
# [-1, -1, -1, -1]
