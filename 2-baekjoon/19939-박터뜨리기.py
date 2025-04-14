"""
2025-04-14
"""

n, k = map(int, input().split())


def solution2():
    total = (1 + k) * k // 2
    if total > n:
        print(-1)
    elif (n - total) % k == 0:
        print(k - 1)
    else:
        print(k)


def solution():
    total = (1 + k) * k // 2
    if total > n:
        print(-1)
    elif total == n:
        print(k - 1)
    else:
        n -= total
        n %= k
        if n == 0:
            print(k - 1)
        else:
            print(k)