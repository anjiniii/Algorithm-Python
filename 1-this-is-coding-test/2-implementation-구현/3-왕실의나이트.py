"""
왕실의 나이트
8 X 8 좌표평면에서
나이트는 (수평 두 칸 후 수직 한 칸) 또는 (수직 두 칸 후 수평 한 칸)으로만 이동 가능
행은 1부터 8, 열은 a부터 h
나이트가 이동할 수 있는 경우의 수
"""
import time

input_string = input()
column = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
x = column[input_string[0]]
y = int(input_string[1])

count = 0
types = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for type in types:
    new_x = x + type[0]
    new_y = y + type[1]
    if new_x > 0 and new_x < 9 and new_y > 0 and new_y < 9:
        count += 1

print(count)

"""
풀고나서
더 효율적으로 할 수 없을까 고민했다..
GPT가 아래와 같은 코드를 추천해줬다.

우선 list가 아닌 tuple로 변경. 이유는 list는 가변이나 tuple은 불변이다.
더 적은 메모리를 차지하는 tuple로 적용.

그리고 필요한 값만 즉시 계산하는 제너레이터 표현식.
흠.. 식이 깔끔해지지만, 아직 익숙하지 않은 방법이고, 한번에 이해되지 않기도..
하지만 분명 더 짧고 효율적으로 보인다!
"""

# 나이트 이동 유형
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 이동 가능한 위치 계산
valid_moves = sum(
    1 for dx, dy in knight_moves
    if 1 <= x + dx <= 8 and 1 <= y + dy <= 8
)

# 결과 출력
print(valid_moves)