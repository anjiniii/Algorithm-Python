"""
2025-03-31-Mon
"""

import math

m, n = map(int, input().split())
result = [True] * (n + 1)

result[0] = False
result[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if result[i]:
        for j in range(i * i, n + 1, i):
            result[j] = False
            print(i, j, result)

for i in range(m, n + 1):
    if result[i]:
        print(i)