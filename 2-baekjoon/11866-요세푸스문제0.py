"""
2025-04-04-금요일
"""
from collections import deque


def solution(n, k):
    people = [x for x in range(1, n+1)]
    queue = deque(people)
    result = []

    while queue:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    print("<" + ", ".join(map(str, result)) + ">")


n, k = map(int, input().split())
solution(n, k)