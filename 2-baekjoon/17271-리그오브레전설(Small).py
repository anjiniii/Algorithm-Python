"""
2025-04-20
"""

# n: 싸움 시간, m: B 시간
n, m = map(int, input().split())

# dp[1] = 1
dp = [1] * (n + 1)

# dp[2] = dp[1] AA B
# dp[3] =  AAA AB BA
# dp[4] =  AAAA ABA BAA AAB BB
# dp[5] =  AAAAA ABAA BAAA AABA BBA AAAB ABB BAB
for i in range(m, n + 1):
    dp[i] = (dp[i - 1] + dp[i - m]) % 1000000007

print(dp[n])

