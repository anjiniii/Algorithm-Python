"""
2025-04-07-월요일
"""

from collections import deque

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(arr, visited, w, h, i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


def solution(w, h):
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(arr, visited, w, h, i, j)
                count += 1

    print(count)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    solution(w, h)



