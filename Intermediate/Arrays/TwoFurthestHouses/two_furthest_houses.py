class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        answer = 0

        for i in range(n):
            if colors[i] != colors[0]:
                answer = max(answer, i)

            if colors[i] != colors[-1]:
                answer = max(answer, n - 1 - i)

        return answer

solution = Solution()

tests = [
    ([1, 1, 1, 6, 1, 1, 1], 3),
    ([1, 8, 3, 8, 3], 4),
    ([0, 1], 1),
]

for colors, expected in tests:
    result = solution.maxDistance(colors)

    print(f"Input:    {colors}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print(f"Passed:   {result == expected}")
    print()
