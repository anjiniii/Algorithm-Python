"""
1로 만들기

5로 나누어 떨어지면 5로 나눈다
3으로 나누어 떨어지면 3으로 나눈다
2로 나누어 떨어지면 2로 나눈다
1을 뺸다

최종 1로 만들기 위해 해야하는 연산의 수
"""

n = int(input())
count = 0

def first_answer(n):
    while n > 1:
        if n % 5 == 0:
            n //= 5
        elif n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 1
        count += 1

# print(count)


def min_operations(n, memo = {}):
    if n == 1:
        return 0
    if n in memo:
        return memo[n]

    # 1을 빼는 경우
    result = min_operations(n - 1, memo) + 1

    # 2, 3, 5로 나누는 경우 고려
    if n % 2 == 0:
        result = min(result, min_operations(n // 2, memo) + 1)
    if n % 3 == 0:
        result = min(result, min_operations(n // 3, memo) + 1)
    if n % 5 == 0:
        result = min(result, min_operations(n // 5, memo) + 1)

    memo[n] = result
    return result

# print(min_operations(n))

dp = [0] * 30001

def book_answer(x):
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
    return dp[x]

print(book_answer(n))