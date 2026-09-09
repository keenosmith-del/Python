class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        result = 0
        n = len(nums2)

        for i in range(len(nums1)):
            left = i
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] >= nums1[i]:
                    result = max(result, mid - i)
                    left = mid + 1
                else:
                    right = mid - 1

        return result


solution = Solution()

print(solution.maxDistance(
    [55, 30, 5, 4, 2],
    [100, 20, 10, 10, 5]
))
# 2

print(solution.maxDistance(
    [2, 2, 2],
    [10, 10, 1]
))
# 1

print(solution.maxDistance(
    [30, 29, 19, 5],
    [25, 25, 25, 25, 25]
))
# 2
