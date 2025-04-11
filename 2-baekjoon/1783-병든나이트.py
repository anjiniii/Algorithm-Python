"""
2025-04-11-금요일
"""

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, ((m - 1) // 2) + 1))
elif m < 7:  # n >= 3
    print(min(m, 4))
else:  # n >= 3
    print(m - 2)