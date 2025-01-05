"""
게임개발
N X M의 맵
현재 방향에서 왼쪽으로 돌려 앞 칸이 가본 곳이라면 가고, 아니면 또 왼쪽으로 돌려본다
모두 가본 곳이라면 원래 방향에서 뒤로 한 칸 가는데, 바다면 움직임을 멈춘다
"""

n, m = map(int, input().split())
x, y, p = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(n)]

count = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

turn = 0
while True:
    new_x = x + dx[p]
    new_y = y + dy[p]
    print(new_x, new_y)

    if map_list[new_x][new_y] == 0:
        count += 1
        x = new_x
        y = new_y
        break

    if p == 0:
        p = 3
    else:
        p -= 1

    turn += 1
    if turn == 4:
        break

print(count)
print(x, y)