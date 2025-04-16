"""
2025-04-16
"""

import heapq

n = int(input())
heap = []
for _ in range(n):
    (x, y) = map(int, input().split())
    heapq.heappush(heap, (x, y))

while heap:
    x, y = heapq.heappop(heap)
    print(x, y)