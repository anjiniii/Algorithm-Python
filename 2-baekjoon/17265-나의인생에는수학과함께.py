"""
2025-04-26-토요일
"""

n = int(input())
routes = [input().split() for _ in range(n)]


def dfs(x, y, expression):
    global min_answer, max_answer
    if x == n -1 and y == n - 1:
        min_answer = min(min_answer, eval(expression))
        max_answer = max(max_answer, eval(expression))
        return

    if 0 <= x + 1 < n:
        if (x + y) % 2 == 0:
            dfs(x + 1, y, expression + routes[x + 1][y])
        else:
            dfs(x + 1, y, str(eval(expression + routes[x + 1][y])))

    if 0 <= y + 1 < n:
        if (x + y) % 2 == 0:
            dfs(x, y + 1, expression + routes[x][y + 1])
        else:
            dfs(x, y + 1, str(eval(expression + routes[x][y + 1])))


min_answer = 5 ** 5
max_answer = -(5 ** 5)

dfs(0, 0, routes[0][0])
print(max_answer, min_answer)