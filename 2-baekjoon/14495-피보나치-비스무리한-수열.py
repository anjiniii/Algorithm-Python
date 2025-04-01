"""
2025-04-01-화요일
"""

n = int(input())


"""
dp 동적 계획법
시간 복잡도 O(n)
공간 복잡도 O(n)
"""
def solution_dp(n):
    if n in [1, 2, 3]:
        return 1

    dp = [0] * (n + 1)
    for i in range(4):
        dp[i] = 1

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    return dp[n]


"""
공간 최적화 dp
시간 복잡도 O(n)
공간 복잡도 O(1)
"""
def solution_dp2(n):
    if n in [1, 2, 3]:
        return 1

    a, b, c = 1, 1, 1
    for i in range(4, n + 1):
        a, b, c = b, c, a + c

    return c


"""
재귀
시간 복잡도 O(2^n)
공간 복잡도 O(n)
"""
def solution_fibo(n):
    if n in [1, 2, 3]:
        return 1

    answer = solution_fibo(n - 1) + solution_fibo(n - 3)
    return answer


print(solution_dp(n))
print(solution_dp2(n))
print(solution_fibo(n))