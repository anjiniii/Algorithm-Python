"""
2025-04-11-금요일
"""

import heapq


def solution1():
    n = int(input())
    queue = []

    for i in range(n):
        age, name = input().split()
        age = int(age)
        heapq.heappush(queue, (age, i, name))

    for _ in range(n):
        result = heapq.heappop(queue)
        print(result[0], result[2])


def solution2():
    n = int(input())
    members = [input().split() for _ in range(n)]
    members.sort(key=lambda x: int(x[0]))
    for age, name in members:
        print(age, name)


solution2()