"""
전보

입력 크기를 고려하지 않은 채, 플로이드-워셜 알고리즘으로 해결했다.
간단한 케이스들은 통과하겠지만, 값이 커지면 어휴..!

다익스트라로 다시 풀어야겠다.
"""

n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]


for i in range(n + 1):
    graph[i][i] = 0


for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] != INF and graph[k][b] != INF:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(n + 1):
    print(graph[i])


count = 0
max_dist = 0
for i in graph[c]:
    if 0 < i and i < INF:
        count += 1
        max_dist = max(max_dist, i)

print(count, max_dist)