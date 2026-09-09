class Solution(object):

    def getMinDistance(self, nums, target, start):
        return min(
            abs(i - start)
            for i in range(len(nums))
            if nums[i] == target
        )


# Test
solution = Solution()

print(solution.getMinDistance([1, 2, 3, 4, 5], 5, 3))  # 1
print(solution.getMinDistance([1], 1, 0))                # 0
print(solution.getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0))  # 0
