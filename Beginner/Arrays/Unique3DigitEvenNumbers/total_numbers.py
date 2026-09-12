class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        count = 0

        for hundreds in range(1, 10):
            for tens in range(10):
                for ones in range(0, 10, 2):
                    number = [hundreds, tens, ones]

                    available = digits.copy()

                    if all(d in available for d in number):
                        for d in number:
                            available.remove(d)

                        count += 1

        return count


solution = Solution()

print(solution.totalNumbers([1, 2, 3, 4]))  # 12
print(solution.totalNumbers([0, 2, 2]))     # 2
print(solution.totalNumbers([6, 6, 6]))     # 1
print(solution.totalNumbers([1, 3, 5]))     # 0
