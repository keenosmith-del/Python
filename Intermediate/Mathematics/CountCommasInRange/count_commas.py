class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        power = 1000

        while power <= n:
            total += n - power + 1
            power *= 1000

        return total


# Test
solution = Solution()

print(solution.countCommas(1002))  # 3
print(solution.countCommas(998))   # 0
print(solution.countCommas(10000))  # 10001
