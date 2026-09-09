class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        count = {}
        total = {}

        for i, value in enumerate(nums):
            if value in count:
                result[i] += i * count[value] - total[value]

            count[value] = count.get(value, 0) + 1
            total[value] = total.get(value, 0) + i

        count.clear()
        total.clear()

        for i in range(n - 1, -1, -1):
            value = nums[i]

            if value in count:
                result[i] += total[value] - i * count[value]

            count[value] = count.get(value, 0) + 1
            total[value] = total.get(value, 0) + i

        return result


solution = Solution()

tests = [
    (
        [1, 3, 1, 1, 2],
        [5, 0, 3, 4, 0]
    ),
    (
        [0, 5, 3],
        [0, 0, 0]
    ),
    (
        [1, 1],
        [1, 1]
    ),
    (
        [1, 2, 1, 2, 1],
        [6, 4, 4, 4, 6]
    ),
]

for nums, expected in tests:
    result = solution.distance(nums)

    print(f"Input:    {nums}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print(f"Passed:   {result == expected}")
    print()
