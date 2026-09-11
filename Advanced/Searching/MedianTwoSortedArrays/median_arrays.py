class Solution:
    def findMedianSortedArrays(
        self,
        nums1: list[int],
        nums2: list[int]
    ) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < m else float("inf")

            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2

            if left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted.")


solution = Solution()

print(solution.findMedianSortedArrays([1, 3], [2]))
# 2.0

print(solution.findMedianSortedArrays([1, 2], [3, 4]))
# 2.5

print(solution.findMedianSortedArrays([], [1]))
# 1.0

print(solution.findMedianSortedArrays([0, 0], [0, 0]))
# 0.0

print(solution.findMedianSortedArrays([1], [2, 3, 4, 5]))
# 3.0
