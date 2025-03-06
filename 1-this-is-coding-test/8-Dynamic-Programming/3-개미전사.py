"""
개미 전사
"""

n = int(input())
food = list(map(int, input().split()))


def answer():
    dp = [0] * 100

    dp[0] = food[0]
    dp[1] = max(dp[0], food[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + food[i], dp[i - 1])

    print(dp[n - 1])


# 이 답안이 조금 더 와닿는 것 같다!!
def gpt():
    if n == 1:
        print(food[0])

    prev2 = food[0]
    prev1 = max(food[0], food[1])

    for i in range(2, n):
        current = max(prev2 + food[i], prev1)
        prev2, prev1 = prev1, current

    print(prev1)