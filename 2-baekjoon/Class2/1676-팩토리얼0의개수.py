"""
2025-04-14
"""

n = int(input())

count = 0
divider = 5
while n >= divider:
    count += n // divider
    divider *= 5

print(count)