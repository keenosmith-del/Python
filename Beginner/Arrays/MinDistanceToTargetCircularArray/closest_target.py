class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        distances = []

        for i, word in enumerate(words):
            if word == target:
                distance = abs(i - startIndex)
                distance = min(distance, n - distance)
                distances.append(distance)

        return min(distances) if distances else -1


solution = Solution()

print(solution.closestTarget(
    ["hello", "i", "am", "leetcode", "hello"],
    "hello",
    1
))  # 1

print(solution.closestTarget(
    ["a", "b", "leetcode"],
    "leetcode",
    0
))  # 1

print(solution.closestTarget(
    ["i", "eat", "leetcode"],
    "ate",
    0
))  # -1
