"""
2025-04-09-수요일
"""

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

# 티셔츠
count_t = 0
for i in size:
    count_t += i // t
    count_t += 1 if i % t > 0 else 0
print(count_t)

# 펜
print(n // p, n % p)