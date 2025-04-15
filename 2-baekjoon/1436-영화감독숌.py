"""
2025-04-15
"""

n = int(input())

count = 0
num = 666
while True:
    if "666" in str(num):
        count += 1

    if count == n:
        print(num)
        break
    else:
        num += 1
