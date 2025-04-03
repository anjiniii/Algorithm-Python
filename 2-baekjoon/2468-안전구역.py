"""
2025-04-03=목요일
"""

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, graph))  # 최대 높이
max_region = 0  # 최대 안전 구역 수

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, height):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))  # queue에 방문할 노드 추가


    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] > h:
                bfs(i, j, visited, h)
                count += 1

    max_region = max(max_region, count)

print(max_region)


"""
import sys
sys.setrecursionlimit(10000)


def dfs(x, y, height, visited, graph, n):
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] > height:
                dfs(nx, ny, height, visited, graph, n)
"""