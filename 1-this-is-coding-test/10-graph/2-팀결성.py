"""
팀결성
팀 합치기 0 a b
팀 확인 1 a b
"""

# n은 학생 수(0 ~ n), m은 연산의 수
n, m = map(int, input().split())

# 자신의 팀의 가장 첫 번째 학생
team_root = [i for i in range(n + 1)]


# 최상단 팀원 찾기
def find(team_root, x):
    if team_root[x] != x:
        team_root[x] = find(team_root, team_root[x])  # 경로 압축
    return team_root[x]


def union(team_root, a, b):
    a_root = find(team_root, a)
    b_root = find(team_root, b)
    if a_root > b_root:
        team_root[a] = find(team_root, b)
    else:
        team_root[b] = find(team_root, a)


def check(team_root, a, b):
    a_root = find(team_root, a)
    b_root = find(team_root, b)
    if a_root == b_root:
        print("YES")
    else:
        print("NO")


for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(team_root, a, b)  # 합치기 연산
    elif x == 1:
        check(team_root, a, b)  # 같은 팀 확인



