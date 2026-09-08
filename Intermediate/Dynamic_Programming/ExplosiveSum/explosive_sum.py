def exp_sum(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for number in range(1, n + 1):
        for total in range(number, n + 1):
            dp[total] += dp[total - number]

    return dp[n]


# Test
print(exp_sum(1))    # 1
print(exp_sum(2))    # 2
print(exp_sum(3))    # 3
print(exp_sum(4))    # 5
print(exp_sum(5))    # 7
print(exp_sum(10))   # 42
print(exp_sum(50))   # 204226
print(exp_sum(80))   # 15796476
print(exp_sum(100))  # 190569292
