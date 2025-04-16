"""
2025-04-15
"""

t = int(input())
dp = [0] * 11
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])