"""
미래도시
플로이드-워셜 알고리즘을 익히고 난 다음 문제라서 아이디어를 얻는데 어려움은 없었다.
다만 이 문제를 BFS로 풀면 시간/공간복잡도가 완화된다고 한다.
아직 탐색 알고리즘이 완전 와닿지 않아서 얼른 공부하고 다시 풀어봐야지.
"""

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]


# 자기 자신에게 가는 거리 0으로 초기화
for i in range(n + 1):
    graph[i][i] = 0


# 연결된 노드 표현
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 한 번 거쳐가는 경우
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 거쳐 가는 노드 번호
x, k = map(int, input().split())

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)