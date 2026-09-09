class Solution:
    def mirrorDistance(self, n: int) -> int:
        reversed_num = int(str(n)[::-1])
        return abs(n - reversed_num)


solution = Solution()

print(solution.mirrorDistance(25))
# 27

print(solution.mirrorDistance(10))
# 9

print(solution.mirrorDistance(7))
# 0
