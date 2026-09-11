class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
print(solution.lengthOfLongestSubstring("bbbbb"))     # 1
print(solution.lengthOfLongestSubstring("pwwkew"))    # 3
print(solution.lengthOfLongestSubstring(""))          # 0
print(solution.lengthOfLongestSubstring(" "))         # 1
