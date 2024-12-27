"""
상하좌우
N X N 좌표에서 (왼쪽 위가 (1, 1))
L, R, U, D 후 최종 좌표는?
"""

n = int(input())
x, y = 1, 1
courses = list(input().split())

for course in courses:
    if course == 'L' and y > 1:
        y -= 1
    elif course == 'R' and y < n:
        y += 1
    elif course == 'U' and x > 1:
        x -= 1
    elif course == 'D' and x < n:
        x += 1

print(x, y)

"""
풀고나서
답안이 신기하다!

L, R, U, D에 따른 이동 방향을 이렇게 작성한다
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

그래서 개별적으로 두지 않고,
nx = x + dx[i]
ny = y + dy[i]
이렇게 이동시킨다.
"""