"""
2025-04-24
"""

n, k = map(int, input().split())

INF = 9999999
dp = [INF] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    if i + i // 2 <= n:
        dp[i + i // 2] = dp[i] + 1

if dp[n] <= k:
    print("minigimbob")
else:
    print("water")
