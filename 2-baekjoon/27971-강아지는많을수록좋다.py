"""
2025-04-23
"""

n, m, a, b = map(int, input().split())
INF = 999999999
dp = [INF] * (n + 1)
dp[0] = 0

for _ in range(m):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        dp[i] = -1

for i in range(1, n + 1):
    # 닫힌 구간
    if dp[i] == -1:
        continue

    # 이전 값에서 더해질 수 있으면 변경
    min_a, min_b = INF, INF
    if -1 < dp[i - a] < INF:
        min_a = dp[i - a]
    if -1 < dp[i - b] < INF:
        min_b = dp[i - b]
    dp[i] = min(min_a, min_b) + 1

if dp[n] >= INF:
    print(-1)
else:
    print(dp[n])