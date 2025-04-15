"""
2025-04-15
"""

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n <= 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = dp[0] + arr[1]
    dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        a = dp[i - 1]  # X
        b = dp[i - 2] + arr[i] # O, 전 X
        c = dp[i - 3] + arr[i - 1] + arr[i] # O, 직전 O, 전전 X
        dp[i] = max(a, b, c)

    print(dp[n - 1])