class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        dp = [0] + [float("inf")] * n

        for position, limit in factory:
            new_dp = dp[:]

            for i in range(1, n + 1):
                distance = 0

                for k in range(1, min(limit, i) + 1):
                    distance += abs(robot[i - k] - position)

                    if dp[i - k] != float("inf"):
                        new_dp[i] = min(
                            new_dp[i],
                            dp[i - k] + distance
                        )

            dp = new_dp

        return dp[n]


solution = Solution()

print(solution.minimumTotalDistance(
    [9, 11, 99, 101],
    [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]]
))  # 6

print(solution.minimumTotalDistance(
    [0, 4, 6],
    [[2, 2], [6, 2]]
))  # 4

print(solution.minimumTotalDistance(
    [1, -1],
    [[-2, 1], [2, 1]]
))  # 2
