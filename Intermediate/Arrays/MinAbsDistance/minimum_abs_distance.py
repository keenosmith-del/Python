class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        last_seen = {}
        result = float("inf")

        for j, num in enumerate(nums):
            if num in last_seen:
                result = min(result, j - last_seen[num])

            reversed_num = int(str(num)[::-1])
            last_seen[reversed_num] = j

        return result if result != float("inf") else -1


solution = Solution()

print(solution.minMirrorPairDistance([12, 21, 45, 33, 54]))
# 1

print(solution.minMirrorPairDistance([120, 21]))
# 1

print(solution.minMirrorPairDistance([21, 120]))
# -1
